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
from typing import List


class SlotsClass:
    """
    Class with manual implementation of safe coding practices.

    The implementation is labor-intensive and has a significant
    amount of repetitive code. The name of each attribute has
    to be specified three times for slots, type declaration,
    and specifying that it is an instance attribute. Additional
    code where attribute name must be specified is required for
    equality and representation as string.
    """

    # To improve performance, manually reserve slots for each attribute
    __slots__ = ["int_attribute", "list_attribute"]

    # Specify attribute types here, however they still must be specified
    # inside __init__ in order to become instance attributes
    int_attribute: int
    list_attribute: List[int]

    def __init__(self):
        """Manually created __init__."""

        # Assignment to self makes them instance attributes
        self.int_attribute = 1
        self.list_attribute = []

    def __repr__(self):
        """
        Manually created string representation
        of the class for use in debugger.
        """
        return (
            f"int_attribute={self.int_attribute};list_attribute={self.list_attribute}"
        )
