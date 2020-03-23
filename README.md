# canlii_data_miner
Generates a report of all of the decisions cited by a decision hosted on
CanLII. Accepts a valid CanLII URL as input.

## V 0.3.1
* Federal jurisdiction code now populates properly
* Removed "Reported" header from the standard report
* "Unreported" header only prints when applicable

## TODO
* Cache results "offline" for faster/future results
* Replace urllib (& json) with requests
* Design and implement a Decision class
* Write a metadata API call
