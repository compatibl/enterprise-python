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
from cl.enterprise_python.core.schema.deep.deep_leg import DeepLeg
from cl.enterprise_python.core.schema.deep.deep_trade import DeepTrade


class DeepSwap(DeepTrade):  # Inherits from DeepTrade that has attributes common to all trades
    """Remaining attributes of swap record."""

    legs = me.ListField(me.EmbeddedDocumentField(DeepLeg))
    """List of swap legs."""
