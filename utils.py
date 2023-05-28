import json

DATAFILE = 'candidates.json'


def load_candidates_from_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates


def get_candidate(candidate_id):
    candidates = load_candidates_from_json(DATAFILE)
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    candidates = load_candidates_from_json(DATAFILE)
    filtered_candidates = [candidate for candidate in candidates if
                           candidate_name.lower() in candidate['name'].lower().split()]
    return filtered_candidates


def get_candidates_by_skill(skill_name):
    candidates = load_candidates_from_json(DATAFILE)
    filtered_candidates = [candidate for candidate in candidates if
                           skill_name.lower() in candidate['skills'].lower().split(', ')]
    return filtered_candidates


def get_all():
    candidates = load_candidates_from_json(DATAFILE)
    return candidates
