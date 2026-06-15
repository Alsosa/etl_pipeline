from fastapi import APIRouter
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

USERS_PATH = os.path.join(BASE_DIR, "data/users.json")
POSTS_PATH = os.path.join(BASE_DIR, "data/posts.json")

router = APIRouter()

with open(USERS_PATH, "r", encoding="utf-8") as f:
    users = json.load(f)

with open(POSTS_PATH, "r", encoding="utf-8") as f:
    posts = json.load(f)

@router.get("/users")
def get_users():
    return users

@router.get("/posts")
def get_posts():
    return posts