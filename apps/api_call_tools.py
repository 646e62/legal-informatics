# API call tools
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

    hosted_case_list = []
    unhosted_case_list = []

    # Formats the styles of cause to McGill 7E standard
    for case in generate_json(api_url)['citedCases']:
        style_of_cause = f"{case['title'].replace('.', '')}, {case['citation']}"
        hosted_case_list.append(style_of_cause)

    
    
    return hosted_case_list, unhosted_case_list
