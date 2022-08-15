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
import sqlalchemy as sa
from sqlalchemy.orm import Session
from cl.enterprise_python.mocks.storage.sqlalchemy.sa_simple_record_mock import SaSimpleRecordMock


class SaSimpleRecordTest:
    """
    Tests for working with SimpleRecord using SqlAlchemy.
    """

    def test_write(self):
        """Test writing."""

        from sqlalchemy import create_engine
        engine = create_engine("sqlite://", echo=True, future=True)

        connection = engine.connect()
        metadata = sa.MetaData()
        table = sa.Table('simple_record_mock', metadata,
                         sa.Column('simple_id', sa.Integer()),
                         sa.Column('string_element', sa.String(255), nullable=False),
                         )
        metadata.create_all(engine)  # Creates the table

        with Session(engine) as session:
            obj_1 = SaSimpleRecordMock(simple_id="A", string_element="AA")
            session.add_all([obj_1])
            session.commit()


if __name__ == "__main__":
    pytest.main([__file__])
