import requests
from bs4 import BeautifulSoup
import json

def main():
    raw = get_data()
    processed = process_data(raw)
    print(json.dumps(processed,indent=4, sort_keys=True, ensure_ascii=False))

def get_data():
    url = "https://onemocneni-aktualne.mzcr.cz/covid-19"
    response = requests.get(url)
    if (response.status_code != 200):
        print("The page is unavailable, error code: ", response.status_code)
        return

    parsed_html = BeautifulSoup(response.text, "html.parser")
    total_regions_data = parsed_html.body.find('div', attrs={'id':'js-total-isin-regions-data'})

    return json.loads(total_regions_data['data-barchart'])


def process_data(raw):
    total = 0
    regions_cases = {}
    for region in raw['values']:
        region_key   = region['x']
        region_value = region['y']
        regions_cases[region_key] = region_value

    return regions_cases


if (__name__ == "__main__"):
    main()
