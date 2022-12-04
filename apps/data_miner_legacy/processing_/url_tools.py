"""Library of URL tools for use with the CanLII API

A small collection of functions used in conjunction with the CanLII API and the
data mining & scraping software being developed for it.
 """

import urllib.request
import urllib.parse
import urllib.error


def verify_canlii_url(url):
    """Verifies that the supplied input is a valid CanLII URL. Returns a """

    # urllib.request.urlopen() verifies the input is a valid URL
    # geturl() expands shortened URLs
    try:

        url = urllib.request.urlopen(url).geturl()
    except:
        print(f"Error: cannot reach {url}")
        return None

    url_data = url.split("/")

    # Double (weak) URL verification
    if len(url_data) != 10:
        print("Error: invalid URL")
        return None
    if url_data[2] != "www.canlii.org":
        print("Error: URL must contain www.canlii.org")
        return None

    return url, url_data


def correct_database_id(database_id):
    """Corrects database_id values to meet the API standard"""

    if database_id == "scc":
        database_id = "csc-scc"

    return database_id


def process_canlii_url(url):
    """Processes a valid CanLII URL and returns a dictionary."""

    # Correct database_id values to meet the API standards
    url[5] = correct_database_id(url[5])

    # Double (weak) URL verification
    if len(url) == 10 and url[2] == "www.canlii.org":
        return {"protocol": url[0][:-1],
                "hostname": url[2],
                "language": url[3],
                "jurisdiction": url[4],
                "database_id": url[5],
                "page_type": url[6],
                "year": url[7],
                "case_id": url[8],
                "file_name": url[9],
                }
    else:
        return None


def download_website(url):
    """Requests, opens, reads, and decodes a website. Returns the result as
    a string
    Using the requests module should eliminate the need for this function
    """
    handle = urllib.request.urlopen(url)
    data = handle.read().decode()

    return data


def input_url():
    """Obtains a URL for verification and processing using user input"""
    webpage = input("Enter URL: ")

    while True:
        try:
            url = verify_canlii_url(webpage)[0]
            url_data = verify_canlii_url(webpage)[1]
            break
        except:
            webpage = input("Enter URL: ")

    return url, url_data


def url_constructor_case(case):
    """Builds URLs from data"""

    language_dict = case['caseId']
    for key, value in language_dict.items():
        language = key
        style_of_cause = value

    court = case['databaseId']
    if court == "csc-scc":
        court = "scc"

    jurisdiction = court[:2]
    if jurisdiction == "sc" or jurisdiction == "fc":
        jurisdiction = "ca"

    year = style_of_cause[:4]
    url = ( "<https://www.canlii.org/"
            f"{language}/{jurisdiction}/{court}/doc/"
            f"{year}/{style_of_cause}/{style_of_cause}.html>")

    return url
