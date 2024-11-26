from fastapi import FastAPI, APIRouter, HTTPException
from configurations import collection

from database.models import User
from database.schemas import all_users

app = FastAPI()

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



app.include_router(router)
