import requests
from bs4 import BeautifulSoup
import json

def main():
    url = "https://onemocneni-aktualne.mzcr.cz/covid-19"
    response = requests.get(url)
    if (response.status_code != 200):
        print("The page is unavailable, error code: ", response.status_code)
        return

    parsed_html = BeautifulSoup(response.text, "html.parser")

    total_regions_data = parsed_html.body.find('div', attrs={'id':'js-total-regions-data'})
    data = json.loads(total_regions_data['data-barchart'])

    total = 0

    print("{")
    for region in data['values']:
        print('\t"%s": %s,' % (region['x'],region['y']))
        total += region['y']
        n += 1
    print('\t"%s": %s,' % ("total",total))
    print("}")

if (__name__ == "__main__"):
    main()
