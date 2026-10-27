"""Regras simples para sugerir possíveis correspondências entre perdas e achados."""
import re
from repositories.occurrence_repository import all_for_matching

STOP_WORDS = {
    "de", "da", "do", "das", "dos", "e", "a", "o", "um", "uma",
    "no", "na", "em", "com", "para", "por", "que"
}

def tokens(text):
    words = re.findall(r"[a-zA-ZÀ-ÿ0-9]+", (text or "").lower())
    return {w for w in words if len(w) > 2 and w not in STOP_WORDS}

def score_pair(lost, found):
    score = 0
    reasons = []
    if (lost.get("categoria", "").casefold() == found.get("categoria", "").casefold()
            and lost.get("categoria")):
        score += 3
        reasons.append("mesma categoria")

    lost_words = tokens(lost.get("nome", "") + " " + lost.get("descricao", ""))
    found_words = tokens(found.get("nome", "") + " " + found.get("descricao", ""))
    common = lost_words & found_words
    if common:
        score += min(4, len(common) * 2)
        reasons.append("palavras em comum: " + ", ".join(sorted(common)[:4]))

    lost_location = tokens(lost.get("local", ""))
    found_location = tokens(found.get("local", ""))
    if lost_location & found_location:
        score += 2
        reasons.append("local semelhante")

    return score, reasons

def suggestions_for(occurrence_id):
    records = all_for_matching()
    current = next((r for r in records if r["id"] == occurrence_id), None)
    if not current:
        return []
    current_type = current.get("tipo", "achado")
    if current_type not in {"perdido", "achado"}:
        return []
    target_type = "achado" if current_type == "perdido" else "perdido"
    suggestions = []
    for other in records:
        if other["id"] == occurrence_id or other.get("tipo", "achado") != target_type:
            continue
        if other.get("status") in {"Devolvido", "Encerrado"}:
            continue
        lost, found = (current, other) if current_type == "perdido" else (other, current)
        score, reasons = score_pair(lost, found)
        if score >= 3:
            suggestions.append({"occurrence": other, "score": score, "reasons": reasons})
    return sorted(suggestions, key=lambda item: item["score"], reverse=True)
