from typing import Union

import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/example_raising_exception")
def example_raising_exception():
    raise HTTPException(status_code=418, detail="Exception raised in FastAPI.")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
