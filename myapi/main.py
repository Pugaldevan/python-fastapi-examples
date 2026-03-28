import asyncio
import json
from urllib import response
from fastapi import FastAPI, Body, Form, UploadFile, File
import httpx
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import time
import http

app = FastAPI()

API_Key = "123456789abcdef"  # Example API key, replace with your actual key


@app.middleware("http")
async def api_key_middleware(request, call_next):
    api_key = request.headers.get("X-API-Key")
    if api_key != API_Key:
        return JSONResponse(status_code=401, content={"message": "Unauthorized"})
    response = await call_next(request)
    return response


@app.get("/user")
def read_user():
    return {"user": "John Doe"}


@app.get("/user/{user_id}")
def get_list_user(user_id: int):
    return {"user_id": user_id, "name": "John Doe: " + str(user_id)}

# Post method with JSON body


class User(BaseModel):
    name: str
    age: int
    address: str


users = []


@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {f'user {user.name} created successfully': len(users)}

# Post method with plain text body


@app.post("/text")
def create_text(content: str = Body(..., media_type="text/plain")):
    return {"type:": "plaintext", "text": content}

# post method with form data


@app.post("/form")
def create_form(username: str = Form(...), password: str = Form(...)):
    return {"type:": "form", "username": username, "password": password}

# post method with file upload


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename, "content_type": file.content_type, "size": len(await file.read())}

# post method with upload file


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    return {"filename": file.filename, "content_type": file.content_type, "size": len(content)}


# sample sync function


@app.get("/sync")
def sync_function(user_id: int):
    start = time.time()
    todos = []
    with httpx.Client() as client:
        for i in range(5):
            response = client.get(JSON_URL)
            data = response.json()
            todos.append(f'Fetched {len(data)} todos in iteration {i+1}')
    end = time.time()
    return {"message": "This is a synchronous function", "user_id": user_id, "time_taken": end - start, "todos": todos}


# Example response for sync function
'''
{
    "message": "This is a synchronous function",
    "user_id": 1,
    "time_taken": 1.23915696144104,
    "todos": [
        "Fetched 200 todos in iteration 1",
        "Fetched 200 todos in iteration 2",
        "Fetched 200 todos in iteration 3",
        "Fetched 200 todos in iteration 4",
        "Fetched 200 todos in iteration 5"
    ]
}
'''

# sample async function


@app.get("/async")
async def async_function(user_id: int):
    start = time.time()
    todos = []
    # await asyncio.sleep(5)  # Simulate a long-running task
    async with httpx.AsyncClient() as client:
        # Create multiple tasks to fetch data concurrently
        tasks = [client.get(JSON_URL) for _ in range(5)]
        responses = await asyncio.gather(*tasks)

        for response in responses:
            data = response.json()
            todos.append(f'Fetched {len(data)} todos')
    end = time.time()
    return {"message": "This is an asynchronous function", "user_id": user_id, "time_taken": end - start}

# sample response for async function
'''
{
    "message": "This is an asynchronous function",
    "user_id": 1,
    "time_taken": 0.5316329002380371
}
'''

# Example JSON URL for testing
JSON_URL = "https://jsonplaceholder.typicode.com/todos"
