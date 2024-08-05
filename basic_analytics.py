# basic_analytics.py

'''
A few proof-of-concept functions to demonstrate the utility of the 
legal_citation_parser package.
'''

import matplotlib.pyplot as plt

from collections import Counter
from legal_citation_parser import create_citation, parse_citation

ABBREVIATION_MAP = {
    "bc": "British Columbia",
    "ab": "Alberta",
    "sk": "Saskatchewan",
    "mb": "Manitoba",
    "on": "Ontario",
    "qc": "Quebec",
    "nb": "New Brunswick",
    "ns": "Nova Scotia",
    "pe": "Prince Edward Island",
    "nl": "Newfoundland and Labrador",
    "yt": "Yukon",
    "nt": "Northwest Territories",
    "nu": "Nunavut",
    "ca": "Canada",
}

def validate_kwargs(citation: str, cited: bool, citing: bool) -> list:
    """
    DRY function used to validate the keyword arguments passed to the function. 
    Future analytics may want to use both cited and citing kwargs, but that's not
    the case for these basic ones.

    Args:
        citation (str): The citation string to be parsed.
        cited (bool): Whether the function is to return cited cases.
        citing (bool): Whether the function is to return citing cases.

    Returns:
        case_list (list): A list of cases that are either cited or citing.
    """

    if cited and not citing:
        case = create_citation(citation, cited=True)
        case_info = case.parse()
        case_list = case_info["cited_cases"]['citedCases']

        return case_list
    
    elif citing and not cited:
        case = create_citation(citation, citing=True)
        case_info = case.parse()
        case_list = case_info["citing_cases"]['citingCases']

        return case_list
    
    else:
        
        return {"error": "Function must operate on either the cited_cases or citing_cases list. Run jurisdiction(citation, cited=True) or (... citing=True)."}
    
def jurisdiction(citation: str, cited=False, citing=False) -> dict:
    """
    Function to return the jurisdiction, court level, and court name of a citation.

    Args:
        citation (str): The citation string to be parsed.
        cited (bool): Whether the function is to return cited cases.
        citing (bool): Whether the function is to return citing cases.

    Returns:
        jurisdiction_counts (dict): A dictionary of jurisdiction counts.
        level_counts (dict): A dictionary of court level counts.
        court_counts (dict): A dictionary of court counts.
    """
 
    case_list = validate_kwargs(citation, cited, citing)
    parsed_case_list = []

    for case in case_list:
        case_info = parse_citation(case["title"] + ", " + case["citation"])
        parsed_case_list.append(case_info)

    # Replace abbreviations with full names
    for case in parsed_case_list:
        if case["jurisdiction"] in ABBREVIATION_MAP:
            case["jurisdiction"] = ABBREVIATION_MAP[case["jurisdiction"]]

    jurisdictions = [case["jurisdiction"] for case in parsed_case_list]
    jurisdiction_counts = Counter(jurisdictions)

    levels = [case["court_level"] for case in parsed_case_list]
    level_counts = Counter(levels)

    courts = [case["jurisdiction"] + " " + case["court_level"] for case in parsed_case_list]
    court_counts = Counter(courts)

    return jurisdiction_counts, level_counts, court_counts

def jurisdiction_analysis(citation: str):
    """
    Function to print out the jurisdiction analysis of a citation.
    """
    
    analysis = jurisdiction(citation, cited=True)

    print("\nJusrisdiction analysis\n==========")
    for item, count in analysis[0].items():
        print(f"{item}: {count}")

    print("\n\nLevel analysis\n==========")
    for item, count in analysis[1].items():
        print(f"{item}: {count}")

    print("\n\nCourt analysis\n==========")
    for item, count in analysis[2].items():
        print(f"{item}: {count}")

def citation_frequency(citation, cited=False, citing=False) -> dict:
    """
    Function to count the frequency of cases by year.

    Args:
        citation (str): The citation string to be parsed.
        cited (bool): Whether the function is to return cited cases.
        citing (bool): Whether the function is to return citing cases.

    Returns:
        year_counts (dict): A dictionary with the year as the key and the frequency of cases as the value.
    """

    case_list = validate_kwargs(citation, cited, citing)
    parsed_case_list = []

    # Count the frequency of each case by year, using the year as the key
    # Note that each case has a "year" attribute
    
    for case in case_list:
        case_info = parse_citation(case["title"] + ", " + case["citation"])
        parsed_case_list.append(case_info["year"])

    year_counts = Counter(parsed_case_list)

    return year_counts

def citation_frequency_analysis(citation: str):
    """
    Plots a bar graph of the citation frequency analysis for a given citation.

    Args:
        citation (str): The citation string to be parsed

    Returns:
        None
    """

    citation_frequency_analysis = citation_frequency(citation, citing=True)
    years = sorted(citation_frequency_analysis.keys())
    frequencies = [citation_frequency_analysis[year] for year in years]

    # Get the case name
    case = create_citation(citation)
    case_name = case.style_of_cause + ", " + case.atomic_citation

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(years, frequencies, color='orange')
    plt.title(f'Citation Frequency Analysis for {case_name}')
    plt.xlabel('Year')
    plt.ylabel('Frequency')

    # Show the plot
    plt.show()
