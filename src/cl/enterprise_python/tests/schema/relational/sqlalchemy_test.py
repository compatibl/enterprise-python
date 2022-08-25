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


class SqlAlchemyTest:
    """
    Tests for SqlAlchemy API.
    """

    _db_file_name: str = "sqlalchemy_test.db"

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

    def test_crud(self):
        """Test CRUD operations."""

        # Connect and set connection parameters
        engine = self.connect()

        # Drop database in case it is left over from the previous test
        self.clean_up()

        # Temporary - sqlalchemy example
        class Parent(RelationalBase):
            __tablename__ = "parent"
            id = sa.Column(sa.String, primary_key=True)
            children = sa.orm.relationship("Child", back_populates="parent")

        class Child(RelationalBase):
            __tablename__ = "child"
            id = sa.Column(sa.String, primary_key=True)
            parent_id = sa.Column(sa.String, sa.ForeignKey("parent.id"))
            parent = sa.orm.relationship("Parent", back_populates="children")

        c1 = Child()
        c1.id = "c1"
        c2 = Child()
        c2.id = "c2"

        p = Parent()
        p.id = "A"
        p.children = [c1, c2]

        with engine.connect() as connection:

            # Create schema
            RelationalBase.metadata.create_all(engine)

            with Session(engine) as session:

                # Write the trade and leg records and commit
                session.add(p)
                session.commit()

        # Drop database to clean up after the test
        # self.clean_up()


if __name__ == "__main__":
    pytest.main([__file__])
