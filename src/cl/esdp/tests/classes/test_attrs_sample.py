# Copyright (C) 2003-present CompatibL. All rights reserved.
#
# This file contains valuable trade secrets and may be copied, stored, used,
# or distributed only in compliance with the terms of a written commercial
# license from CompatibL and with the inclusion of this copyright notice.

import pytest

from cl.esdp.core.classes.attrs_sample import AttrsSample


class TestAttrsSample:
    """
    Tests for AttrsSample.
    """

    def test_compare(self):
        """Test AttrsSample comparison."""

        # Unlike for raw classes, empty instances of attrs classes are equal
        assert AttrsSample() == AttrsSample()


if __name__ == '__main__':
    pytest.main([__file__])
