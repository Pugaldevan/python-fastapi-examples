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

- GET `/user` - Sample user
- GET `/user/{user_id}` - User by ID
- POST `/users` - Create user (JSON)
- POST `/text` - Plain text input
- POST `/form` - Form data
- POST `/upload` - File upload
- GET `/sync` - Synchronous operations
- GET `/async` - Asynchronous operations

All endpoints require `X-API-Key: 123456789abcdef` header.
