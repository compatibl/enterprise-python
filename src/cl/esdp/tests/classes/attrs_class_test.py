# Copyright (C) 2003-present CompatibL. All rights reserved.
#
# This file contains valuable trade secrets and may be copied, stored, used,
# or distributed only in compliance with the terms of a written commercial
# license from CompatibL and with the inclusion of this copyright notice.

import pytest

from cl.esdp.core.classes.attrs_class import AttrsClass


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

    def test_list_attribute_initialization(self):
        """Test the effect of initializing a list attribute using [] rather than list()."""

        # Create first class instance and append an element
        # to the three list attributes
        obj_1 = AttrsClass()
        obj_1.list_attribute_with_init_bug_1.append(1)
        obj_1.list_attribute_with_init_bug_2.append(1)
        obj_1.list_attribute.append(1)

        # Create second class instance that should have
        # three empty list attributes.
        obj_2 = AttrsClass()

        # The first two are not empty because their values
        # are shared with the other instance. This does not
        # make them class attributes. Rather, they are
        # instance attributes whose value is shared across
        # all class instances. Unlike for class attributes,
        # separate values can be assigned if desired.
        #
        # This issue is a side effect of how attrs and similar
        # libraries use Python decorators to avoid excessive
        # boilerplate code required by raw Python approach
        # shown in UnsafeClass to specify a new attribute.
        # This bug does not happen for UnsafeClass, making
        # it safe in this one respect.
        assert len(obj_2.list_attribute_with_init_bug_1) == 1
        assert len(obj_2.list_attribute_with_init_bug_2) == 1

        # Only the attribute that uses Factory(list) avoids
        # this problem. The Factory creates a separate list
        # instance for each class instance.
        assert len(obj_2.list_attribute) == 0


if __name__ == "__main__":
    pytest.main([__file__])
