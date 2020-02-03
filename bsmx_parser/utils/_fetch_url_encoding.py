"""fetch the html character encodings.

The package comes pre-packed with the url_encodings json. This script is really
just for reference purposes and for when/if the url encodings change.

"""
import requests
import json


def _fetch_url_encoding():
    """fetch the url encodings.

    Fetches the url encodings from the html authorities. Returns a dict with
    the encodings.
    """
    resp = requests.get("https://html.spec.whatwg.org/entities.json")

    raw_json = resp.json()

    encoding_dict = {}
    for code, array in raw_json.items():
        encoding_dict[code] = array['characters']

    return(encoding_dict)


url_encodings = _fetch_url_encoding()

url_encodings_json = json.dumps(url_encodings)
f = open("data/url_encodings.json", "w")
f.write(url_encodings_json)
f.close()
