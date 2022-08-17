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


import pytest
from _pytest.fixtures import FixtureRequest
import mongoengine as me
import approvaltests as at
from typing import List, Any, Tuple

from pymongo import MongoClient

from cl.enterprise_python.core.schema.wide.wide_bond import WideBond
from cl.enterprise_python.core.schema.wide.wide_swap import WideSwap
from cl.enterprise_python.core.schema.wide.wide_trade import WideTrade


class WideCrudTest:
    """
    Tests for WideSwap using MongoEngine ODM and deep style of embedding.
    """

    def set_up(self, request: FixtureRequest) -> Tuple[str, MongoClient]:
        """Set up a dedicated database for the test."""

        # Use a unique connection alias per test method
        # to enable multiple simultaneous connections
        # when running multiple tests at the same time
        connection_alias = "wide" # f"{__name__}_{request.node.name}"

        # Connect to the database using test-specific alias
        connection = me.connect(connection_alias, alias=connection_alias)

        # Delete (drop) the existing database if already exists
        # to ensure the test starts from scratch
        self.tear_down(connection_alias, connection)

        return connection_alias, connection

    def tear_down(self, connection_alias: str, connection: MongoClient) -> None:
        """Drop database to clean up after the test."""

        connection.drop_database(connection_alias)

    def create_records(self) -> List[WideTrade]:
        """
        Return a list of random records objects.
        This method does not write to the database.
        """

        # Create a list of currencies to populate swap records
        ccy_list = ["USD", "GBP", "JPY", "NOK", "AUD"]
        ccy_count = len(ccy_list)

        # Create swap records
        swaps = [
            WideSwap(
                trade_id=f"T{i+1}",
                trade_type="Swap",
                leg_type_1="Fixed",
                leg_type_2="Floating",
                leg_ccy_1=ccy_list[i % ccy_count],
                leg_ccy_2="EUR"
            )
            for i in range(0, 2)
        ]
        bonds = [
            WideBond(
                trade_id=f"T{i+1}",
                trade_type="Bond",
                bond_ccy=ccy_list[i % ccy_count]
            )
            for i in range(2, 3)
        ]
        return swaps + bonds

    def test_crud(self, request: FixtureRequest):
        """Test CRUD operations."""

        # Set up a new database for the rest
        connection_alias, connection = self.set_up(request)

        # Set up result string
        result = ""

        # Create records and insert them into the database
        records = self.create_records()
        WideTrade.objects.insert(records)

        # Retrieve all trades ordered by trade_id to avoid
        # receiving records in random order
        trades = WideTrade.objects.order_by('trade_id')
        result += "All Trades:\n" + "".join(
            [f"trade_id={trade.trade_id} trade_type={trade.trade_type}\n" for trade in trades]
        )

        # Verify result
        at.verify(result)

        # Delete (drop) the database after the test
        self.tear_down(connection_alias, connection)


if __name__ == "__main__":
    pytest.main([__file__])
