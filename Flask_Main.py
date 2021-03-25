from flask import Flask, render_template, url_for
app = Flask(__name__)

desc = "Create an account or log into Facebook. Connect with friends, family and other people you know. Share photos and videos, send messages and get updates."

user_info = [
    {
        "name": "Finn",
        "age" : "17",
        "hobbies": "making web applications in Python"
    }
]

posts_info = [
    {
        'author': 'Finn',
        'title': 'My 17th Birthday',
        'content': 'I got a bike for my 17th birthday'
    },
    {
        'author': 'Finn',
        'title': 'A Walk in the Park',
        'content': 'I took a walk in the park today'
    },
    {
        'author': 'Finn',
        'title': 'Flying to Hawaii',
        'content': 'I flew to Hawaii today'
    }
]

friends_info = [
    {
        'name': 'Matthew',
        'age': '18',
    },
    {
        'name': 'Micheal',
        'age': '18',
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', description = desc, title = "Home Page")


@app.route("/user_page")
def user_page():
    return render_template('user_page.html', user_info = user_info)

@app.route("/posts")
def posts():
    return render_template('posts.html', posts_info = posts_info)

@app.route("/friends")
def friends():
    return render_template('friends.html', friends_info = friends_info)


if __name__ == '__main__':
    app.run(debug=True)