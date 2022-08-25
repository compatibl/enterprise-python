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
import os
import sqlalchemy as sa
from sqlalchemy.orm import Session
from typing import List, Any
import approvaltests as at
from cl.enterprise_python.core.schema.relational.relational_base import RelationalBase
from cl.enterprise_python.core.schema.relational.relational_bond import RelationalBond
from cl.enterprise_python.core.schema.relational.relational_leg import RelationalLeg
from cl.enterprise_python.core.schema.relational.relational_swap import RelationalSwap
from cl.enterprise_python.core.schema.relational.relational_trade import RelationalTrade


class RelCrudTest:
    """
    Tests for RelSwap using MongoEngine ODM and rel style of embedding.
    """

    _db_file_name: str = "rel_crud_test.db"

    def connect(self) -> Any:
        """
        Connect and return engine object.
        """
        # Connect to the database
        return sa.create_engine(
            f"sqlite:///{self._db_file_name}", echo=True, future=True
        )

    def clean_up(self) -> None:
        """Delete database file to clean up before and after the test."""
        # Remove DB file after test
        if os.path.exists(self._db_file_name):
            os.remove(self._db_file_name)

    def create_records(self) -> List[RelationalTrade]:
        """
        Return a list of random records objects.
        This method does not write to the database.
        """

        # Create a list of currencies to populate swap records
        ccy_list = ["USD", "GBP", "JPY", "NOK", "AUD"]
        ccy_count = len(ccy_list)

        fixed_legs = [
            RelationalLeg(
                leg_id=f"L{i + 1}1",
                trade_id=f"T{i + 1}",
                leg_type="Fixed",
                leg_ccy=ccy_list[i % ccy_count],
            )
            for i in range(0, 2)
        ]

        floating_legs = [
            RelationalLeg(
                leg_id=f"L{i + 1}2",
                trade_id=f"T{i + 1}",
                leg_type="Floating",
                leg_ccy="EUR",
            )
            for i in range(0, 2)
        ]

        # Create swap records using legs
        swaps: List[RelationalTrade] = [
            RelationalSwap(
                trade_id=f"T{i + 1}",
                trade_type="Swap",
                legs=[fixed_legs[i], floating_legs[i]],
            )
            for i in range(0, 2)
        ]

        # Create bond records
        bonds: List[RelationalTrade] = [
            RelationalBond(
                trade_id=f"T{i + 1}",
                trade_type="Bond",
                bond_ccy=ccy_list[i % ccy_count],
            )
            for i in range(2, 3)
        ]

        return swaps + bonds

    def test_crud(self):
        """Test CRUD operations."""

        # Connect and set connection parameters
        engine = self.connect()

        # Drop database in case it is left over from the previous test
        self.clean_up()

        # Set up result string
        result = ""

        # Create swap records
        trades = self.create_records()

        with engine.connect() as connection:

            # Create schema
            RelationalBase.metadata.create_all(engine)

            with Session(engine) as session:

                # Write the trade and leg records and commit
                session.add_all(trades)
                session.commit()

                # Retrieve all trades
                # Must use noqa because PyCharm linter thinks does not return anything
                all_trades = list(
                    session.query(RelationalTrade).order_by(RelationalTrade.trade_id)
                )  # noqa

                # Add the result to approvaltests file
                result += "All Trades:\n" + "".join(
                    [
                        f"    trade_id={trade.trade_id} trade_type={trade.trade_type}\n"
                        for trade in all_trades
                    ]
                )

                # Retrieve all swaps but skip bonds, use trade_type instead of
                # class name to avoid creating even more complex ORM mapping
                # Must use noqa because PyCharm linter thinks does not return anything
                all_swaps = list(
                    session.query(RelationalSwap)
                    .where(RelationalSwap.trade_type == "Swap")
                    .order_by(RelationalSwap.trade_id)
                )  # noqa

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

                # This Iterable includes trades where a leg has type=Fixed and ccy=GBP
                #  For the purposes of this exercise, we will assume that each swap has
                #  one Fixed leg and one Floating leg (most of the swaps traded in the
                #  market are like that), so we do not need to eliminate duplicates.
                gbp_fixed_swaps = list(
                    session.query(RelationalSwap)
                    .join(RelationalLeg)
                    .where(
                        sa.and_(
                            RelationalSwap.trade_type == "Swap",
                            RelationalLeg.leg_ccy == "GBP",
                            RelationalLeg.leg_type == "Fixed",
                        )
                    )
                    .order_by(RelationalSwap.trade_id)
                )  # noqa

                # Add the result to approvaltests file
                result += "Swaps where fixed leg has GBP currency:\n" + "".join(
                    [
                        f"    trade_id={trade.trade_id} trade_type={trade.trade_type} "
                        f"leg_type[0]={trade.legs[0].leg_type} leg_ccy[0]={trade.legs[0].leg_ccy} "
                        f"leg_type[1]={trade.legs[1].leg_type} leg_ccy[1]={trade.legs[1].leg_ccy}\n"
                        for trade in gbp_fixed_swaps
                    ]
                )

        # Verify result
        at.verify(result)

        # Drop database to clean up after the test
        self.clean_up()


if __name__ == "__main__":
    pytest.main([__file__])
