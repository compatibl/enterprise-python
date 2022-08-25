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
from sqlalchemy.orm import Session, declarative_base
from typing import List, Any, Tuple

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

    def create_records(self) -> Tuple[List[RelationalTrade], List[RelationalLeg]]:
        """
        Return a list of random records objects.
        This method does not write to the database.
        """

        # Create a list of currencies to populate swap records
        ccy_list = ["USD", "GBP", "JPY", "NOK", "AUD"]
        ccy_count = len(ccy_list)

        # Create swap records
        swaps = [
            RelationalSwap(trade_id=f"T{i + 1}", trade_type="Swap") for i in range(0, 2)
        ]
        bonds = [
            RelationalBond(
                trade_id=f"T{i + 1}",
                trade_type="Bond",
                bond_ccy=ccy_list[i % ccy_count],
            )
            for i in range(2, 3)
        ]

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

        return swaps + bonds, fixed_legs + floating_legs

    def test_crud(self):
        """Test CRUD operations."""

        # Connect and set connection parameters
        engine = self.connect()

        # Drop database in case it is left over from the previous test
        self.clean_up()

        # Create swap records
        trades, legs = self.create_records()

        with engine.connect() as connection:

            # Create schema
            RelationalBase.metadata.create_all(engine)

            with Session(engine) as session:

                # Write the trade and leg records and commit
                session.add_all(trades)
                session.add_all(legs)
                session.commit()

        # Drop database to clean up after the test
        # self.clean_up()


if __name__ == "__main__":
    pytest.main([__file__])
