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

import mongoengine as me
from cl.enterprise_python.core.schema.wide.wide_trade_key import WideTradeKey


class WideTrade(WideTradeKey):
    """
    Non-primary-key attributes common to all trades.

    Inherits from WideTradeKey that has primary key attributes
    """

    trade_type = me.StringField(max_length=50)
    """Trade type."""
