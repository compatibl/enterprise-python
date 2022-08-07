# Copyright (C) 2003-present CompatibL. All rights reserved.
#
# This file contains valuable trade secrets and may be copied, stored, used,
# or distributed only in compliance with the terms of a written commercial
# license from CompatibL and with the inclusion of this copyright notice.

import pytest
from approvaltests import verify

from cl.enterprise_python.core.classes.slots_class import SlotsClass


class SlotsClassTest:
    """
    Tests for SlotsClass.
    """

    def test_attribute_name(self):
        """Test the effect of a typo in attribute name."""

        # Assign value of attribute with typo in name
        obj = SlotsClass()

        # Attribute name has a typo here, and this assignment
        # will throw an exception for AttrsClass
        with pytest.raises(AttributeError):
            obj.instance_attirbute = 2

    def test_repr(self):
        """Test how the instance will appear in the debugger."""

        obj = SlotsClass()
        obj.instance_attribute = 1
        obj.list_attribute = [2, 3]
        obj_repr = repr(obj)
        verify(obj_repr)

    def test_list_attribute_initialization(self):
        """Test list initialization."""

        # Create the first class instance and append
        # an element to the list attribute
        obj_1 = SlotsClass()
        obj_1.list_attribute.append(1)

        # Create the second class instance that should have
        # an empty list attribute.
        obj_2 = SlotsClass()

        # Check that the list attribute in second
        # class instance has zero size
        assert len(obj_2.list_attribute) == 0

    def test_equality(self):
        """Test for the built-in equality operator."""

        # One expects these two instances to be equal,
        # but with SlotsClass they are not
        with pytest.raises(AssertionError):
            assert SlotsClass() == SlotsClass()


if __name__ == "__main__":
    pytest.main([__file__])
