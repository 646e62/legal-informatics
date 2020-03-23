#!/usr/bin/env python3

"""Generates a standard report"""
from apps.url_tools import *
from apps.api_call_tools import *


# Requests a URL from user input
url = input_url()

# Calls cited_cases() to produce the cited cases lists
case_list = cited_cases(url[0], process_canlii_url(url[1]))

# Formats the cases in an enumerated list
print("Jurisprudence\n=============")

if len(case_list[0]) > 0:
    count = 0
    for case in case_list[0]:
        count += 1
        print(f"({count})\t{case[0]}\n\t{case[1]}")

if len(case_list[1]) > 0:
    print("\nNot reported on CanLII\n----------------------")
    
    count = 0
    for case in case_list[1]:
        count += 1
        print(f"({count})\t{case}")
