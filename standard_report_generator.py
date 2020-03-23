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
from apps.url_tools import *
from apps.api_call_tools import *


# Requests a URL from user input
url = input_url()

# Cals cited_cases() to produce the cited cases lists
case_list = cited_cases(url[0], process_canlii_url(url[1]))

# Formats the cases in an enumerated list
print("Jurisprudence\n=============")
print("\nHosted cases\n------------")

count = 0
for case in case_list[0]:
    count += 1
    print(f"({count})\t{case}")

print("\nNot hosted on CanLII\n--------------------")
    
count = 0
for case in case_list[1]:
    count += 1
    print(f"({count})\t{case}")
