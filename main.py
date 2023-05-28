from flask import Flask, render_template, request
from utils import get_candidate, get_candidates_by_name, get_candidates_by_skill, get_all

app = Flask(__name__)


@app.route('/')
def candidates():
    candidates = get_all()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:id>')
def candidate(id):
    candidate_data = get_candidate(id)
    if candidate_data:
        return render_template('single.html', candidate=candidate_data)
    else:
        return "Кандидат не найден"


@app.route('/skill', defaults={'skill_name': None})
@app.route('/skill/<skill_name>')
def skill(skill_name):
    if skill_name:
        # Если передан параметр skill_name, выполняем поиск по навыкам
        filtered_candidates = get_candidates_by_skill(skill_name)
    else:
        # Если параметр skill_name не передан, получаем его из запроса
        skill_name = request.args.get('skill')
        filtered_candidates = get_candidates_by_skill(skill_name)

    count = len(filtered_candidates)
    return render_template('skill.html', candidates=filtered_candidates, count=count)


@app.route('/search', defaults={'candidate_name': None})
@app.route('/search/<candidate_name>')
def search(candidate_name):
    if candidate_name:
        # Если передан параметр candidate_name, выполняем поиск по имени
        filtered_candidates = get_candidates_by_name(candidate_name)
    else:
        # Если параметр candidate_name не передан, получаем его из запроса
        candidate_name = request.args.get('name')
        filtered_candidates = get_candidates_by_name(candidate_name)

    count = len(filtered_candidates)
    return render_template('search.html', candidates=filtered_candidates, count=count)


if __name__ == '__main__':
    app.run()
