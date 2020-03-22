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


def process_canlii_url(url):
    """Processes a valid CanLII URL and returns a dictionary."""
    # Correct database_id values to meet the API standards

    if url[5] == "scc":
        url[5] = "csc-scc"
    
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
    handle = urllib.request.urlopen(url)
    data = handle.read().decode()

    return data


def input_url():
    webpage = input("Enter URL: ")

    while True:
        try:
            url = verify_canlii_url(webpage)[0]
            url_data = verify_canlii_url(webpage)[1]
            break
        except:
            webpage = input("Enter URL: ")

    return url, url_data


# def url_constructor(case_list):

#    return url_list
