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
import mongoengine as me
from pymongo import MongoClient
import approvaltests as at
from typing import List, Tuple
from cl.enterprise_python.core.schema.wide.wide_bond import WideBond
from cl.enterprise_python.core.schema.wide.wide_swap import WideSwap
from cl.enterprise_python.core.schema.wide.wide_trade import WideTrade


class WideCrudTest:
    """
    Tests for WideSwap using MongoEngine ODM and deep style of embedding.
    """

    def set_up(self) -> Tuple[str, MongoClient]:
        """Set up a dedicated database for the test."""

        # Use connection alias specified in 'meta' attribute of the data types for the test
        connection_alias = "wide"

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
        swaps: List[WideTrade] = [
            WideSwap(
                trade_id=f"T{i+1}",
                trade_type="Swap",
                leg_type_1="Fixed",
                leg_type_2="Floating",
                leg_ccy_1=ccy_list[i % ccy_count],
                leg_ccy_2="EUR",
            )
            for i in range(0, 2)
        ]
        bonds: List[WideTrade] = [
            WideBond(
                trade_id=f"T{i+1}", trade_type="Bond", bond_ccy=ccy_list[i % ccy_count]
            )
            for i in range(2, 3)
        ]

        return swaps + bonds

    def test_crud(self):
        """Test CRUD operations."""

        # Set up a new database for the rest
        connection_alias, connection = self.set_up()

        # Set up result string
        result = str()

        # Create records and insert them into the database
        records = self.create_records()
        WideTrade.objects.insert(records)

        # Retrieve all trades ordered by trade_id to avoid
        # receiving records in random order
        all_trades = WideTrade.objects.order_by("trade_id")

        # Add the result to approvaltests file
        result += "All Trades:\n" + "".join(
            [
                f"    trade_id={trade.trade_id} trade_type={trade.trade_type}\n"
                for trade in all_trades
            ]
        )

        # Retrieve only those trades that have type WideSwap
        all_swaps = WideSwap.objects.order_by("trade_id")

        # Add the result to approvaltests file
        result += "All Swaps:\n" + "".join(
            [
                f"    trade_id={trade.trade_id} trade_type={trade.trade_type}\n"
                for trade in all_swaps
            ]
        )

        # The objective is to retrieve only those trades that have type WideSwap
        # and have GBP currency for the fixed leg. Having GBP currency for the
        # floating leg does not count.

        # This Iterable includes trades where leg 1 has type=Fixed and ccy=GBP
        gbp_fixed_leg_1_swaps = WideSwap.objects(
            leg_type_1="Fixed", leg_ccy_1="GBP"
        ).order_by("trade_id")

        # This Iterable includes trades where leg 2 has type=Fixed and ccy=GBP
        gbp_fixed_leg_2_swaps = WideSwap.objects(
            leg_type_2="Fixed", leg_ccy_2="GBP"
        ).order_by("trade_id")

        # This list combines items in both Iterables. For the purposes of this
        # exercise, we will assume that each swap has one Fixed leg and one
        # Floating leg (most of the swaps traded in the market are like that),
        # so we do not need to eliminate duplicates.
        gbp_fixed = list(gbp_fixed_leg_1_swaps) + list(gbp_fixed_leg_2_swaps)

        # Add the result to approvaltests file
        result += "Swaps where fixed leg has GBP currency:\n" + "".join(
            [
                f"    trade_id={trade.trade_id} trade_type={trade.trade_type} "
                f"leg_type_1={trade.leg_type_1} leg_ccy_1={trade.leg_ccy_1} "
                f"leg_type_2={trade.leg_type_2} leg_ccy_2={trade.leg_ccy_2}\n"
                for trade in gbp_fixed
            ]
        )

        # Verify result
        at.verify(result)

        # Delete (drop) the database after the test
        self.tear_down(connection_alias, connection)


if __name__ == "__main__":
    pytest.main([__file__])
