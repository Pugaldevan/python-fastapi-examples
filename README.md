# FastAPI Examples

A comprehensive FastAPI project demonstrating various API endpoints, including synchronous and asynchronous operations, file uploads, form handling, and API key authentication.

## Features

- RESTful API endpoints with GET and POST methods
- Synchronous vs Asynchronous operations comparison
- File upload handling
- Form data processing
- JSON body parsing with Pydantic models
- Plain text body handling
- API key authentication middleware
- Concurrent HTTP requests demonstration

## Installation

1. Install dependencies: `pip install -r requirement.txt`
2. Run the server: `uvicorn myapi.main:app --reload`

## API Endpoints

All endpoints require the API key header: `X-API-Key: 123456789abcdef`

### User Endpoints

- **GET** `/user`
  - Returns a sample user object
  - Example response: `{"user": "John Doe"}`

- **GET** `/user/{user_id}`
  - Returns user information by ID
  - Path parameter: `user_id` (integer)
  - Example: `/user/123`
  - Example response: `{"user_id": 123, "name": "John Doe: 123"}`

### Data Creation Endpoints

- **POST** `/json`
  - Creates a new user with JSON data
  - Request body: `{"name": "string", "age": integer, "address": "string"}`
  - Example request body:
    ```json
    {
      "name": "Alice",
      "age": 30,
      "address": "123 Main St"
    }
    ```
  - Example response: `{"user Alice created successfully": 1}`

- **POST** `/text`
  - Accepts plain text input
  - Content-Type: `text/plain`
  - Example request body: `"Hello, World!"`
  - Example response: `{"type:": "plaintext", "text": "Hello, World!"}`

- **POST** `/form`
  - Accepts form-encoded data
  - Form fields: `username`, `password`
  - Example response: `{"type:": "form", "username": "testuser", "password": "testpass"}`

- **POST** `/upload`
  - Uploads a file
  - Form field: `file` (file upload)
  - Example response: `{"filename": "example.txt", "content_type": "text/plain", "size": 1024}`

### Performance Comparison Endpoints

- **GET** `/sync?user_id=1`
  - Demonstrates synchronous operations
  - Makes 5 sequential HTTP requests to an external API
  - Query parameter: `user_id` (integer)
  - Returns execution time and fetched data
  - Example response:
    ```json
    {
      "message": "This is a synchronous function",
      "user_id": 1,
      "time_taken": 2.5,
      "todos": ["Fetched 200 todos in iteration 1", ...]
    }
    ```

- **GET** `/async?user_id=1`
  - Demonstrates asynchronous operations
  - Makes 5 concurrent HTTP requests to an external API
  - Query parameter: `user_id` (integer)
  - Returns execution time and fetched data
  - Example response:
    ```json
    {
      "message": "This is an asynchronous function",
      "user_id": 1,
      "time_taken": 0.8,
      "todos": ["Fetched 200 todos in iteration 1", ...]
    }
    ```

## Testing with Postman

1. Set the request method and URL
2. Add header: `X-API-Key` = `123456789abcdef`
3. Configure body as needed (JSON, form-data, etc.)
4. Send the request

## Interactive Documentation

When the server is running, visit `http://127.0.0.1:8000/docs` for Swagger UI documentation.

## Dependencies

- fastapi
- uvicorn
- pydantic
- httpx
- python-multipart

## Project Structure

```
myapi/
├── main.py          # Main application with all endpoints
├── __init__.py      # Package initialization
├── pyproject.toml   # Project configuration
├── uv.lock          # Dependency lock file
└── README.md        # This documentation
```

## Learning Objectives

This project demonstrates:

- FastAPI routing and request handling
- Synchronous vs asynchronous programming
- Data validation with Pydantic
- File upload processing
- Form data handling
- API authentication
- Performance benefits of async operations
