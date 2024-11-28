from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from configurations import collection
from bson.objectid import ObjectId

from database.models import User
from database.schemas import all_users

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific origins for better security in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()



#Api to fetch everything
@router.get("/")
async def get_all_users():
    data = collection.find() #If you pass a blank, it fetches anything, and if not, it will pass through that filter/criteria
    return all_users(data)

@router.post("/")
async def create_user(new_user: User):
    try:
        resp = collection.insert_one(dict(new_user))
        return {"status_code": 200, "id": str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error ocurred {e}")

@router.put("/{user_id}")
async def update_user(user_id: str, update_User: User):
    try:
        id = ObjectId(user_id)
        existing_doc = collection.find_one({"_id": id})
        if not existing_doc:
            return HTTPException(status_code=500, detail=f"User does not exist")
        resp = collection.update_one({"_id":id}, {"$set": dict(update_User)})
        return {"status_code":200, "message":"Task updated successfully"}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error ocurred {e}")


@router.delete("/{user_id")
async def delete_user(user_id: str):
    try:
        id = ObjectId(user_id)
        existing_doc = collection.find_one({"_id": id})
        if not existing_doc:
            return HTTPException(status_code=500, detail=f"User does not exist")
        resp = collection.delete_one({"_id": id})
        return {"status_code": 200, "message": "Task deleted successfully"}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error ocurred {e}")

app.include_router(router)
