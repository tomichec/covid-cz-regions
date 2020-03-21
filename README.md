# Czech COVID-19 Cases

This scripts downloads and prints the data about the COVID-19 cases
based on the Czech Ministry of Healthcare Services. The data are
sourced from the regional hygenic stations.

As of now (March 21) the total does not match the officially published
data for the whole of Czechia.

## Prerequisites

Python3, BeautifulSoup library (python3-bs4).

## Usage

Clone the repository, go to the repository folder in the terminal and
run the following command:

```
python3 regions_cases.py
```

## Output Example

The output is printed to standard output as JSON, where the key is the
name of the region and value represents the number of cases detected.

```
{
	"Hlavní město Praha": 135,
	"Středočeský kraj": 118,
	"Jihočeský kraj": 30,
	"Plzeňský kraj": 17,
	"Karlovarský kraj": 32,
	"Ústecký kraj": 36,
	"Liberecký kraj": 9,
	"Královéhradecký kraj": 15,
	"Pardubický kraj": 22,
	"Kraj Vysočina": 9,
	"Jihomoravský kraj": 66,
	"Olomoucký kraj": 68,
	"Zlínský kraj": 51,
	"Moravskoslezský kraj": 79,
}
```

## Copyright Notice

This code is released under MIT licence.


