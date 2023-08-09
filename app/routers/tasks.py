from fastapi import APIRouter

router = APIRouter(
    prefix="/tasks",
)

posts = [{"id":"1","name":"aa", "content": "Hello World"},{"id":"2","name":"bb", "content": "Hello World"}]
@router.get("/")
async def get_posts():
    return posts[0]

@router.get("/{id}")
async def get_post(id):
    result = {""}
    for post in posts:
        if post["id"] == id:
            result = post

    return result
