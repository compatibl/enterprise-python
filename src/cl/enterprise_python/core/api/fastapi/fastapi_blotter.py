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

from typing import Union, List

import uvicorn
from fastapi import FastAPI, HTTPException

from cl.enterprise_python.core.schema.tree.tree_bond import TreeBond
from cl.enterprise_python.core.schema.tree.tree_leg import TreeLeg
from cl.enterprise_python.core.schema.tree.tree_swap import TreeSwap
from cl.enterprise_python.core.schema.tree.tree_trade import TreeTrade

app = FastAPI()


def create_records() -> List[TreeTrade]:
    """
    Return a list of random records objects.
    This method does not write to the database.
    """

    # Create a list of currencies to populate swap records
    ccy_list = ["USD", "GBP", "JPY", "NOK", "AUD"]
    ccy_count = len(ccy_list)

    # Create swap records
    swaps = [
        TreeSwap(
            trade_id=f"T{i + 1}",
            trade_type="Swap",
            legs=[
                TreeLeg(leg_type="Fixed", leg_ccy=ccy_list[i % ccy_count]),
                TreeLeg(leg_type="Floating", leg_ccy="EUR")
            ]
        )
        for i in range(0, 2)
    ]
    bonds = [
        TreeBond(
            trade_id=f"T{i + 1}",
            trade_type="Bond",
            bond_ccy=ccy_list[i % ccy_count]
        )
        for i in range(2, 3)
    ]
    return swaps + bonds


@app.get("/")
def get_root():
    """This result is returned when you access the main URL."""
    return "Welcome to FastAPI Trade Blotter!"


@app.get("/create")
def create_trades():
    """Create sample trades."""
    return "Done"


@app.get("/clear")
def clear_trades():
    """Clear all trades."""
    return "Done"


@app.get("/trades")
def read_item():
    trades = create_records()
    result = {"trades": [trade.to_json() for trade in trades]}
    return result


@app.get("/example_raising_exception")
def example_raising_exception():
    raise HTTPException(status_code=418, detail="Exception raised in FastAPI.")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=50301)
