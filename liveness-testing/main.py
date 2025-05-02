from fastapi import FastAPI, HTTPException
from random import randrange

app = FastAPI()
# Another line Add a comment, add more comment


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/healthcheck")
def healthcheck():
    """
    Healthcheck that has a 1/10 chance to fail
    """
    randomNumber = randrange(1,11) 
    if randomNumber == 1: # Fail
        raise HTTPException(status_code=500, detail="Not healthy")
    else:
        return {"Healthcheck": f"Random: {randomNumber}"}
