# Copyright (C) 2003-present CompatibL. All rights reserved.
#
# This file contains valuable trade secrets and may be copied, stored, used,
# or distributed only in compliance with the terms of a written commercial
# license from CompatibL and with the inclusion of this copyright notice.

import pytest
from approvaltests import verify

from cl.enterprise_python.core.classes.attrs_class import AttrsClass


class AttrsClassTest:
    """
    Tests for AttrsClass.
    """

    def test_attribute_name(self):
        """Test the effect of a typo in attribute name."""

        # Assign value of attribute with typo in name
        obj = AttrsClass()

        # Attribute name has a typo here, and this assignment
        # will throw an exception for AttrsClass
        with pytest.raises(AttributeError):
            obj.instance_attirbute = 2

    def test_equality(self):
        """Test for the built-in equality operator."""

        # One expects these two instances to be equal, and they are
        # without having to manually override the equality operator
        assert AttrsClass() == AttrsClass()

    def test_repr(self):
        """Test how the instance will appear in the debugger."""

        obj = AttrsClass()
        obj.instance_attribute = 1
        obj.list_attribute = [2, 3]
        obj_repr = repr(obj)
        verify(obj_repr)

    def test_list_attribute_initialization(self):
        """
        Test the effect of initializing a mutable object
        directly instead of using Factory(type).
        """

        # Create the first class instance and append elements
        # to list_attribute and list_attribute_with_init_bug.
        obj_1 = AttrsClass()
        obj_1.list_attribute_with_init_bug.append(1)
        obj_1.list_attribute.append(1)

        # Create the second class instance that should have
        # empty list_attribute and list_attribute_with_init_bug.
        obj_2 = AttrsClass()

        # Because list_attribute_with_init_bug is set to [],
        # it is assigned the same object inside obj_1 and obj_2.
        # This is not the intended behavior.
        #
        # This issue is a side effect of how attrs and similar
        # libraries use Python decorators to avoid excessive
        # boilerplate code required by raw Python.
        assert len(obj_2.list_attribute_with_init_bug) == 1

        # Because list_attribute uses Factory(list), it avoids
        # this problem. The Factory creates a separate list
        # instance for each class instance.
        assert len(obj_2.list_attribute) == 0


if __name__ == "__main__":
    pytest.main([__file__])
