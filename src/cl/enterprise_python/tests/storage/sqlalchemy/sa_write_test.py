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
from cl.enterprise_python.mocks.storage.sqlalchemy.sa_simple_record_mock import (
    SaSimpleRecordMock,
)


class SaSimpleRecordTest:
    """
    Tests for working with SimpleRecord using SqlAlchemy.
    """

    def test_write(self):
        """Test writing."""

        file_name_db = "sa_write_test.db"

        # Remove DB file before test, in case it was left over from previous run
        if os.path.exists(file_name_db):
            os.remove(file_name_db)

        engine = sa.create_engine(f"sqlite:///{file_name_db}", echo=True, future=True)

        with engine.connect() as connection:

            metadata = sa.MetaData()
            table = sa.Table(
                "simple_record_mock",
                metadata,
                sa.Column(
                    "simple_id", sa.String(255), nullable=False, primary_key=True
                ),
                sa.Column("string_element", sa.String(255), nullable=False),
            )
            metadata.create_all(engine)  # Creates the table

            with Session(engine) as session:

                # Create records
                a_aa = SaSimpleRecordMock(simple_id="A", string_element="AA")
                b_bb = SaSimpleRecordMock(simple_id="B", string_element="BB")

                # Write the records and commit
                session.add_all([a_aa, b_bb])
                session.commit()

            with pytest.raises(sa.exc.IntegrityError):  # noqa
                with Session(engine) as session:

                    # Update one of the object by writing another object with the same primary key
                    a_bb = SaSimpleRecordMock(simple_id="A", string_element="BB")
                    session.add_all([a_bb])
                    session.commit()

        # Remove DB file after test
        if os.path.exists(file_name_db):
            os.remove(file_name_db)


if __name__ == "__main__":
    pytest.main([__file__])
