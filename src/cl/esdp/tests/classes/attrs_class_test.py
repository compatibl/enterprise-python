# Copyright (C) 2003-present CompatibL. All rights reserved.
#
# This file contains valuable trade secrets and may be copied, stored, used,
# or distributed only in compliance with the terms of a written commercial
# license from CompatibL and with the inclusion of this copyright notice.

import pytest

from cl.esdp.core.classes.attrs_class import AttrsClass


class TestAttrsClass:
    """
    Tests for AttrsClass.
    """

    def test_attribute_name(self):
        """Test the effect of a typo in attribute name."""

        # Assign value of attribute with typo in name
        attrs_obj = AttrsClass()

        # Attribute name has a typo here, and this assignment
        # will throw an exception for AttrsClass
        attrs_obj.instance_attirbute = 2

    def test_compare(self):
        """Test AttrsClass comparison."""

        # Unlike for raw classes, empty instances of attrs classes are equal
        assert AttrsClass() == AttrsClass()


if __name__ == "__main__":
    pytest.main([__file__])
