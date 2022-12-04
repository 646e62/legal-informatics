'''
A small set of tools that can be used to download decisions from CanLII..

The CanLII website has a RESTful API that can be used to download decisions
from the website. However, the API is not well-documented and the documentation
that is available is not always up-to-date. As a result, I decided to use
user-inputted URLs to download decisions.

CanLII sometimes uses shortened URLs for its search results. The full URL can
be resolved by requesting the shortened URL. The shortened URL can be resolved
using a web browser or using the requests library.

The URL of each decision is composed of several parts. The URL of a decision
follows the following structure:

    {scheme}{separator}{language}/{jurisdiction}/{court}/{type}/{year}/
    {citation}/{file}

The URL can be separated into its components using the '/' character. The
components can then be used to create a local path to a folder where the
decision should be saved. The local path should be structured as follows:

    canlii_data/{jurisdiction}/{court}/{year}

The jurisdiction, court, and year are the first three components of the URL.
The jurisdiction and court folders are created if they don't exist. The year
folder is created if it doesn't exist. The decision is saved to the year
folder using the last component of the URL as the file name. If the file
already exists, it is not downloaded again.

This module contains three functions:

    * resolve_url
    * split_url
    * download_decision

The resolve_url function can be used to resolve a shortened URL. The
split_url function can be used to split the URL into its components. The
download_decision function can be used to download a decision to a local
folder matching the URL.
'''

import os
import requests


# Resolve a full URL from a shortened URL
def resolve_url(short_url: str) -> str:
    '''
    Get the full URL from the shortened URL

    The CanLII website uses shortened URLs for its search results. The full
    URL can be resolved by requesting the shortened URL. The shortened URL can
    be resolved using a web browser or using the requests library.

    This function uses the requests library to resolve the shortened URL using
    the GET method. The timeout is set to 5 seconds.

    Args:
        short_url (str): The shortened URL to resolve.

    Returns:
        str: The full URL of the decision.

    '''
    response = requests.get(short_url, timeout=5)
    return response.url

# Splits the URL into its components and returns its local path
def split_url(url: str)->str:
    '''
    Full CanLII URLs use the following structure:

        {scheme}{separator}{language}/{jurisdiction}/{court}/{type}/{year}/
        {citation}/{file}

    This function splits the URL at the '/' character. As a result, the '//'
    separator returns as two blank list items. Because this project deals with
    NLP specifically directed at legal language, and because I don't speak
    French well enough to parse through its legal linguistic nuances, I've
    excluded French results from this project. As a result, the first list item
    included is jurisdiction.
    '''
    # Splits the URL into components
    full_url_split = url.split('/')

    # Exports a path based on the jurisdiction, court, and year
    jurisdiction = full_url_split[4]
    court = full_url_split[5]
    year = full_url_split[7]
    path =  f"canlii_data/{jurisdiction}/{court}/{year}"
    return path


# Download the decision to a local folder matching the URL
def download_decision(url: str) -> str:
    '''
    Downloads a decision from CanLII to a local folder matching the URL.
    '''
    # Creates the file path
    # Determines whether the URL is shortened or full
    # Shortened URLs use "canlii.ca" while full URLs use "canlii.org"
    if "canlii.ca" in url:
        full_url = resolve_url(url)
    else:
        full_url = url

    # Resolves URLs followed by query terms
    # Shortened URLs don't have query terms
    if "?" in url:
        full_url = url.split('?')[0]
    file_name = full_url.split('/')[-1]

    path = split_url(full_url)
    # Don't download the file if it already exists
    if os.path.exists(f"{path}/{file_name}"):
        return
    else:
        file_path = f"{path}/{file_name}"

        # Get the HTML of the decision
        response = requests.get(url, timeout=10)
        html = response.text

        # Write the HTML to a file
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(html)

        return file_path

# Path: apps/processing/canlii_decision_retriever.py
