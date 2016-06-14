#!/usr/local/bin/python

from elasticsearch import Elasticsearch
from elasticsearch import helpers
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Elasticsearch management')
    parser.add_argument('-r', '--reindex', action='store', help='Reindex specified index and append with "-reindex"')
    parser.add_argument('-e', '--elasticsearch', action='store', help='Specify Elasticsearch host', required=True)
    args = parser.parse_args()
    return args


def host():
    args = parse_args()

    host = args.elasticsearch
    return host


def main():
    args = parse_args()

    es = Elasticsearch(host())
    src_index_name = args.reindex
    des_index_name = src_index_name + "-reindex"

    helpers.reindex(es, src_index_name, des_index_name)


if __name__ == '__main__':
    main()