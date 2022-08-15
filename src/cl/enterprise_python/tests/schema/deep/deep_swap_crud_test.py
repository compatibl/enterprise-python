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

from cl.enterprise_python.core.schema.deep.deep_leg import DeepLeg
from cl.enterprise_python.core.schema.deep.deep_swap import DeepSwap
from cl.enterprise_python.core.schema.deep.deep_swap_key import DeepSwapKey


class DeepTest:
    """
    Tests for DeepSwap using MongoEngine ODM and deep style of embedding.
    """

    def test_write(self):
        """Test writing."""

        # Connect to the database
        db_name = "deep_test_write"
        me.connect(db_name)

        # Create swap record
        rec = DeepSwap(
            trade_id="T1",
            trade_type="Swap",
            legs=[
                DeepLeg(leg_type="Fixed", leg_ccy="USD"),
                DeepLeg(leg_type="Floating", leg_ccy="EUR")
            ]
        )
        rec.save()


if __name__ == "__main__":
    pytest.main([__file__])
