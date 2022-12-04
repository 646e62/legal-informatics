# legal-informatics

Extracts information from written decisions in Canadian criminal cases.

## Version history

### V 0.4.0

* Renamed the repo "informatics" to reflect the project's broader scope
* Identified three separate projects:
  * CanLII data processor
  * Citator
  * Headnote
* Added a wiki

#### CanLII data processor

* Moved all of the old data processing tools to a legacy folder
  * Added the lone function from json_tools.py to api_call_tools.py and deleted
  the redundant file
* Future versions will be built around the new canlii_decision_* toolset
* Legacy programs have a few CanLII API-specific functions that should be 
useful for other programs going forward

#### Citator

* Created SK Decision, Legislation, and SecondarySources classes based on the
[2015 Citation Guide](https://sasklawcourts.ca/wp-contentuploads/2020/09/Citation_Guide_2015_revisions.pdf)
* Started to codify the SK Citation Guide rule set

### V 0.3.2

* Download and cache documents from CanLII through the
canlii_decision_retriever script using the requests library
* Extract text and itemize paragaphs using the canlii_decision_extractor script

### V 0.3.1

* Federal jurisdiction code now populates properly
* Removed "Reported" header from the standard report
* "Unreported" header only prints when applicable

## TODO

### Functionality

* Design and implement a Decision class
* Retrieve metadata through the CanLII API
  * The legacy tools should be able to accomplish this

### UX

* Make some design decisions
