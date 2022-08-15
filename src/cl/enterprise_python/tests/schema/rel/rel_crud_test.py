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
from typing import List, Any, Tuple

from cl.enterprise_python.core.schema.rel.rel_bond import RelBond
from cl.enterprise_python.core.schema.rel.rel_leg import RelLeg
from cl.enterprise_python.core.schema.rel.rel_swap import RelSwap
from cl.enterprise_python.core.schema.rel.rel_trade import RelTrade


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
        return sa.create_engine(f"sqlite:///{self._db_file_name}", echo=True, future=True)

    def clean_up(self) -> None:
        """Delete database file to clean up before and after the test."""
        # Remove DB file after test
        if os.path.exists(self._db_file_name):
            os.remove(self._db_file_name)

    def create_records(self) -> Tuple[List[RelTrade], List[RelLeg]]:
        """
        Return a list of random records objects.
        This method does not write to the database.
        """

        # Create a list of currencies to populate swap records
        ccy_list = ["USD", "GBP", "JPY", "NOK", "AUD"]
        ccy_count = len(ccy_list)

        # Create swap records
        swaps = [
            RelSwap(
                trade_id=f"T{i+1}",
                trade_type="Swap"
            )
            for i in range(0, 2)
        ]
        bonds = [
            RelBond(
                trade_id=f"T{i+ 1}",
                trade_type="Bond",
                bond_ccy=ccy_list[i % ccy_count]
            )
            for i in range(2, 3)
        ]

        fixed_legs = [
            RelLeg(leg_id=f"L{i+1}1", trade_id=f"T{i+1}", leg_type="Fixed", leg_ccy=ccy_list[i % ccy_count])
            for i in range(0, 2)
        ]

        floating_legs = [
            RelLeg(leg_id=f"L{i+1}2",trade_id=f"T{i+ 1}", leg_type="Floating", leg_ccy="EUR")
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

            metadata = sa.MetaData()
            trade_table = sa.Table('rel_trade', metadata,
                             sa.Column('trade_id', sa.String(255), nullable=False, primary_key=True),
                             sa.Column('trade_type', sa.String(255), nullable=False),
                             sa.Column('bond_ccy', sa.String(255), nullable=True),
                             )
            leg_table = sa.Table('rel_leg', metadata,
                                   sa.Column('leg_id', sa.String(255), nullable=False, primary_key=True),
                                   sa.Column('trade_id', sa.String(255), nullable=False,
                                             foreign_key=sa.ForeignKey("rel_trade.trade_id")),
                                   sa.Column('leg_type', sa.String(255), nullable=True),
                                   sa.Column('leg_ccy', sa.String(255), nullable=True),
                                   )
            metadata.create_all(engine)  # Creates the table

            with Session(engine) as session:

                # Write the trade and leg records and commit
                session.add_all(trades)
                session.add_all(legs)
                session.commit()

                # Use join to query legs that belong to a trade
                result = session.query(RelTrade).join(RelLeg).filter(Invoice.amount == 8500)
                for row in result:
                    for inv in row.invoices:
                        print(row.id, row.name, inv.invno, inv.amount)


        # Drop database to clean up after the test
        # self.clean_up()


if __name__ == "__main__":
    pytest.main([__file__])
