from elasticsearch import Elasticsearch


def es(args):
    # Creates the connection with Elasticsearch
    conn = Elasticsearch(args.endpoint)
    return conn
