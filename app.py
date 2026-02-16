#"Add" Route
#We’re going to make the /add route, which will display a form for creating a new blog post if a GET request is sent,
# and add a new blog post to our list if a POST request is sent.

import json
from flask import Flask, render_template, request #import request

app = Flask(__name__)

def load_posts():
    with open('storage.json', 'r') as file:
        return json.load(file)

@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)

# Create the Route and the Function
@app.route('/add', methods=['GET', 'POST']) #In the @app.route decorator, we’ve added methods=['GET', 'POST']. This tells Flask that this route should respond to both GET and POST requests.
def add():
    if request.method == 'POST':
        # We will fill this in the next step
        pass
    return render_template('add.html')

#If a POST request is sent to this route, we want to add a new blog post. If any other type of request is sent (or by default, a GET request), we want to display a form for adding a new blog post. We’ve set up an if statement to handle this.












if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



