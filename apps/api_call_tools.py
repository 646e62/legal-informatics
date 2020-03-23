# API call tools
import requests
from bs4 import BeautifulSoup

from apps.api_key import *
from apps.url_tools import *
from apps.json_tools import *


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
        hosted_cases.append(style_of_cause + "\n\t" + case_url)


    # Unhosted cases
    unhosted_cases = cases_cited_unhosted(url)

    return hosted_cases, unhosted_cases

def cases_cited_unhosted(url):

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
