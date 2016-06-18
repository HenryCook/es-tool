#!/usr/local/bin/python

from elasticsearch import Elasticsearch
from elasticsearch import helpers
import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description='Elasticsearch management')
    parser.add_argument('-r', '--reindex', action='store', help='Reindex specified index and append with "-reindex"')
    parser.add_argument('-d', '--delete_index', action='store', help='Specify which index to delete')
    parser.add_argument('-e', '--endpoint', action='store', help='Specify Elasticsearch host', required=True)
    args = parser.parse_args()
    return args


def es():
    # Creates the connection with Elasticsearch
    args = parse_args()

    host = args.endpoint
    conn = Elasticsearch(host)

    return conn


def delete():
    # To delete an index specified
    args = parse_args()

    conn = es()
    index_to_remove = args.delete_index

    conn.indices.delete(index=index_to_remove)
    print(index_to_remove + "has been removed")


def reindex():
    # To reindex a specified index and appends the new index with "-reindex"
    args = parse_args()

    src_index_name = args.reindex
    des_index_name = src_index_name + "-reindex"

    helpers.reindex(es(), src_index_name, des_index_name)
    print(src_index_name + " has been reindexed to " + des_index_name)


def main():
    args = parse_args()

    if args.delete_index:
        delete()
    elif args.reindex:
        reindex()
    else:
        sys.exit()
    pass



if __name__ == '__main__':
    main()