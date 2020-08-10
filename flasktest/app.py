from flask import Flask, request
app = Flask(__name__)

#new comment to fix author
@app.route('/')
def home_page():
    """ Return simple Hello Greeting"""
    html = """
    <html>
        <body>
            <h1>Home page!</h1>
            <p>This is the home page1</p>
            <a href=/hello>Click me to go to hello page</a>
        </body>
    </html?
    """
    return html


@app.route('/hello')
def say_hello():
    """ Return simple Hello Greeting"""
    html = """
    <html>
        <body>
            <h1>Hello!</h1>
            <p>This is the hello page</p>
        </body>
    </html?
    """
    return html


@app.route('/search')
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1>Search Results form: {term}</h1> <p>Sorting by: {sort}</p>"


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
