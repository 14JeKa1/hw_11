import json


def load_candidates_from_json() -> list[dict]:
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def get_candidate(candidate_id) -> dict:
    for condidate in load_candidates_from_json():
        if condidate['id'] == candidate_id:
            return condidate

def get_candidates_by_name(candidate_name:str) -> list[dict]:
    rsult = []
    for condidate in load_candidates_from_json():
        if condidate['name'] == candidate_name:
            rsult.append(condidate)
    return rsult

def get_candidates_by_skill(skill_name) -> list[dict]:
    rsult = []
    for condidate in load_candidates_from_json():
        if skill_name in condidate['skills'].lower().split(', '):
            rsult.append(condidate)
    return rsult

print(get_candidates_by_skill('python'))
