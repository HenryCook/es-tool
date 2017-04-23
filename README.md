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

	pip install -t vendored/ -r requirements.txt

Currently I've only tested it with Python 2.X


## Usage

    usage: es-tool.py [-h] [-r REINDEX] [-n NEW_INDEX_NAME] [-d DELETE_INDEX]
                      [-S SOURCE] [-e ENDPOINT] [-D DESTINATION] [-ps PORT_SOURCE]
                      [-pd PORT_DESTINATION] [-ls SSL_SOURCE]
                      [-ld SSL_DESTINATION]

    Elasticsearch management

    optional arguments:
      -h, --help            show this help message and exit
      -r REINDEX, --reindex REINDEX
                            Reindex all documents in specified index and append
                            with "-reindex", if --new_index_name options has not
                            been specified
      -n NEW_INDEX_NAME, --new_index_name NEW_INDEX_NAME
                            Name for new index
      -d DELETE_INDEX, --delete_index DELETE_INDEX
                            Specify which index to delete from source ES
      -S SOURCE, --source SOURCE
                            Specify Elasticsearch host from which the data will be
                            downloaded
      -e ENDPOINT, --endpoint ENDPOINT
                            Alias for --source for backward compatibility
      -D DESTINATION, --destination DESTINATION
                            Specify Elasticsearch host in which the data will be
                            uploaded. If not specified, the --source connection
                            will be used as destination.
      -ps PORT_SOURCE, --port_source PORT_SOURCE
                            Specify port for the source Elasticsearch (9200 by
                            default, for AWS ES it can be 80 or 443).
      -pd PORT_DESTINATION, --port_destination PORT_DESTINATION
                            Specify port for the destination Elasticsearch (9200
                            by default, for AWS ES it can be 80 or 443).
      -ls SSL_SOURCE, --ssl_source SSL_SOURCE
                            Use SSL (https) connection for the source
                            ElasticSearch.
      -ld SSL_DESTINATION, --ssl_destination SSL_DESTINATION
                            Use SSL (https) connection.


### Reindex inside one cluster

If you wanted to reindex an index you can do this:

	./es-tool.py \
        --source elasticsearch-host \
        --reindex name-of-index \
        --new_index_name name-of-new-index \
        --ssl_source true \
        --port_source 443

The tool will reindex the indices on the same cluster and append "-reindex" to the end e.g. *"name-of-index-reindex"*

### Reindex from one cluster to another one

    ./es-tool.py \
        --source elasticsearch-host-1 \
        --destination elasticsearch-host-2 \
        --reindex name-of-index \
        --new_index_name name-of-new-index \
        --ssl_source true \
        --port_source 443 \
        --ssl_destination true \
        --port_destination 443

## To do

* List indexes
* Dry-run
* Improve logging/messages
* **Refactor into a module fashion like my hubot-scripts implementation**
