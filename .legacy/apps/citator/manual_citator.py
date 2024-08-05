'''
Generates a McGill-style citation from user input. The citation should be in
HTML format.

This module requires the user to input all of the citation's components. The
auto_citator.py module generates citations from CanLII webpages using the API
call and the BeautifulSoup library.

The manual_citator.py module can generate citations for legislation,
jurisprudence, and secondary sources. Future versions will include citations
for foreign sources.
'''

from string import punctuation
from objects import Decision

def punctuation_remover(text):
    '''
    Removes punctuation from a string.
    '''
    for symbol in punctuation:
        text = text.replace(symbol, '')

# Function to generate McGill-style citations

def legislation_mcgill_9e(title: str,
                short_title: str,
                statute_volume: str,
                year: str,
                chapter: str,
                index_elements: str,
                session_supplement: str,
                pinpoint: str) -> str:
    '''
    Generates a McGill-style citation for legislation.
    '''
    # 
    if short_title:
        title = short_title
    else:
        title = f"<em>{punctuation_remover(title)}</em>"

def jurisprudence_mcgill_9e(style_of_cause: str,
                  citation: str,
                  pinpoint: str,
                  parallel_citations: tuple[str]) -> str:

    '''
    Generates a McGill-style citation for jurisprudence.
    '''

def secondary_mcgill_9e():
    '''
    Generates a McGill-style citation for secondary sources.
    '''

