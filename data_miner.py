#!/usr/bin/env python3

"""
V 0.2
Minimally functional web scraper that extracts all of the cases cited in a
reported decision on CanLII.

Accepts a URL from a CanLII decision as input and returns all of the cases that
 the decision cites. Current version uses the CanLII API to pull and display a
JSON file from the service.

The current version is limited to "casesCited" calls. The casesCited call does
not pick up cases that are not indexed on CanLII, so several results will be
missing
"""

import urllib
import json
from url_tools import verify_canlii_url
from url_tools import process_canlii_url


# verify_url() verifies and formats valid input
webpage = input("Enter URL: ")

while True:
    try:
        url = verify_canlii_url(webpage)[1]
        break
    except:
        webpage = input("Invalid URL: ")

url_dict = process_canlii_url(url)

# Imports the CanLII API key from a text file
with open("key.txt") as api_key:
    key = api_key.readlines()[0].strip()

# Assigns the correctly formatted API call string to citation_api_call
citation_api_call = (
    "https://api.canlii.org/v1/caseCitator/en/"
    f"{url_dict['database_id']}/{url_dict['case_id']}/citedCases?api_key={key}")

# Requests, reads/decodes, and returns the JSON file as the json_file dictionary
handle = urllib.request.urlopen(citation_api_call)
data = handle.read().decode()
json_file = json.loads(data)
case_list = []

for case in json_file['citedCases']:
    case_list.append(f"{case['title'].replace('.', '')}, {case['citation']}")

# Formats the cases in an enumerated list
count = 0
for case in case_list:
    count += 1
    print(f"({count}) {case}")
