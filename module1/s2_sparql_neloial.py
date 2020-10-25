"""Query Wikidata for Belgian cities and towns"""

import argparse

from SPARQLWrapper import SPARQLWrapper, JSON

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filter', type=str, help='Filtering on name')
parser.add_argument('-n', '--number', type=int, help='Number of rows to display')

def get_rows():
    """Retrieve results from SPARQL"""
    endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
    sparql = SPARQLWrapper(endpoint)

    statement = """
    #Population of cities and towns in Belgium 
    SELECT DISTINCT ?city ?cityLabel ?population WHERE {
        SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
        VALUES ?town_or_city {
            wd:Q3957
            wd:Q515
        }
        ?city (wdt:P31/(wdt:P279*)) ?town_or_city;
            wdt:P17 wd:Q31.
        OPTIONAL { ?city wdt:P1082 ?population. }
    }
    ORDER BY ?cityLabel
    """

    sparql.setQuery(statement)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    rows = results['results']['bindings']
    print(f"\n{len(rows)} Belgian cities and towns found\n")
    return rows

def show(rows, name_filter=None, n=20):
    """Display n towns or cities in Belgium (default=20)"""
  
    if name_filter:
        rows = [row for row in rows if name_filter.lower() in row['cityLabel']['value'].lower()]
    print(f"Displaying the first {n}:\n")
    for row in rows[:n]:
        try:
            pop = row['population']['value']
        except KeyError:
            pop = "????"
        print(f"{row['cityLabel']['value']} ({pop})")

if __name__ == "__main__":
    args = parser.parse_args()
    my_rows = get_rows()
    my_filter = args.filter if args.filter else None
    number = args.number if args.number else 20
    show(my_rows, my_filter, number)
