import json

import requests


class HTTP:
    @staticmethod
    def get(url, params, return_json=True):
        r = requests.get(url, params=params)
        if r.status_code != 200:
            return None
        else:
            return json.loads(r.text) if return_json else r.text
