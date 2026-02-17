#Delete route

import json
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
STORAGE_FILE = 'storage.json'


def load_posts():
    """Load blog posts from the JSON file. Returns an empty list if file doesn't exist."""
    if not os.path.exists(STORAGE_FILE):
        return []
    try:
        with open(STORAGE_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_posts(posts):
    """Save blog posts to the JSON file."""
    with open(STORAGE_FILE, 'w') as file:
        json.dump(posts, file, indent=4)

@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """Handle adding a new blog post."""
    if request.method == 'POST':
        blog_posts = load_posts()

        # Generate a unique ID (max current ID + 1, or 1 if no posts exist)
        new_id = max([post['id'] for post in blog_posts], default=0) + 1

        new_post = {
            "id": new_id,
            "author": request.form.get('author'),
            "title": request.form.get('title'),
            "content": request.form.get('content')
        }

        blog_posts.append(new_post)
        save_posts(blog_posts)
        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    blog_posts = load_posts()

    # Create a new list to store posts we want to keep
    updated_posts = []

    # Go through each post in the current list
    for post in blog_posts:
        # If the post ID is NOT the one we want to delete, add it to our new list
        if post['id'] != post_id:
            updated_posts.append(post)

    save_posts(updated_posts)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



