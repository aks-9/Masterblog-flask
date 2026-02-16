#setting up the home route (or URL) that our blog will respond to, and also design the data structure for saving our blog posts.

# 1.Data Structure for Blog Posts
# we’ll start by using a list of dictionaries to store our blog posts, where each dictionary represents a blog post.
# In each dictionary, we’ll have keys for 'author’, 'title’, and 'content’.

blog_posts = [
    {"id": 1, "author": "John Doe", "title": "First Post", "content": "This is my first post."},
    {"id": 2, "author": "Jane Doe", "title": "Second Post", "content": "This is another post."}
    # More blog posts can go here...
]

# Save it as a JSON file
# Your data structure should be saved in a JSON file, which will be used as a storage file. Your storage file will contain this data structure, and whenever you need to read, update, add or delete a blog post, change it directly.
# create storage.json and paste the data structure into it.
# then in the app.py import json and add a function to read the json file.
import json
def load_posts():
    with open('storage.json', 'r') as file:
        return json.load(file)

# 2. Create the Index Route
# Our next step is to create the index route (/). This route will display all blog posts. We’ll create a function (for instance, index()) that sends our list of blog posts to a template for display.

from flask import render_template

@app.route('/')
def index():
    # add code here to fetch the blog posts from a file
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)

# In this function, we’re using Flask’s render_template function to render the index.html template. We’re also passing our list of blog posts to the template with posts=blog_posts. In the template, we’ll be able to access this list with the variable name posts.


#create an index.html file inder templates folder and a style.css under static folder

