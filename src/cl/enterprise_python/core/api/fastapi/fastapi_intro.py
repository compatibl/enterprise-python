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

from typing import Union, Optional

import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def get_root():
    return "Welcome to FastAPI!"


@app.get("/with_path_params/{path_param_1}/{path_param_2}")
def get_trades(path_param_1: str, path_param_2: str):
    return {"path_param_1": path_param_1, "path_param_2": path_param_2}


@app.get("/with_get_params")
def get_trades(get_param_1: str, get_param_2: str):
    return {"get_param_1": get_param_1, "get_param_2": get_param_2}


@app.get("/with_optional_params")
def get_trades(required_str: str, optional_int: Optional[int] = None):
    return {"required_str": required_str, "optional_int": optional_int}


@app.get("/example_raising_exception")
def example_raising_exception():
    raise HTTPException(status_code=418, detail="Exception raised in FastAPI.")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=50300)
