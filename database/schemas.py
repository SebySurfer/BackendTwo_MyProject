
# This works to get the necessary data that we want to use, doesn't have to be all the details
# Its where you organize and highlight how should the data be organized
def individual_User(user):
    return{
        "id": str(user["_id"]),
        "firstName": str(user["firstName"]),
        "lastName": str(user["lastName"]),
    }

def all_users(users):
    return [individual_User(user) for user in users]