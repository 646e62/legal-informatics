'''
Generates McGill Guide-compliant citations from CanLII webpages.

Short titles:
    * Generate a short title from a full title using NLP techniques.
'''

def short_title_generator(title: str) -> str:
    '''
    Generates a short title from a full title.

    This function uses NLP techniques to generate a short title from a full
    title.

    For legislation, the program must determine whether there is an official
    short title. Official short titles are identified as such in the
    legislation, usually towards the beginning. The short title is typically
    preceded by the phrase "This Act may be cited as" or "This Act may be
    known as". The program will search for these phrases and return the
    following text as the short title.
    
    Where either the full title or the official short title contain four or
    more words, the program generates a short form title for subsequent
    citations.

    For case law, the McGill Guide outlines several rules that must be followed
    when generating a short title.
    '''