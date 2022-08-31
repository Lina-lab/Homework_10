import json

from candidates import Candidates


def load_candidates(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_all(data):
    arr = []
    for item in data:
        candidates = Candidates(item['name'], item['pk'], item['position'], item['picture'], item['skills'].lower())
        arr.append(candidates)
    return arr


def get_by_pk(pk, arr):
    for item in arr:
        if item.pk == pk:
            return item

def get_by_skills(skill_name, data):
    arr =[]
    for item in data:
        if skill_name in item.skill_name:
            arr.append(item)
    return arr


