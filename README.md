# Masterblog

Masterblog is a simple blog application built with Flask that allows users to create, view, update, and delete blog posts. It also includes a "Like" feature for posts. Data is persisted in a JSON file.

## Features

- **Index Page**: View all blog posts.
- **Add Post**: Create new blog posts with an author, title, and content.
- **Update Post**: Edit existing blog posts.
- **Delete Post**: Remove blog posts.
- **Like Post**: Increment a like counter for any post.
- **Persistent Storage**: All posts are saved in `storage.json`.

## Prerequisites

- Python 3.x
- Flask

## Installation

1. Navigate to the `Masterblog-flask` directory.
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To start the Flask development server:

```bash
python app.py
```

The application will be available at `http://localhost:5000`.

## Project Structure

- `app.py`: Main Flask application file.
- `storage.json`: JSON file used for data persistence.
- `templates/`: HTML templates for rendering pages.
- `static/`: Static files (CSS).
- `requirements.txt`: List of Python dependencies.
- `.gitignore`: Files and directories to be ignored by Git.
