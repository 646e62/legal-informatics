'''
Tools to gather case information via the CanLII API.
'''

# API call tools
import json
import requests
from bs4 import BeautifulSoup

from api_key import generate_key
from url_tools import *

def generate_json(api_url: str) -> dict:
    '''
    Generates a JSON object from an API call.
    '''
    return json.loads(download_website(api_url))


def cited_cases(url, url_data):
    """citedCases call

    Returns a formatted list of case name strings. Future versions to include
    case URLs and cases that are not hosted on CanLII
    """

    database_id = url_data['database_id']
    case_id = url_data['case_id']
    key = generate_key()
    api_url = ("https://api.canlii.org/v1/caseCitator/en/"
               f"{database_id}/{case_id}/citedCases?api_key={key}")

    # Formats the styles of cause to McGill 7E standard
    # Hosted cases
    hosted_cases = []
    case_dictionary = generate_json(api_url)['citedCases']
    for case in case_dictionary:

        style_of_cause = f"{case['title'].replace('.', '')}, {case['citation']}"
        case_url = url_constructor_case(case)
        hosted_cases.append((style_of_cause, case_url))


    # Unhosted cases
    unhosted_cases = cited_cases_unhosted(url)

    return hosted_cases, unhosted_cases

def cited_cases_unhosted(url):
    """Scrapes a valid CanLII decision page for cited cases not available on
    CanLII
    """

    html = requests.get(url)
    data = BeautifulSoup(html.content, 'html.parser')
    results = data.find_all("div", class_='col flex-wrap')
    unhosted_cases = []

    for result in results:

        if "(not available on CanLII)" in result.text:
            unhosted_cases.append(
                result.text.strip().replace(
                    '.', ''
                ).replace(
                    '(not available on CanLII)', ''
                )
            )

    return unhosted_cases
