from fastapi import FastAPI, Body

app = FastAPI()
data = []
user = []


@app.get("/")
async def get():
    return {"msg": "Hello!"}


@app.get("/greeting/{name}/{major}")
async def get_with_path(name: str, major: str):
    return {"msg": f"Hello, my name is {name} and I major in {major}"}


@app.get("/greeting/")
async def get_with_query(name: str, age: str):
    return {"msg": f"Hello, I am {name}, who is {age} years old."}


@app.get("/greeting/{name}")
async def get_with_path_and_query(name: str, major: str = "CS", age: int = 30):
    return {"msg": f"Hello, my name is {name}, I am {age} years old and major in {major}."}


@app.post("/create_user")
async def post(new_user=Body()):
    user.append(new_user)
    print(user)
    return {"msg": "This is a POST API.", "new_user": new_user}


@app.put("/put/")
async def put(name: str, age: int):
    data.append([name, age])
    print(data)
    return {"msg": f"Age with name {name} has been created."}


@app.delete("/delete/")
async def delete(name: str):
    for i in range(len(data)):
        if data[i][0] == name:
            data.pop(i)
            return {"msg": f"{name} has been deleted."}

    return {"msg": f"{name} not found!"}
