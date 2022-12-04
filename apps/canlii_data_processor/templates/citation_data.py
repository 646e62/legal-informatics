'''
These classes should be broad enough to include the type of data required by 
all Canadian courts, as well as the McGill Guide.
'''

from typing import List

class Decision:
    '''
    Stores case data

    Attributes:
        case_name (str): The name of the case.
        neutral_citation (str): The neutral citation of the case.
        additional_citations (list): Additional citations of the case.
        pinpoint (str): The pinpoint of the case.

    '''

    def __init__(self,
                case_name: str,
                neutral_citation: str,
                additional_citations: List[str],
                pinpoint: str):
        self.case_name = case_name
        self.neutral_citation = neutral_citation
        self.additional_citations = additional_citations
        self.pinpoint = pinpoint

    def sk_citation(self):
        '''
        Returns a Saskatchewan-style citation.
        '''
        
        pass

class Legislation:
    '''
    Stores legislation data
    '''

class SecondarySource:
    '''
    Stores secondary source data
    '''
