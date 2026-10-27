"""
Camada de acesso aos dados.
Usamos estruturas nativas do Redis:
- Hash: campos de cada ocorrência;
- Set: conjunto de IDs;
- String: contador de IDs;
- Sorted Set: ocorrências ordenadas pelo instante de criação.
Não usamos banco de documentos.
"""
import time
from extensions import get_redis

IDS_KEY = "ocorrencias:ids"
COUNTER_KEY = "ocorrencias:proximo_id"
TIMELINE_KEY = "ocorrencias:por_data"

def _key(occurrence_id):
    return f"ocorrencia:{occurrence_id}"

def list_all():
    db = get_redis()
    ids = db.zrevrange(TIMELINE_KEY, 0, -1)
    result = []
    for occurrence_id in ids:
        data = db.hgetall(_key(occurrence_id))
        if data:
            data["id"] = occurrence_id
            result.append(data)
    # Compatibilidade com registros antigos criados no primeiro protótipo:
    # naquela versão, os Hashes tinham chaves objeto:<id>.
    seen = {item["id"] for item in result}
    for occurrence_id in sorted(
        get_redis().smembers("objetos:ids"),
        key=lambda x: int(x) if x.isdigit() else 0,
        reverse=True
    ):
        if occurrence_id in seen:
            continue
        legacy = get_redis().hgetall(f"objeto:{occurrence_id}")
        if legacy:
            legacy["id"] = occurrence_id
            legacy.setdefault("tipo", "achado")
            legacy.setdefault("status", "Aberto")
            legacy.setdefault("criado_em", str(time.time()))
            result.append(legacy)
    return result

def get(occurrence_id):
    data = get_redis().hgetall(_key(occurrence_id))
    if data:
        data["id"] = occurrence_id
        return data
    # Migração simples do objeto de teste usado na versão anterior.
    legacy = get_redis().hgetall(f"objeto:{occurrence_id}")
    if legacy:
        legacy["id"] = occurrence_id
        legacy.setdefault("tipo", "achado")
        legacy.setdefault("criado_em", str(time.time()))
        return legacy
    return None

def create(fields):
    db = get_redis()
    # Evita colisão com IDs antigos se o contador ainda não existir.
    if not db.exists(COUNTER_KEY):
        existing = db.smembers(IDS_KEY)
        legacy_ids = [int(x) for x in existing if x.isdigit()]
        db.set(COUNTER_KEY, max(legacy_ids, default=0))
    occurrence_id = str(db.incr(COUNTER_KEY))
    now = str(time.time())
    data = dict(fields)
    data["criado_em"] = now
    data.setdefault("status", "Aberto")
    db.hset(_key(occurrence_id), mapping=data)
    db.sadd(IDS_KEY, occurrence_id)
    db.zadd(TIMELINE_KEY, {occurrence_id: float(now)})
    return occurrence_id

def update(occurrence_id, fields):
    db = get_redis()
    if not db.exists(_key(occurrence_id)):
        # Não atualizar diretamente registros legados; serão editáveis após novo cadastro.
        return False
    db.hset(_key(occurrence_id), mapping=fields)
    return True

def delete(occurrence_id):
    db = get_redis()
    key = _key(occurrence_id)
    if not db.exists(key):
        return False
    db.delete(key)
    db.srem(IDS_KEY, occurrence_id)
    db.zrem(TIMELINE_KEY, occurrence_id)
    return True

def all_for_matching():
    return list_all()
