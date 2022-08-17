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

import mongoengine as me
from typing import List
import uvicorn
from fastapi import FastAPI, HTTPException
from cl.enterprise_python.core.schema.tree.tree_leg import TreeLeg
from cl.enterprise_python.core.schema.tree.tree_swap import TreeSwap
from cl.enterprise_python.core.schema.tree.tree_trade import TreeTrade

app = FastAPI()


def create_trades(trade_count: int) -> List[TreeTrade]:
    """
    Create the specified number of random swap records.
    """

    # Create a list of currencies to populate swap records
    ccy_list = ["USD", "EUR", "GBP", "JPY", "NOK", "AUD", "CAD"]
    ccy_count = len(ccy_list)

    # Create swap records
    swaps = [
        TreeSwap(
            trade_id=f"T{i + 1}",
            trade_type="Swap",
            legs=[
                TreeLeg(leg_type="Fixed", leg_ccy=ccy_list[i % ccy_count]),
                TreeLeg(leg_type="Floating", leg_ccy=ccy_list[(2*i) % ccy_count]),
            ]
        )
        for i in range(trade_count)
    ]
    return swaps


@app.get("/")
def get_root():
    """This result is returned when you access the main URL."""
    return "Welcome to FastAPI Trade Blotter!"


@app.get("/add_trades/{trade_count}")
def add_trades(trade_count: int):
    """
    Create and add to DB the specified number of random swap records.
    """

    # Use connection alias specified in 'meta' attribute of the data types for the test
    connection_alias = "tree"

    # Connect to the database using test-specific alias
    connection = me.connect(connection_alias, alias=connection_alias)

    # Create records and insert them into the database
    records = create_trades(trade_count)
    TreeTrade.objects.insert(records)

    return f"Success: Added {trade_count} trades."


@app.get("/clear")
def clear_trades():
    """Clear all trades."""
    return "Done"


@app.get("/book_trades")
def read_item():
    trades = create_records()
    result = {"trades": [trade.to_json() for trade in trades]}
    return result


@app.get("/example_raising_exception")
def example_raising_exception():
    raise HTTPException(status_code=418, detail="Exception raised in FastAPI.")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=50301)
