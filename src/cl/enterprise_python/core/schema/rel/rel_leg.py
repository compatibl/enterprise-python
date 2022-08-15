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

from sqlalchemy import Column, String
from cl.enterprise_python.core.schema.rel.rel_leg_key import RelLegKey


class RelLeg(RelLegKey):  # Inherits from RelLegKey that has primary key attributes
    """Swap leg."""

    trade_id: str = Column(String)
    """Identifier of trade to which the leg belongs (foreign key)."""

    leg_type: str = Column(String)
    """Leg type."""

    leg_ccy: str = Column(String)
    """Leg currency."""
