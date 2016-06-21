# es-tool

An [Elasticsearch](https://www.elastic.co/products/elasticsearch) tool written in Python.

`es-tool.py` utilises the [elasticsearch-py](http://elasticsearch-py.readthedocs.io/en/master/) client, that in turn
  interacts with Elasticsearch via it's API.

> Official low-level client for Elasticsearch. Its goal is to provide common ground for all Elasticsearch-related code in Python; because of this it tries to be opinion-free and very extendable.


Table of Contents
=================

  * [es\-tool](#es-tool)
    * [Reason](#reason)
    * [Installation](#installation)
    * [Usage](#usage)
      * [Example](#example)
    * [To do](#to-do)


## Reason

After moving over to [AWS Elasticsearch service](https://aws.amazon.com/elasticsearch-service/), I realised the amount of active shards was increasing by stupid amounts per day. After some reading I had found that by default ES assigns `5 primary shards` and `1 replica shard` meaning each indices was creating 10 shards.

AWS ES service doesn't allow for you to specify the number of shards via `elasticsearch.yaml` or a `GET /_cluster/settings` method, it can only be done via [index templates](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-templates.html). This then means as opposed to specifying your number of shards per cluster, it's done per index.

Rather annoyingly, at the time of writing this the AWS ES version is `1.5.2` which means I couldn't use the [Reindex API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-reindex.html), or use logstash as there is no amazon_es input only [output](https://github.com/awslabs/logstash-output-amazon_es). 

I was initially messing around with the API, and thought it'd be nice to create a tool to make my life a little easier when doing a few administration tasks (like reindexing).


## Installation

To use the tool you'll need to install it's dependencies.

	pip install -r requirements.txt

Currently I've only tested it with Python 2.X


## Usage

	usage: es-tool.py [-h] [-r REINDEX] [-n NEW_INDEX_NAME] [-d DELETE_INDEX] -e
                  ENDPOINT

	Elasticsearch management

	optional arguments:
	  -h, --help            show this help message and exit
	  -r REINDEX, --reindex REINDEX
	                        Reindex specified index and append with "-reindex", if
	                        -d option has not been used
	  -n NEW_INDEX_NAME, --new_index_name NEW_INDEX_NAME
	                        Name for Reindexed index
	  -d DELETE_INDEX, --delete_index DELETE_INDEX
	                        Specify which index to delete
	  -e ENDPOINT, --endpoint ENDPOINT
	                        Specify Elasticsearch host


### Example

If you wanted to reindex an index you can do this:

	./es-tool.py --elasticsearch http://elasticsearch --reindex name-of-index

The tool will reindex the indices on the same cluster and append "-reindex" to the end e.g. *"name-of-index-reindex"*


## To do

* List indexes
* Dry-run
* Ability to specify source and destination hosts
* Fix SSL Whining
* Improve logging/messages