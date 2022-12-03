# headnote_

Extracts information from written decisions in Canadian criminal cases.

## V 0.3.2

* Download and cache documents from CanLII through the
canlii_decision_retriever script using the requests library
* Extract text and itemize paragaphs using the canlii_decision_extractor script

## V 0.3.1

* Federal jurisdiction code now populates properly
* Removed "Reported" header from the standard report
* "Unreported" header only prints when applicable

## TODO

### Functionality

* Design and implement a Decision class
* Retrieve metadata through the CanLII API

### UX

* Package with FastAPI
