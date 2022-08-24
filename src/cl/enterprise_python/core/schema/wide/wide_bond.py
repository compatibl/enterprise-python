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
from cl.enterprise_python.core.schema.wide.wide_trade import WideTrade


class WideBond(WideTrade):
    """
    Remaining attributes of bond record.

    Inherits from WideTrade that has attributes common to all trades.
    """

    bond_ccy = me.StringField(max_length=3)
    """Bond currency."""
