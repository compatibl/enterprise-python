# Copyright (C) 2003-present CompatibL. All rights reserved.
#
# This file contains valuable trade secrets and may be copied, stored, used,
# or distributed only in compliance with the terms of a written commercial
# license from CompatibL and with the inclusion of this copyright notice.

import pytest

from cl.esdp.core.classes.unsafe_class import UnsafeClass


class TestUnsafeClass:
    """
    Tests for UnsafeClass.
    """

    def test_attribute_name(self):
        """Test the effect of a typo in attribute name."""

        # Assign value of attribute with typo in name
        unsafe_obj = UnsafeClass()

        # Attribute name has a typo here
        unsafe_obj.instance_attirbute = 2

        # But not here, so it has the old value
        assert unsafe_obj.instance_attribute == 1

        # And there is now a second, unwanted attribute with typo in name
        assert unsafe_obj.instance_attirbute == 2

    def test_equality(self):
        """Test for the built-in equality operator."""

        # One expects these two instances to be equal,
        # but with UnsafeClass they are not
        with pytest.raises(AssertionError):
            assert UnsafeClass() == UnsafeClass()


if __name__ == "__main__":
    pytest.main([__file__])
