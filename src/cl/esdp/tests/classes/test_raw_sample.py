# Copyright (C) 2003-present CompatibL. All rights reserved.
#
# This file contains valuable trade secrets and may be copied, stored, used,
# or distributed only in compliance with the terms of a written commercial
# license from CompatibL and with the inclusion of this copyright notice.

import pytest

from cl.esdp.core.classes.raw_sample import RawSample


class TestRawSample:
    """
    Tests for RawSample.
    """

    def test_compare(self):
        """Test RawSample comparison."""

        # Two empty instances are not equal
        assert RawSample() != RawSample()


if __name__ == '__main__':
    pytest.main([__file__])
