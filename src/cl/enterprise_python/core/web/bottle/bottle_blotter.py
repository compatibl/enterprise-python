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

import bottle
import requests

# Makes web app much more verbose for debugging
# Should not be used in production
bottle.debug(True)

# Port used by fastapi_blotter.py
api_url = "http://localhost:50301"


# Page that will be displayed when main web app URL is opened
@bottle.route('/')
def get_main_page():
    """Display trade blotter"""

    page_and_table_header = """<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Bottle Home</title>
    <link rel="stylesheet" type="text/css" href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css">
</head>
<body>
    <h1>All trades</h1>
    <div >My List A</div>
       <ol>"""

    page_and_table_footer = """       </ol>
    </div>
</body>
</html>"""

    # Retrieve trades from REST API
    trade_str_dict = requests.post(api_url + "/query_trades").json()
    trade_str_list = trade_str_dict["trades"]
    trades = [json.loads(trade_str) for trade_str in trade_str_list]

    # Form table rows
    trade_rows = [f"{trade['trade_id']}" for trade in trades]
        #f"    trade_id={trade.trade_id} trade_type={trade.trade_type} "
        #     f"leg_type[0]={trade.legs[0].leg_type} leg_ccy[0]={trade.legs[0].leg_ccy} "
        #     f"leg_type[1]={trade.legs[1].leg_type} leg_ccy[1]={trade.legs[1].leg_ccy}\n"
    table_rows = "\n".join([f"<li>{trade_row}</li>" for trade_row in trade_rows])

    # Return complete page with header and footer
    return f"{page_and_table_header}{table_rows}{page_and_table_footer}"



if __name__ == "__main__":

    # Run the built-in server locally on the default http port 8080
    bottle.run(host='localhost', port=50101, debug=True)
