# Backend Note App

Educational project for learning backend development with FastAPI and Firestore. The main goal is to create a simple note-taking application with user authentication and CRUD operations for notes using Firestore as the database and consume the API with a React frontend.

## Architecture

The application follows this main architecture:

![Architecture](architecture.png)

### How to use makefile

The makefile is used to simplify common tasks. Here are some of the available commands:

- `make setup`: Create and activate a virtual environment and install dependencies.
- `make run-local`: Run the FastAPI application with Uvicorn.