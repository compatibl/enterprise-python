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

import flask

# Create a Flask app object
import requests

app = flask.Flask(__name__)

# Port used by fastapi_blotter.py
api_url = "http://localhost:50301"


# Page that will be displayed when main web app URL is opened
@app.route("/")
def get_main_page():
    """Display trade blotter"""
    response = requests.get(api_url + "/trades")
    return "Welcome to Bottle Trade Blotter!\n\n" + str(response.json())


# Run the built-in server locally on the default http port 8080
if __name__ == '__main__':
    app.run(host='localhost', port=50201, debug=True)
