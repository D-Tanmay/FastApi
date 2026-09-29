from fastapi import FastAPI
app = FastAPI()

#Home route
@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

#About route
@app.get("/about")
def about():
    return {"message": "This is the about page of the FastAPI application."}

#usr route
@app.get("/usr")
def usr():
    return {"message": "This is the user page of the FastAPI application."}