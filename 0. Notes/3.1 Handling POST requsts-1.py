#Handle POST Requests
#When a POST request is sent, that means the user has filled out our form and submitted it. We want to take the data from the form and use it to create a new blog post.
import json
from flask import Flask, render_template, request, redirect, url_for#import redirect and url_for

app = Flask(__name__)

def load_posts():
    with open('storage.json', 'r') as file:
        return json.load(file)

#to save the post after creating a new post
def save_posts(posts):
    with open('storage.json', 'w') as file:
        json.dump(posts, file, indent=4)

@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST': # to get the data from our form.
        blog_posts = load_posts()
        new_post = {
            "id": len(blog_posts) + 1,  # Simple way to generate a new ID
            "author": request.form.get('author'),
            "title": request.form.get('title'),
            "content": request.form.get('content')
        }
        blog_posts.append(new_post)
        save_posts(blog_posts)
        return redirect(url_for('index')) #redirecting the user back to the home page to view all the blog postings.
    return render_template('add.html')














if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



