from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_fastapi():
    return {"message": "API FastAPI opérationnelle"}


@app.get(
    "/users",
    response_model=list,
    summary="Récupérer la liste des utilisateurs",
    description="Retourne une liste d'utilisateurs au format JSON",
    responses={
        200: {
            "description": "Liste des utilisateurs récupérées avec succès",
            "content": {
                "application/json": {
                    "example": [{"name": "Jami"}, {"name": "benoit"}]
                }
            }
        }
    }
)
def get_users():
    users = [
        {"id": 1, "name" : "alice"},
        {"id": 2, "name" : "bob"},
        {"id": 3, "name" :  "charlie"},
        {"id": 4, "name" :  "diana"},
        {"id": 5, "name" :  "edward"},
        {"id": 6, "name" :  "fatima"},
        {"id": 7, "name" :  "guillaume"},
        {"id": 8, "name" :  "hana"},
        {"id": 9, "name" :  "ismael"},
        {"id": 10, "name" : "julien"}
    ]

    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}


@app.get("/search")
def search(name: str = None):
    return {"search": name}
