from fastapi import FastAPI
from app.routers import tasks, Users, auth
from starlette.middleware.cors import CORSMiddleware
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",  # React's development server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(tasks.router)
app.include_router(Users.router)
app.include_router(auth.router)
@app.get("/")
async def root():
    # dict_of_todos = {"name": "first", "second": "second"}
    return {"members": "text"}


@app.get("/hello")
async def say_hello():
    dict_of_todos = {"name": "first", "second": "second"}
    return {"message": ["Hello it it tit it it", "member, member2"]}
