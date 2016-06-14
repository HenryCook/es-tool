# es-tool

Elasticsearch tool written in Python

I was initially messing around with the API, and thought it'd be nice to create a tool to make my life a little easier when doing a few administration tasks.

## Usage

	usage: es-tool.py [-h] [-r REINDEX] -e ELASTICSEARCH

	Elasticsearch management

	optional arguments:
	  -h, --help            show this help message and exit
	  -r REINDEX, --reindex REINDEX
	                        Reindex specified index and append with "-reindex"
	  -e ELASTICSEARCH, --elasticsearch ELASTICSEARCH
	                        Specify Elasticsearch host


## To do

* Remove old indexes
* List indexes
* Dry-run **IMPORTANT**
* Ability to specify source and destination hosts