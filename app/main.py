#uvicorn app.main:app --host localhost --port 3000
from fastapi import FastAPI
from Models.user import User

app = FastAPI(
    title = "TryToBack"
)

# Тестовый декаратор
@app.get("/")
def index():
    return{"message": "Hello world!"}

# Получение пользователя
@app.get("/users/{id}", response_model=User)
def get_user(user_id: int):
    return user_id

# Изменение имени пользователя
@app.post("users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    #current_user организовать поиск пользователя по id
    return {"status": 200} #success

@app.post("/registration")
def register_user(user: User):
    return {"status": 200}