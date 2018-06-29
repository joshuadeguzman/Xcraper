import pandas as pd
import requests

baseUrl = 'http://www.pesobility.com/'


def str_join(*args):
    """
    Joins strings base on arguments received
    :param args: Strings to be concatenated
    :type args: str
    :return: formatted string
    """
    return ''.join(map(str, args))


def get_stock_list(output_type):
    """
    Calls stock list via specified url
    """
    url = 'stock'
    render_data_request(url, output_type)


def get_top_gainers(output_type):
    """
    Calls top gainers via specified url
    """
    url = 'reports/top-gainers'
    render_data_request(url, output_type)


def get_worst_losers(output_type):
    """
    Calls worst gainers via specified url
    """
    url = 'reports/worst-losers'
    render_data_request(url, output_type)


def get_most_active(output_type):
    """
    Calls most active via specified url
    """
    url = 'reports/most-active'
    render_data_request(url, output_type)


def render_data_request(url, output_type):
    """
    Returns data base output_type format
    :param url: Url request based on request' sub path
    :type url: str
    :param output_type: Requested output type
    :type: output_type: str
    :return: prints formatted output_type request of the data
    """
    url = str_join(baseUrl, url)

    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    r = requests.get(url, header)

    dfs, = pd.read_html(r.text)
    if output_type == "json":
        # Prints json formatted data
        print(dfs.to_json(orient="records", date_format="iso"))
    elif output_type == "table":
        # Prints table formatted data
        print(dfs)
    else:
        # Prints table formatted data
        print(dfs)


# Initial requests
# You can also initially call render_data_request() for dynamic url request under the base url
get_stock_list("table")
get_top_gainers("table")
get_worst_losers("table")
get_most_active("table")
