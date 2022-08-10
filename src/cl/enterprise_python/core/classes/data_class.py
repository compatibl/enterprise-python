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

from typing import Optional, List
from dataclasses import dataclass, field


@dataclass  # TODO - change to @dataclass(slots=True) after Python 3.10 upgrade
class DataClass:
    """
    Sample class for the dataclass decorator.

    In Python 3.10 we could write @dataclass(slots=True),
    but we are currently using Python 3.9 for this repo.
    """

    int_attribute: Optional[int] = None
    """Optional integer attribute."""

    # list_attribute_with_init_bug: List[int] = []
    #
    # If this code was allowed, the default value would be
    # unintentionally shared between different class instances.
    #
    # Fortunately, dataclass will not permit this code
    # to run and uncommenting this code line would cause
    # an error. Not all data class libraries offer such
    # protection, for example the current version of attrs
    # a similar code would execute and cause a bug.

    list_attribute: List[int] = field(default_factory=list)
    """
    Use default_factory for mutable attributes.
    """
