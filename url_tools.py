import urllib.request
import urllib.parse
import urllib.error


def verify_url(url):
    """Verifies that the supplied input is a valid CanLII URL. Returns a """

    # urllib.request.urlopen() verifies the input is a valid URL
    # geturl() expands shortened URLs
    try:
        url = urllib.request.urlopen(url).geturl()
    except:
        return None

    url_data = url.split("/")

    # Check list length & verify the hostname is www.canlii.org
    if len(url_data) != 10:
        return None
    if url_data[2] != "www.canlii.org":
        return None

    return url, url_data
