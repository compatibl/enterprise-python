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

import json
import flask
import requests

# Create a Flask app object
app = flask.Flask(__name__)

# Port used by fastapi_blotter.py
api_url = "http://localhost:50301"


# Page that will be displayed when main web app URL is opened
@app.route("/")
def get_main_page():
    """Display trade blotter"""

    page_and_table_header = """<!DOCTYPE html>
<html lang="en">
<head>
    <title>Flask Trade Blotter</title>
    <link rel="stylesheet" type="text/css" href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css">
</head>
<body>
    <h1>Flask Trade Blotter</h1>
    <h2>All trades</h2>
       <table>
          <tr><td>Trade</td><td>Ccy1</td><td>Ccy2</td></tr>"""

    page_and_table_footer = """       </table>
</body>
</html>"""

    # Retrieve trades from REST API
    trade_str_dict = requests.post(api_url + "/query_trades").json()
    trade_str_list = trade_str_dict["trades"]
    trades = [json.loads(trade_str) for trade_str in trade_str_list]

    # Form table rows
    trade_rows = [
        f"<tr>"
        f"<td>{trade['trade_id']}</td>"
        f"<td>{trade['legs'][0]['leg_ccy']}</td>"
        f"<td>{trade['legs'][1]['leg_ccy']}</td>"
        f"</tr>"
        for trade in trades
    ]
    table_rows = "\n".join(trade_rows)

    # Return complete page with header and footer
    return f"{page_and_table_header}{table_rows}{page_and_table_footer}"


# Run the built-in server locally on the default http port 8080
if __name__ == "__main__":
    app.run(host="localhost", port=50201, debug=True)
