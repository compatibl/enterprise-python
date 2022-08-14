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


class QualityUtil:
    """Helper class for specifying result quality vs. run time."""

    quality: int = 5
    """
    Set this class attribute to specify result quality vs. run time:

    * Quality 0 only checks that the test completes but not the results
    * Quality 1 is for smoke tests
    * Quality 5 is the default for which approval tests are recorded

    For other values of quality, methods return adjusted inputs such
    that an increase in quality by 1 corresponds to approximately
    double of the run time.
    """
