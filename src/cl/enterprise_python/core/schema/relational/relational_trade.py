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

import sqlalchemy as sa
from cl.enterprise_python.core.schema.relational.relational_trade_key import (
    RelationalTradeKey,
)


class RelationalTrade(RelationalTradeKey):
    """
    Non-primary-key attributes common to all trades.

    Inherits from RelTradeKey that has primary key attributes.
    """

    trade_type: str = sa.Column(sa.String)
    """Trade type."""
