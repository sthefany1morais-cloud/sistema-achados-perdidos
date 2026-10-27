import json
from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash, Response
from extensions import get_redis
from repositories.occurrence_repository import list_all, get, create, update, delete
from services.matching_service import suggestions_for

main_bp = Blueprint("main", __name__)

CATEGORIES = [
    "Eletrônicos", "Documentos", "Acessórios", "Material escolar",
    "Roupas", "Chaves", "Bolsas e mochilas", "Outros"
]

def filtered_records():
    records = list_all()
    query = request.args.get("busca", "").strip().casefold()
    kind = request.args.get("tipo", "").strip()
    status = request.args.get("status", "").strip()
    result = []
    for item in records:
        if query:
            searchable = " ".join(item.get(field, "") for field in ("nome", "descricao", "categoria", "local")).casefold()
            if query not in searchable:
                continue
        if kind and item.get("tipo", "achado") != kind:
            continue
        if status and item.get("status", "Aberto") != status:
            continue
        result.append(item)
    return result

@main_bp.get("/")
def index():
    records = filtered_records()
    all_records = list_all()
    stats = {
        "total": len(all_records),
        "perdidos": sum(1 for x in all_records if x.get("tipo") == "perdido" and x.get("status") != "Devolvido"),
        "achados": sum(1 for x in all_records if x.get("tipo", "achado") == "achado" and x.get("status") != "Devolvido"),
        "devolvidos": sum(1 for x in all_records if x.get("status") == "Devolvido"),
    }
    return render_template("index.html", records=records, stats=stats,
                           busca=request.args.get("busca", ""),
                           tipo=request.args.get("tipo", ""),
                           status=request.args.get("status", ""))

@main_bp.route("/nova", methods=["GET", "POST"])
def nova():
    if request.method == "POST":
        fields = {
            "tipo": request.form.get("tipo", "achado").strip(),
            "nome": request.form.get("nome", "").strip(),
            "descricao": request.form.get("descricao", "").strip(),
            "categoria": request.form.get("categoria", "").strip(),
            "local": request.form.get("local", "").strip(),
            "data_ocorrencia": request.form.get("data_ocorrencia", "").strip(),
            "status": "Aberto",
        }
        if fields["tipo"] not in {"perdido", "achado"}:
            flash("Selecione se o objeto foi perdido ou encontrado.", "erro")
            return render_template("form.html", item=fields, categories=CATEGORIES, editing=False)
        if not all(fields[k] for k in ("nome", "descricao", "categoria", "local")):
            flash("Preencha nome, descrição, categoria e local.", "erro")
            return render_template("form.html", item=fields, categories=CATEGORIES, editing=False)
        occurrence_id = create(fields)
        flash(f"Ocorrência cadastrada! Código: R-{occurrence_id}", "sucesso")
        return redirect(url_for("main.detalhe", occurrence_id=occurrence_id))
    return render_template("form.html", item={}, categories=CATEGORIES, editing=False)

@main_bp.route("/editar/<occurrence_id>", methods=["GET", "POST"])
def editar(occurrence_id):
    item = get(occurrence_id)
    if not item or not item.get("tipo"):
        flash("Registro não encontrado ou antigo demais para edição. Cadastre novamente se necessário.", "erro")
        return redirect(url_for("main.index"))
    if request.method == "POST":
        fields = {
            "tipo": request.form.get("tipo", "").strip(),
            "nome": request.form.get("nome", "").strip(),
            "descricao": request.form.get("descricao", "").strip(),
            "categoria": request.form.get("categoria", "").strip(),
            "local": request.form.get("local", "").strip(),
            "data_ocorrencia": request.form.get("data_ocorrencia", "").strip(),
        }
        if fields["tipo"] not in {"perdido", "achado"} or not all(fields[k] for k in ("nome", "descricao", "categoria", "local")):
            flash("Confira os campos obrigatórios.", "erro")
            return render_template("form.html", item={**item, **fields}, categories=CATEGORIES, editing=True)
        update(occurrence_id, fields)
        flash("Ocorrência atualizada.", "sucesso")
        return redirect(url_for("main.detalhe", occurrence_id=occurrence_id))
    return render_template("form.html", item=item, categories=CATEGORIES, editing=True)

@main_bp.get("/ocorrencia/<occurrence_id>")
def detalhe(occurrence_id):
    item = get(occurrence_id)
    if not item:
        flash("Ocorrência não encontrada.", "erro")
        return redirect(url_for("main.index"))
    suggestions = suggestions_for(occurrence_id)
    return render_template("detail.html", item=item, suggestions=suggestions)

@main_bp.post("/devolver/<occurrence_id>")
def devolver(occurrence_id):
    item = get(occurrence_id)
    if not item or not item.get("tipo"):
        flash("Registro não encontrado.", "erro")
    elif item.get("tipo") != "achado":
        flash("Só um objeto encontrado pode ser marcado como devolvido.", "erro")
    else:
        update(occurrence_id, {"status": "Devolvido", "devolvido_em": str(datetime.now().timestamp())})
        flash("Devolução registrada com sucesso.", "sucesso")
    return redirect(url_for("main.detalhe", occurrence_id=occurrence_id))

@main_bp.post("/encerrar/<occurrence_id>")
def encerrar(occurrence_id):
    if update(occurrence_id, {"status": "Encerrado"}):
        flash("Ocorrência encerrada.", "sucesso")
    else:
        flash("Não foi possível encerrar este registro.", "erro")
    return redirect(url_for("main.detalhe", occurrence_id=occurrence_id))

@main_bp.post("/excluir/<occurrence_id>")
def excluir(occurrence_id):
    if delete(occurrence_id):
        flash("Ocorrência excluída.", "sucesso")
    else:
        flash("Registro não encontrado.", "erro")
    return redirect(url_for("main.index"))

@main_bp.get("/exportar")
def exportar():
    records = list_all()
    payload = json.dumps(records, ensure_ascii=False, indent=2)
    return Response(payload, mimetype="application/json",
                    headers={"Content-Disposition": "attachment; filename=reencontra-backup.json"})
