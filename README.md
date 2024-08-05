# legal-informatics

Extracts information from court decisions hosted on [CanLII](https://www.canlii.org/).

## Overview

This project consists of a collection of functions used to process legal information. CanLII is a free legal database that hosts court decisions and legislation from across Canada. As a Canadian legal practitioner, I use CanLII for all of my primary legal research. While this project is focused on informatics, creating, maintaining, and updating tools that improve CanLII's accessibilty and functionality is an intentional aspirational side-effect.

Version 0.1.0 of this project takes over at least two previous attempts to develop a similar toolset. Code from these projects is currently stored in a .legacy folder, and some of it will be incorporated into the new project. Two of the tools — Citator and Headnote — were eventually developed under separate repos (as [citation-generator] and [case-brief](), respectively) as a part of my work on the PDM program in 2022/23, and the rationale for this project fell by the wayside. 

But since the last work on this repo a few years ago, I developed a tool ([legal-citation-parser](https://github.com/646e62/legal-citation-parser)) to generate information from a CanLII citation, in tandem with the publicly available CanLII API. Several potential informatic insights became apparent when using it, so I've decided to revisit this project and refocus its scope.

The first version of this project introduces two very basic analytic functions: a tool that counts jurisdictions and court levels, and a tool that organizes citations by year. Although these are mostly proof of concept functions t, the data from each can be used to generate more complex insights. For example, the jurisdiction and court level data can be used to generate a report that shows how different courts read and cite one another, while annual data can be used to generate a report that shows a case's popularity over time.

This version migrates the code from the "master" branch to "main", as I'm not sure why I opted for the former name in the first place. Also, it's a new start to the project, so if I'm going to change the branch name, now is the time to do it.

## Version 0.1.0 features

* Moved legacy code to a legacy folder
* New project description and updates to the README
* No gods, no master branch — replaced "master" with "main" and deleted the former
* Removed and recreaded "dev"
* 

## Legacy code

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
