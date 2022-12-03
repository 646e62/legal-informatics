'''
These functions convert an HTML file into text and identify several components
of the decision. These include:

    - The decision title
    - The decision date
    - The decision text
    - Block quotes
    - Citations

These functions use Beautiful Soup to parse the HTML file into numbered 
paragraphs. 

'''

from bs4 import BeautifulSoup

# Reads the HTML file and parses it into a BeautifulSoup object
def read_html_file(filename: str)->BeautifulSoup:
    with open(filename, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
    return soup


# Extracts the decision text
def extract_decision_text(paragraphs: list)->list:
    '''
    
    '''
    numbered_paragraphs = identify_numbered_paragraphs(paragraphs)

    decision_text = []

    for paragraph in numbered_paragraphs:
        decision_text.append(paragraph)

    return decision_text

# Appends paragraph text to a list
def generate_paragraphs(soup: BeautifulSoup)->list:

    paragraphs = []

    for paragraph in soup.find_all('p'):
        paragraphs.append(paragraph.text)

    return paragraphs

# Remove a non-alpha item from a list
def remove_non_alpha(item: str)->str:
    return item.isalpha()

# Remove a string from a list if the string is a number
def remove_numbers(item: str)->str:
    return item.isnumeric()

# Identifies numbered paragraphs
def identify_numbered_paragraphs(paragraphs: list)->list:
    '''
    Numbered paragraphs are contained in the <div class="paragWrapper"> tags.
    But some paragraphs are followed by block quotes or enumerated lists that
    aren't contained in the <div class="paragWrapper"> tag. This function 
    appends these outlier paragraphs to the text contained in <div class=
    "paragWrapper"> tag immediately preceding.
    '''

    numbered_paragraphs = []

    for paragraph in paragraphs:
        if paragraph.find('div class="paragWrapper">') != -1:
            numbered_paragraphs.append(paragraph)

    return numbered_paragraphs
