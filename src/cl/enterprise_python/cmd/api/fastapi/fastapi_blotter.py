# Copyright (C) 2021-present CompatibL
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Union

import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def get_root():
    return "Welcome to FastAPI Trade Blotter!"


@app.get("/trades")
def read_item():
    return {"trade_id": "T1"}


@app.get("/example_raising_exception")
def example_raising_exception():
    raise HTTPException(status_code=418, detail="Exception raised in FastAPI.")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=50301)
