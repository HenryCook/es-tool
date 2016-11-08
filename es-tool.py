#!/usr/bin/env python

import argparse
import sys

import modules.connection as connection
import modules.indices as indices


def parse_args():
    parser = argparse.ArgumentParser(description='Elasticsearch management')
    parser.add_argument('-r', '--reindex', action='store', help='Reindex all documents in specified index and append with "-reindexed", if --new_index_name options has not been specified')
    parser.add_argument('-n', '--new_index_name', action='store', help='Name for new index')
    parser.add_argument('-d', '--delete_index', action='store', help='Specify which index to delete')
    parser.add_argument('-e', '--endpoint', action='store', help='Specify Elasticsearch host', required=True)
    parser.add_argument('-l', '--list-all-indices', action='store_true', help='Lists all indices from Elasticsearch cluster')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    conn = connection.es(args)
    if conn:
        pass
    else:
        print('Failed to connect to ES cluster')
        sys.exit(2)

    if args.list_all_indices:
        indices.list_all(conn)
    elif args.delete_index:
        indices.delete(args, conn)
    elif args.reindex:
        indices.reindex(args, conn)
    else:
        sys.exit()
    pass


if __name__ == "__main__":
    main()
