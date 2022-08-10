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
from attr import Factory
from attrs import define


@define
class AttrsClass:
    """
    Sample class for the attrs library.
    """

    int_attribute: Optional[int] = None
    """Optional integer attribute."""

    list_attribute_with_init_bug: List[int] = []
    """
    If an attribute is a mutable type, it has to
    be initialized using Factory(type). Otherwise,
    its default value will be unintentionally shared
    between different class instances.
    
    This issue is a side effect of how attrs and similar
    libraries use Python decorators to avoid excessive
    boilerplate code required by raw Python approach 
    shown in UnsafeClass to specify a new attribute.
    This bug does not happen for UnsafeClass, making
    it safe in this one respect.
    """

    list_attribute: List[int] = Factory(list)
    """
    Only assigning Factory(list) avoids this problem.
    """
