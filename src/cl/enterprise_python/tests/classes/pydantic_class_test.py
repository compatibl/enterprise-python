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
import cl.enterprise_python.core as ep
from approvaltests import verify


class PydanticClassTest:
    """
    Tests for PydanticClass.
    """

    def test_attribute_name(self):
        """Test the effect of a typo in attribute name."""

        # Assign value of attribute with typo in name
        obj = ep.PydanticClass()

        # Attribute name has a typo here, and this assignment
        # will throw an exception for PydanticClass
        with pytest.raises(ValueError):
            obj.int_attirbute = 2

    def test_equality(self):
        """Test for the built-in equality operator."""

        # One expects these two instances to be equal, and they are
        # without having to manually override the equality operator
        assert ep.PydanticClass() == ep.PydanticClass()

    def test_repr(self):
        """Test how the instance will appear in the debugger."""

        obj = ep.PydanticClass()
        obj.int_attribute = 1
        obj.list_attribute = [2, 3]
        obj_repr = repr(obj)
        verify(obj_repr)

    def test_list_attribute_initialization(self):
        """
        Test the effect of initializing a mutable object
        directly instead of using Factory(type).
        """

        # Create the first class instance and append an element
        # to list_attribute.
        obj_1 = ep.PydanticClass()
        obj_1.list_attribute.append(1)

        # Create the second class instance that should have
        # empty list_attribute, and it does
        obj_2 = ep.PydanticClass()
        assert len(obj_2.list_attribute) == 0


if __name__ == "__main__":
    pytest.main([__file__])
