# Copyright (C) 2003-present CompatibL. All rights reserved.
#
# This file contains valuable trade secrets and may be copied, stored, used,
# or distributed only in compliance with the terms of a written commercial
# license from CompatibL and with the inclusion of this copyright notice.

import pytest

from cl.esdp.core.classes.raw_class import UnsafeClass


class TestUnsafeClass:
    """
    Tests for UnsafeClass.
    """

    def test_attribute_name(self):
        """Test wrong attribute name."""

        # Assign value of attribute with typo in name
        unsafe_obj = UnsafeClass()

        # Attribute name has a typo here
        unsafe_obj.instance_attirbute = 2

        # But not here, so it has the old value
        assert unsafe_obj.instance_attribute == 1  # But not here

        # And there is now a second, unwanted attribute with typo in name
        assert unsafe_obj.instance_attirbute == 2

    def test_compare(self):
        """Test UnsafeClass comparison."""

        # Two empty instances are not equal
        assert UnsafeClass() != UnsafeClass()


if __name__ == "__main__":
    pytest.main([__file__])
