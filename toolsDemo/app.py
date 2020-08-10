
from flask import Flask, request, render_template, redirect, flash
from random import randint, choice, sample


app = Flask(__name__)
app.config['SECRET_KEY'] = "adfasedira"


@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/form')
def show_form():
    return render_template("form.html")


@app.route('/form2')
def show_form2():
    return render_template("form2.html")


COMPLIMENTS = ["cool", "clever", "tenacious", "awesome", "Pythonic"]


@app.route('/greeter')
def greet():
    username = request.args["username"]
    nice_thing = choice(COMPLIMENTS)
    return render_template("greet.html", username=username, compliment=nice_thing)


@app.route('/greet2')
def greet2():
    username = request.args["username"]
    wants = request.args.get("wants_compliments")
    nice_things = sample(COMPLIMENTS, 3)
    return render_template("greet2.html", username=username, wants_compliments=wants, compliments=nice_things)


@app.route('/hello')
def say_hello():
    """ Return simple Hello Greeting"""

    return render_template("hello.html")


@app.route('/lucky')
def lucky_number():
    num = randint(1, 5)
    return render_template('lucky.html', lucky_num=num, msg="You are so lucky")


@app.route('/spell/<word>')
def spell(word):
    caps_word = word.upper()
    return render_template("spell.html", word=caps_word)


# --------------------------------------------------------------
# REDIRECTING


@app.route('/old-home-page')
def redirect_to_home():
    flash('That page has moved! This is our new home page!')
    return redirect("/")


MOVIES = {'Amadeus', 'Chicken Run', 'Dances with Wolves'}
""" Fake Database """


@app.route('/movies')
def show_all_moves():
    """Show list of all movies in fake database"""
    return render_template('movies.html', movies=MOVIES)


@app.route('/movies/new', methods=["POST"])
def add_movie():
    title = request.form['title']
    # add to pretend db
    if title in MOVIES:
        flash('Movie already exists', 'error')
    else:
        MOVIES.add(title)
    # ADD IN YOUR FLASH
        flash("Created your Movie!", 'success')

    return redirect('/movies')
