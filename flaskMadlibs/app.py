from flask import Flask, request, render_template
from random import choice, sample
from stories import story


app = Flask(__name__)


@app.route('/')
def home_page():
    prompts = story.prompts
    return render_template("home.html", prompts=prompts)


@app.route('/story')
def make_madlib():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]

    return render_template("story.html", place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun)
