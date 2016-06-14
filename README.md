# es-tool

Elasticsearch tool written in Python

I was initially messing around with the API, and thought it'd be nice to create a tool to make my life a little easier when doing a few administration tasks.

## Installation

To use the tool you'll need to install it's dependencies.

	pip install -r requirements.txt

Currently I've only tested it works with Python 2.X


## Usage

	usage: es-tool.py [-h] [-r REINDEX] [-d DELETE_INDEX] -e ELASTICSEARCH

	Elasticsearch management

	optional arguments:
	  -h, --help            show this help message and exit
	  -r REINDEX, --reindex REINDEX
	                        Reindex specified index and append with "-reindex"
	  -d DELETE_INDEX, --delete_index DELETE_INDEX
	                        Specify which index to delete
	  -e ELASTICSEARCH, --elasticsearch ELASTICSEARCH
	                        Specify Elasticsearch host


### Example

If you wanted to reindex and index you can do this

	./es-tool.py --elasticsearch http://elasticsearch --reindex name-of-index

The tool will reindex the indices on the same cluster and append "-reindex" to the end e.g. *"name-of-index-reindex"*


## To do

* List indexes
* Dry-run **IMPORTANT**
* Ability to specify source and destination hosts