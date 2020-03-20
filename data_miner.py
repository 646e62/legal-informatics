#!/usr/bin/env python3

"""
V 0.1
Minimally functional web scraper that extracts all of the cases cited in a
reported decision on CanLII.

Accepts a URL from a CanLII decision as input and returns all of the cases that
 the decision cites. Current version uses the CanLII API to pull and display a
JSON file from the service.

The current version is limited to "casesCited" calls. The casesCited call does
not pick up cases that are not indexed on CanLII, so several results will be
missing
"""

import urllib.request
import urllib.parse
import urllib.error
import json

# Pulls a URL from a string.
# The while-try-except keeps the input honest by attempting to assign the
# HTTPrequest to a valid URL, and by demanding a valid URL when it receives
# bad input

webpage = input("Enter URL: ")
while True:
    try:
        webpage_data = urllib.request.urlopen(webpage)
        break
    except:
        webpage = input("Invalid URL: ")

# Expands the URL when a shortened version is supplied
# The webpage input string is replaced with the expanded URL
if len(webpage) < 25:
    webpage = webpage_data.geturl()

# Extracts the databaseId and caseID from the long form URL
url_data = webpage[8:].split("/")
language = url_data[1]
database_id = url_data[3]
case_id = url_data[6]

# Corrects database_id values to meet the API's standards
# Currently only accounts for SCC decisions, because this is the only outlier
# I've noticed so far
if database_id == "scc":
    database_id = "csc-scc"

# Imports the CanLII API key from a text file, refines the data and makes it
# available for the API call
# Needs to be secured/encypted before the program goes live
with open("key.txt") as api_key:
    key = api_key.readlines()[0].strip()

# Assigns the correctly formatted API call string to citation_api_call
citation_api_call = (
    "https://api.canlii.org/v1/caseCitator/en/"
    f"{database_id}/{case_id}/citedCases?api_key={key}")

# Requests, reads, decodes, and returns the JSON file as json_file
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
