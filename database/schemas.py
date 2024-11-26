
# This works to get the necessary data that we want to use, doesn't have to be all the details
# Its where you organize and highlight how should the data be organized
def individual_User(users):
    return{
        "id": str(users["_id"]),
        "firstName": str(users["firstName"]),
        "lastName": str(users["lastName"]),
    }
