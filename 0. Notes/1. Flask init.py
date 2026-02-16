
# Create a Basic Flask Module

# Create a new GitHub repository in your profile.
# Create a new PyCharm Project.
# Clone the repository to your PyCharm project using the terminal.
# Initialize your Flask app:
# Create a new file called app.py and write the following lines of code to initialize your Flask app.

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

# Push (add, commit, push) your code to the repository.
# Verify that the code was successfully uploaded to your repository by browsing to GitHub.
# PreviousNext