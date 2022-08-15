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
from typing import List, Any
from cl.enterprise_python.core.schema.deep.deep_leg import DeepLeg
from cl.enterprise_python.core.schema.deep.deep_swap import DeepSwap


class DeepSwapTest:
    """
    Tests for DeepSwap using MongoEngine ODM and deep style of embedding.
    """

    def connect(self) -> Any:
        """
        Connect and return connection object.

        MongoEngine provides no explicit type for
        the connection so Any is used in annotation.
        """
        # Connect to the database using class name for the table
        return me.connect(__name__)

    def clean_up(self, connection: Any) -> None:
        """Drop database to clean up before and after the test."""
        connection.drop_database(__name__)

    def create_records(self) -> List[DeepSwap]:
        """
        Return a list of random records objects.
        This method does not write to the database.
        """

        # Create a list of currencies to populate swap records
        ccy_list = ["USD", "GBP", "JPY", "NOK", "AUD"]
        ccy_count = len(ccy_list)

        # Create swap records
        records = [
            DeepSwap(
                trade_id=f"T{i}",
                trade_type="Swap",
                legs=[
                    DeepLeg(leg_type="Fixed", leg_ccy=ccy_list[i % ccy_count]),
                    DeepLeg(leg_type="Floating", leg_ccy="EUR")
                ]
            )
            for i in range(5)
        ]
        return records

    def test_crud(self):
        """Test CRUD operations."""

        # Connect and set connection parameters
        connection = self.connect()

        # Drop database in case it is left over from the previous test
        self.clean_up(connection)

        ccy_list = ["USD", "GBP", "JPY", "NOK", "AUD"]
        ccy_count = len(ccy_list)

        # Create swap records
        records = self.create_records()

        # TODO - use bulk insert
        for record in records:
            record.save()

        # Retrieve all records
        print()
        for swap in DeepSwap.objects:
            print(swap.trade_id)

        # Drop database to clean up after the test
        self.clean_up(connection)


if __name__ == "__main__":
    pytest.main([__file__])
