from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def index():
    """Глвная страница"""
    candidates: list[dict] = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:idx>')
def page(idx):
    candidate = get_candidate(idx)
    if not candidate:
        return f"<h1>Нет кандидата с id {idx}</h1>"
    return render_template('candidate.html', candidate=candidate)


@app.route('/search/<string:name>')
def search_by_name(name):
    candidates: list[dict] = get_candidates_by_name(name)
    return render_template('search.html', candidates=candidates)

@app.route('/skills/<string:skill>')
def search_by_skills(skill):
    candidates: list[dict] = get_candidates_by_skill(skill)
    return render_template('skill.html', candidates=candidates, skill=skill)


if __name__ == '__main__':
    app.run()
