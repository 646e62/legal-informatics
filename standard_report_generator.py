#!/usr/bin/env python3

"""
V0.3: forked from data_miner.py

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

url = input_url()
case_list = cited_cases(url[0], process_canlii_url(url[1]))

# Formats the cases in an enumerated list
print("\n=============\nJurisprudence\n=============\n")


count = 0
for case in case_list[0]:
    count += 1
    print(f"({count})\t{case}")
