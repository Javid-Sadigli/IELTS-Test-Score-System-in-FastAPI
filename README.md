# IELTS Test Score System (FastAPI)

This project is an IELTS Test Score System built with FastAPI. It provides a RESTful API for managing students and their IELTS test scores. The system allows you to create, retrieve, update, and delete student records and their associated test results. It is designed for educational institutions or organizations that need to track IELTS test performance.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [API Endpoints](#api-endpoints)
  - [Student Endpoints](#student-endpoints)
  - [Test Endpoints](#test-endpoints)
- [How to Run with Docker Compose](#how-to-run-with-docker-compose)
- [Requirements](#requirements)
- [Local Development (without Docker)](#local-development-without-docker)
- [Contributing](#contributing)


## Features
- Manage students (CRUD operations)
- Manage IELTS test scores for students
- RESTful API endpoints
- Dockerized for easy deployment

## Project Structure
```
├── controllers/
│   ├── student_controller.py
│   └── test_controller.py
├── db/
│   └── db.py
├── models/
│   ├── student.py
│   └── test.py
├── routers/
│   ├── student_router.py
│   └── test_router.py
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yaml
```

## How It Works
- **main.py**: Entry point. Initializes FastAPI app and includes routers.
- **models/**: Pydantic models for Student and Test data.
- **db/db.py**: Handles in-memory or persistent storage (implementation-dependent).
- **controllers/**: Business logic for students and tests.
- **routers/**: API route definitions for students and tests.

## API Endpoints

### Student Endpoints

- `GET /students`
  - **Response:**
    ```json
    [
      {
        "id": 1,
        "full_name": "John Doe",
        "email": "john@example.com"
      },
      {
        "id": 2,
        "full_name": "Jane Smith",
        "email": "jane@example.com"
      }
    ]
    ```

- `GET /students/{student_id}`
  - **Response (Success):**
    ```json
    {
      "id": 1,
      "full_name": "John Doe",
      "email": "john@example.com"
    }
    ```
  - **Response (Not Found):**
    ```json
    { "error": "Student not found" }
    ```

- `POST /students`
  - **Request Body:**
    ```json
    {
      "full_name": "John Doe",
      "email": "john@example.com"
    }
    ```
  - **Response:**
    ```json
    {
      "id": 1,
      "full_name": "John Doe",
      "email": "john@example.com"
    }
    ```

- `DELETE /students/{student_id}`
  - **Response (Success):**
    ```json
    { "message": "Student deleted successfully" }
    ```
  - **Response (Not Found):**
    ```json
    { "error": "Student not found or could not be deleted" }
    ```

- `GET /students/{student_id}/tests`
  - **Response (Success):**
    ```json
    [
      {
        "id": 1,
        "student_id": 1,
        "reading_score": 8.0,
        "writing_score": 7.0,
        "listening_score": 7.5,
        "speaking_score": 7.0,
        "total_score": 7.5
      }
    ]
    ```
  - **Response (Student Not Found):**
    ```json
    { "error": "Student not found" }
    ```

- `PUT /students/{student_id}`
  - **Request Body:**
    ```json
    {
      "full_name": "Updated Name",
      "email": "updated@email.com"
    }
    ```
  - **Response (Success):**
    ```json
    {
      "id": 1,
      "full_name": "Updated Name",
      "email": "updated@email.com"
    }
    ```
  - **Response (Not Found):**
    ```json
    { "error": "Student not found or could not be updated" }
    ```

### Test Endpoints

- `GET /tests`
  - **Response:**
    ```json
    [
      {
        "id": 1,
        "student_id": 1,
        "reading_score": 8.0,
        "writing_score": 7.0,
        "listening_score": 7.5,
        "speaking_score": 7.0,
        "total_score": 7.5
      }
    ]
    ```

- `GET /tests/{test_id}`
  - **Response (Success):**
    ```json
    {
      "id": 1,
      "student_id": 1,
      "reading_score": 8.0,
      "writing_score": 7.0,
      "listening_score": 7.5,
      "speaking_score": 7.0,
      "total_score": 7.5
    }
    ```
  - **Response (Not Found):**
    ```json
    { "error": "Test not found" }
    ```

- `POST /tests`
  - **Request Body:**
    ```json
    {
      "student_id": 1,
      "listening": 7.5,
      "reading": 8.0,
      "writing": 6.5,
      "speaking": 7.0
    }
    ```
  - **Response (Success):**
    ```json
    {
      "id": 1,
      "student_id": 1,
      "reading_score": 8.0,
      "writing_score": 6.5,
      "listening_score": 7.5,
      "speaking_score": 7.0,
      "total_score": 7.25
    }
    ```
  - **Response (Student Not Found):**
    ```json
    { "error": "Student not found" }
    ```

- `DELETE /tests/{test_id}`
  - **Response (Success):**
    ```json
    { "message": "Test deleted successfully" }
    ```
  - **Response (Not Found):**
    ```json
    { "error": "Test not found" }
    ```

- `PUT /tests/{test_id}`
  - **Request Body:**
    ```json
    {
      "listening": 8.0,
      "reading": 8.5,
      "writing": 7.0,
      "speaking": 7.5
    }
    ```
  - **Response (Success):**
    ```json
    {
      "id": 1,
      "student_id": 1,
      "reading_score": 8.5,
      "writing_score": 7.0,
      "listening_score": 8.0,
      "speaking_score": 7.5,
      "total_score": 7.75
    }
    ```
  - **Response (Not Found):**
    ```json
    { "error": "Test not found or could not be updated" }
    ```

## How to Run with Docker Compose

1. **Build and start the containers:**
   ```powershell
   docker-compose up --build -d
   ```
2. **Access the API docs:**
   Open your browser at [http://localhost:8000/docs](http://localhost:8000/docs)

## Requirements
- Docker & Docker Compose
- Or, for local development: Python 3.12+, FastAPI, Uvicorn

## Local Development (without Docker)
1. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
2. Run the app:
   ```powershell
   uvicorn main:app --reload
   ```
3. Visit [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

## Contributing 
Contributions are welcome! Follow these steps to contribute:
* Fork the project.
* Create a new branch: `git checkout -b feature/your-feature`.
* Make your changes.
* Submit a pull request.

### Thanks for your attention! 