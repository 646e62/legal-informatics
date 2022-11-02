# headnote_
Extracts information from written decisions in Canadian criminal cases. Currently, the tools generate a report of all of the decisions cited by a decision hosted on CanLII. 

## V 0.3.1
* Federal jurisdiction code now populates properly
* Removed "Reported" header from the standard report
* "Unreported" header only prints when applicable

## TODO

### Functionality
* Retrieve and cache full MHTML decisions for faster/future results
* Design and implement a Decision class
* Retrieve metadata through the CanLII API

### Refactoring
* Replace urllib (& json) with requests

### UX
* Package with FastAPI
