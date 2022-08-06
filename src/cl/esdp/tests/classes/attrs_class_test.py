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

    def test_compare(self):
        """Test AttrsClass comparison."""

        # Unlike for raw classes, empty instances of attrs classes are equal
        assert AttrsClass() == AttrsClass()


if __name__ == "__main__":
    pytest.main([__file__])
