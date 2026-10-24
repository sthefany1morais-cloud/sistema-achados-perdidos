from flask import Flask, render_template, request, redirect, url_for, flash
import redis

app = Flask(__name__)
app.secret_key = "chave-local-desenvolvimento"

# Conexão com o Redis
db = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True,
    socket_connect_timeout=5
)


def listar_objetos(busca=""):
    """Consulta os objetos cadastrados e filtra os resultados."""
    ids = db.smembers("objetos:ids")
    objetos = []

    for objeto_id in sorted(ids, key=int, reverse=True):
        dados = db.hgetall(f"objeto:{objeto_id}")

        if not dados:
            continue

        dados["id"] = objeto_id

        texto = " ".join([
            dados.get("nome", ""),
            dados.get("descricao", ""),
            dados.get("categoria", ""),
            dados.get("local", "")
        ]).casefold()

        if busca.casefold() in texto:
            objetos.append(dados)

    return objetos


@app.route("/")
def inicio():
    """Exibe a página inicial e a lista de objetos."""
    busca = request.args.get("busca", "").strip()

    try:
        objetos = listar_objetos(busca)

        return render_template(
            "index.html",
            objetos=objetos,
            busca=busca
        )

    except redis.RedisError:
        flash("Não foi possível consultar o banco de dados.")
        return render_template(
            "index.html",
            objetos=[],
            busca=busca
        ), 503


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    """Cadastra um novo objeto encontrado."""
    nome = request.form.get("nome", "").strip()
    descricao = request.form.get("descricao", "").strip()
    categoria = request.form.get("categoria", "").strip()
    local = request.form.get("local", "").strip()

    if not all([nome, descricao, categoria, local]):
        flash("Preencha todos os campos.")
        return redirect(url_for("inicio"))

    try:
        # Confere a conexão com o Redis
        db.ping()

        # Gera um identificador único, preservando cadastros existentes
        with db.pipeline() as pipeline:
            pipeline.watch("objetos:proximo_id")

            contador = pipeline.get("objetos:proximo_id")

            if contador is None:
                ids_existentes = pipeline.smembers("objetos:ids")
                maior_id = max(
                    (int(i) for i in ids_existentes if i.isdigit()),
                    default=0
                )
                pipeline.multi()
                pipeline.set("objetos:proximo_id", maior_id)
                pipeline.execute()

            pipeline.unwatch()

        objeto_id = str(db.incr("objetos:proximo_id"))

        # Grava o objeto e seu identificador no Redis
        with db.pipeline() as pipeline:
            pipeline.hset(
                f"objeto:{objeto_id}",
                mapping={
                    "nome": nome,
                    "descricao": descricao,
                    "categoria": categoria,
                    "local": local,
                    "status": "Encontrado"
                }
            )
            pipeline.sadd("objetos:ids", objeto_id)
            pipeline.execute()

        flash("Objeto cadastrado com sucesso!")

    except redis.RedisError:
        flash("Erro ao salvar o objeto. Verifique se o Redis está funcionando.")

    return redirect(url_for("inicio"))


@app.route("/devolver/<objeto_id>", methods=["POST"])
def devolver(objeto_id):
    """Marca um objeto como devolvido."""
    if not objeto_id.isdigit():
        flash("Identificador inválido.")
        return redirect(url_for("inicio"))

    try:
        chave = f"objeto:{objeto_id}"

        if db.exists(chave):
            db.hset(chave, "status", "Devolvido")
            flash("Status atualizado: objeto devolvido.")
        else:
            flash("Objeto não encontrado.")

    except redis.RedisError:
        flash("Não foi possível atualizar o objeto no banco de dados.")

    return redirect(url_for("inicio"))


@app.route("/excluir/<objeto_id>", methods=["POST"])
def excluir(objeto_id):
    """Exclui um objeto cadastrado."""
    if not objeto_id.isdigit():
        flash("Identificador inválido.")
        return redirect(url_for("inicio"))

    try:
        chave = f"objeto:{objeto_id}"

        # Exclui o registro e remove o ID da coleção
        with db.pipeline() as pipeline:
            pipeline.watch(chave)

            if not pipeline.exists(chave):
                pipeline.unwatch()
                flash("Objeto não encontrado.")
            else:
                pipeline.multi()
                pipeline.delete(chave)
                pipeline.srem("objetos:ids", objeto_id)
                pipeline.execute()
                flash("Objeto excluído com sucesso!")

    except redis.RedisError:
        flash("Não foi possível excluir o objeto do banco de dados.")

    return redirect(url_for("inicio"))


if __name__ == "__main__":
    try:
        db.ping()
        print("Conexão com o Redis estabelecida com sucesso!")
        app.run(debug=True)

    except redis.RedisError:
        print(
            "Erro: não foi possível conectar ao Redis. "
            "Verifique se o contêiner está em execução."
        )