from fastapi import FastAPI

app = FastAPI(
    title="Test Project"
)


users = [
    {"id": 1, "role": 'student', 'name': "Shohjahon"},
    {"id": 2, "role": 'student', 'name': "Shohjahon"},
    {"id": 3, "role": 'student', 'name': "Shohjahon"}
]


data = [
    {"id": 1, "user_id": 1, 'title': "Step 1: import FastAPI.", "price": 11111},
    {"id": 2, "user_id": 2, 'title': "Step 2: import FastAPI.", "price": 22222},
    {"id": 3, "user_id": 3, 'title': "Step 3: import FastAPI.", "price": 33333},
    {"id": 4, "user_id": 4, 'title': "Step 4: import FastAPI.", "price": 44444},
    {"id": 5, "user_id": 5, 'title': "Step 5: import FastAPI.", "price": 55555},
]


@app.get("/hello/")
def get_hello():
    return "Hello World"


@app.get("/users/{user_id}")
def get_users(user_id: int):
    return [user for user in users if user.get('id') == user_id]


@app.get("/data/")
def get_data(limit: int = 1, offset: int = 0):
    return data[offset:][:limit]


@app.post("/users/{user_id}/")
def change_username(user_id: int, name: str):
    current_user = [user for user in users if user.get('id') == user_id][0]
    current_user['name'] = name
    return {"status": 200, "data": current_user}

