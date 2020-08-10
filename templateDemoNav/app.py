from flask import Flask, request, render_template
from random import randint, choice, sample


app = Flask(__name__)


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


@app.route('/search')
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1>Search Results form: {term}</h1> <p>Sorting by: {sort}</p>"


@app.route('/spell/<word>')
def spell(word):
    caps_word = word.upper()
    return render_template("spell.html", word=caps_word)

# @app.route('/post', methods=['POST'])
# def post():
#     return "YOPU MADE A POST REQUREST"

# @app.route('/post', methods=['GET'])
# def get():
#     return "YOPU MADE A GET REQUREST"

# get request for form


@app.route('/add-comment')
def add_comment_form():
    return """
    <h1>Add Comment</h1>
    <form method="POST">
        <input type='text' placeholder='comment' name='comment'/>
        <input type='text' placeholder='username' name='username'/>
        <button>Submit</button>
    </form>
    """


@app.route('/add-comment', methods=["POST"])
def save_comment():
    comment = request.form["comment"]
    username = request.form["username"]
    # print(request.from_values)
    return f"""
    <h1>Saved your comment!</h1>
    <ul>
        <li>Username: {username}</li>
        <li>Comment: {comment}</li>
    </ul>
    """


@app.route('/r/<subreddit>')
# this variable must mach EXACTLY as the route is passing it automatically
def show_subreddit(subreddit):
    return f"<h1> Browsing the {subreddit} Subreddit"


""" POSTS is a mock database"""
POSTS = {
    1: "I like chicken tenders",
    2: "I hate mayo",
    3: "Double rainbow all the way",
    4: "YOLO OMG"
}


@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS.get(id, "Post not found")
    return f"<p>{post}</p>"
