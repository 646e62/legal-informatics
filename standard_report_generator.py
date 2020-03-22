#!/usr/bin/env python3

"""
V0.2: forked from data_miner.py

Generates the standard report, which includes the following elements:
* Style of cause
* URL
* Legislation cited
* Cases cited
* Metadata
"""

import urllib
import json

from apps.url_tools import *
from apps.json_tools import *
from apps.api_call_tools import *
from apps.api_key import *

# verify_url() verifies and formats valid input
webpage = input("Enter URL: ")

while True:
    try:
        url = verify_canlii_url(webpage)[0]
        url_data = verify_canlii_url(webpage)[1]
        break
    except:
        webpage = input("Invalid URL: ")

case_list = cited_cases(url, process_canlii_url(url_data))[0]

# Formats the cases in an enumerated list
print("\n=============\nJurisprudence\n=============\n")


count = 0
for case in case_list:
    count += 1
    print(f"({count})\t{case}")
