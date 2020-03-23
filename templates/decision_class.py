"""Decision class for storing and manipulating case data "offline"

Creates a template for valid CanLII decisions. Later versions should include the
ability to run reports straight from the class object.

URLs for cited cases do not need to be used in this class.

The class should be able to be built straight from the JSON data associated with
the decision
"""

class Decision:
    def __init__(self, decision_info, url, cited_cases):
        self.decision_info = decision_info
        self.url = url
        self.cited_cases = cited_cases

        pass
