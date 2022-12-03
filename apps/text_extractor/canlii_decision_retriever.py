import requests
import urllib.parse
import os


# Resolve a full URL from a shortened URL
def resolve_url(short_url):
    ''' 
    Get the full URL from the shortened URL
    '''
    response = requests.get(short_url)
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
    split_url = url.split('/')

    # Exports a path based on the jurisdiction, court, and year
    jurisdiction = split_url[4]
    court = split_url[5]
    year = split_url[7]
    path =  f"canlii_data/{jurisdiction}/{court}/{year}"
    return path


# Download the decision to a local folder matching the URL
def download_decision(url):
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
        response = requests.get(url)
        html = response.text

        # Write the HTML to a file
        with open(file_path, 'w') as f:
            f.write(html)

        return file_path


