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

import bottle

# Makes web app much more verbose for debugging
# Should not be used in production
bottle.debug(True)


# Page that will be displayed when main web app URL is opened
@bottle.route("/")
def get_root_page():
    return "Welcome to Bottle!"


if __name__ == "__main__":

    # Run the built-in server locally on the default http port 8080
    bottle.run(host="localhost", port=50100, debug=True)
