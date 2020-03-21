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
import sys

from url_tools import *
from json_tools import *
from api_call_tools import *


def cited_cases(database_id, case_id):
    citation_api_call = (
        "https://api.canlii.org/v1/caseCitator/en/"
        f"{database_id}/{case_id}/citedCases?api_key={key}")

    return citation_api_call


# verify_url() verifies and formats valid input
webpage = input("Enter URL: ")

while True:
    try:
        url = verify_canlii_url(webpage)[1]
        break
    except:
        webpage = input("Invalid URL: ")

# Imports the CanLII API key from a text file
# Error and exit if the API key is not present
try:
    with open("key.txt") as api_key:
        key = api_key.readlines()[0].strip()
except FileNotFoundError:
    print("A CanLII API key is required to process this request")
    sys.exit()

url_dict = process_canlii_url(url)
api_call = cited_cases(url_dict['database_id'], url_dict['case_id'])

# Requests, reads/decodes, and returns the JSON file as the json_file dictionary
handle = urllib.request.urlopen(api_call)
data = handle.read().decode()
json_file = json.loads(data)
case_list = []

# Formats the styles of cause to McGill 7E standard
for case in json_file['citedCases']:
    case_list.append(f"{case['title'].replace('.', '')}, {case['citation']}")

# Formats the cases in an enumerated list
count = 0
for case in case_list:
    count += 1
    print(f"({count}) {case}")
