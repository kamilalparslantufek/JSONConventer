import requests
import json

# not defined in class, only need to get json request
# in another file, keeping main clear
def get_json(url):
    """Gets JSON from request

    Args:
        url ([string]): [URL to make response]

    Returns:
        [dict]: [JSON file]
    """

    r = requests.get(url)
    r_json = json.loads(r.text)
    return r_json