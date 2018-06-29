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


def get_top_gainers():
    """
    Calls top gainers url when called
    """
    top_gainers_url = 'reports/top-gainers'
    render_data_request(top_gainers_url)


def render_data_request(url):
    """
    Returns output in json format
    :param url: Url request based on request' sub path
    :type url: str
    :return: outputs json formatted request of the data
    """
    url = str_join(baseUrl, url)

    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    r = requests.get(url, header=header)

    dfs, = pd.read_html(r.text)
    print(dfs.to_json(orient="records", date_format="iso"))


# Initial requests
get_top_gainers()
