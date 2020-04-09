import requests
from bs4 import BeautifulSoup
import json

def main():
    data = get_data()
    print_data(data)

def get_data():
    url = "https://onemocneni-aktualne.mzcr.cz/covid-19"
    response = requests.get(url)
    if (response.status_code != 200):
        print("The page is unavailable, error code: ", response.status_code)
        return

    parsed_html = BeautifulSoup(response.text, "html.parser")
    total_regions_data = parsed_html.body.find('div', attrs={'id':'js-total-isin-regions-data'})

    return json.loads(total_regions_data['data-barchart'])

def print_data(data):
    total = 0
    output_string = "{\n"
    for region in data['values']:
        output_string += ('\t"%s": %s,\n' % (region['x'],region['y']))
        total += region['y']

    # print('\t"%s": %s,' % ("Total",total))
    output_string = output_string[:-2]
    output_string += "\n}"

    print(output_string)

if (__name__ == "__main__"):
    main()
