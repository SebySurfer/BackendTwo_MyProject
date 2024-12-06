from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from configurations import collection
from bson.objectid import ObjectId

from database.models import User
from database.schemas import all_users, individual_User
from database.models import QuestionsUpdate

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


@router.get("/{user_id}")
async def get_user(user_id: str):
    try:
        id = ObjectId(user_id)
        user = collection.find_one({"_id": id})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return individual_User(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occurred: {e}")


@router.post("/")
async def create_user(new_user: User):
    try:
        resp = collection.insert_one(dict(new_user))
        return {"status_code": 200, "id": str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error ocurred {e}")


@router.put("/{user_id}")
async def update_user(user_id: str, update_data: QuestionsUpdate):
    try:
        id = ObjectId(user_id)
        existing_doc = collection.find_one({"_id": id})
        if not existing_doc:
            raise HTTPException(status_code=404, detail="User does not exist")

        # Debug log for incoming data
        print(f"Data received for update: {update_data.questions}")

        # Update the database
        resp = collection.update_one({"_id": id}, {"$set": {"questions": update_data.questions}})
        if resp.modified_count == 0:
            print(f"No documents modified for user_id {user_id}")
            raise HTTPException(status_code=500, detail="Failed to update user questions")

        return {"status_code": 200, "message": "Questions updated successfully"}
    except Exception as e:
        print(f"Error during update: {e}")
        raise HTTPException(status_code=500, detail=f"Some error occurred: {e}")



@router.delete("/{user_id}")
async def delete_user(user_id: str):
    try:
        id = ObjectId(user_id)
        existing_doc = collection.find_one({"_id": id})
        if not existing_doc:
            raise HTTPException(status_code=404, detail="User does not exist")
        collection.delete_one({"_id": id})
        return {"status_code": 200, "message": "User deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occurred: {e}")


app.include_router(router)
