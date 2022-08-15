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


class UnsafeClassTest:
    """
    Tests for UnsafeClass.
    """

    def test_attribute_name(self):
        """Test the effect of a typo in attribute name."""

        # Assign value of attribute with typo in name
        obj = ep.UnsafeClass()

        # Attribute name has a typo here
        obj.int_attirbute = 2

        # But not here, so it has the old value
        assert obj.int_attribute == 1

        # And there is now a second, unwanted attribute with typo in name
        assert obj.int_attirbute == 2

    def test_repr(self):
        """Test how the instance will appear in the debugger."""

        obj = ep.UnsafeClass()
        obj.int_attribute = 1
        obj.list_attribute = [2, 3]
        obj_repr = repr(obj)
        assert obj_repr.startswith(
            "<cl.enterprise_python.core.classes.unsafe_class.UnsafeClass object at"
        )

    def test_list_attribute_initialization(self):
        """Test list initialization."""

        # Create the first class instance and append
        # an element to the list attribute
        obj_1 = ep.UnsafeClass()
        obj_1.list_attribute.append(1)

        # Create the second class instance that should have
        # an empty list attribute.
        obj_2 = ep.UnsafeClass()

        # Check that the list attribute in second
        # class instance has zero size
        assert len(obj_2.list_attribute) == 0

    def test_equality(self):
        """Test for the built-in equality operator."""

        # One expects these two instances to be equal,
        # but with ep.UnsafeClass they are not
        assert ep.UnsafeClass() != ep.UnsafeClass()


if __name__ == "__main__":
    pytest.main([__file__])
