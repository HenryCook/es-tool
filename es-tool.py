#!/usr/bin/env python

import sys
import os
import argparse

current_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(current_path, "vendored"))

from elasticsearch import Elasticsearch, RequestsHttpConnection, helpers

def parse_args():
    parser = argparse.ArgumentParser(description='Elasticsearch management')
    parser.add_argument('-r', '--reindex', action='store', help='Reindex all documents in specified index and append with "-reindex", if --new_index_name options has not been specified')
    parser.add_argument('-n', '--new_index_name', action='store', help='Name for new index')
    parser.add_argument('-d', '--delete_index', action='store', help='Specify which index to delete from source ES')
    parser.add_argument('-S', '--source', action='store', help='Specify Elasticsearch host from which the data will be downloaded', required=False)
    parser.add_argument('-e', '--endpoint', action='store', help='Alias for --source for backward compatibility', required=False)
    parser.add_argument('-D', '--destination', action='store', help='Specify Elasticsearch host in which the data will be uploaded. If not specified, the --source connection will be used as destination.', required=False)
    parser.add_argument('-ps', '--port_source', action='store', help='Specify port for the source Elasticsearch (9200 by default, for AWS ES it can be 80 or 443).', required=False)
    parser.add_argument('-pd', '--port_destination', action='store', help='Specify port for the destination Elasticsearch (9200 by default, for AWS ES it can be 80 or 443).', required=False)
    parser.add_argument('-ls', '--ssl_source', action='store', help='Use SSL (https) connection for the source ElasticSearch.', required=False, default=False)
    parser.add_argument('-ld', '--ssl_destination', action='store', help='Use SSL (https) connection.', required=False, default=False)
    args = parser.parse_args()

    return args

def esSrc():
    """
    Creates the connection with Elasticsearch from which the data will be downloaded
    """
    args = parse_args()

    if not args.endpoint:
        host = args.source
    else:
        # backward compatibility
        host = args.endpoint
    if not host:
        raise Exception('error: argument -S/--source is required')

    conn = Elasticsearch(
        host,
        use_ssl=args.ssl_source in ['true', '1', 't', 'y', 'yes'],
        verify_certs=True,
        connection_class=RequestsHttpConnection,
        port=int(args.port_source)
    )

    return conn

def esDest():
    """
    Creates the connection with Elasticsearch in which the data will be uploaded
    """

    args = parse_args()

    if not args.destination:

        return None
    else:
        host = args.destination
        conn = Elasticsearch(
            host,
            use_ssl=args.ssl_destination in ['true', '1', 't', 'y', 'yes'],
            verify_certs=True,
            connection_class=RequestsHttpConnection,
            port=int(args.port_source)
        )

        return conn

def delete():
    """
    To delete an index specified
    """
    args = parse_args()

    conn = esSrc()
    index_to_remove = args.delete_index

    conn.indices.delete(index=index_to_remove)
    print(index_to_remove + "has been removed")


def reindex():
    """
    To reindex a specified index and appends the new index with "-reindex"
    if the --new_index_name options has not been specified
    """
    args = parse_args()

    src_index_name = args.reindex

    if args.new_index_name is not None:
        des_index_name = args.new_index_name
    else:
        des_index_name = src_index_name + "-reindex"

    helpers.reindex(esSrc(), src_index_name, des_index_name, None, esDest())
    print(src_index_name + " has been reindexed to " + des_index_name)


def main():
    args = parse_args()

    if args.delete_index:
        if raw_input('Are you sure to delete index "' + args.delete_index + '"? This operation cannot be reversed. (yes/no)').lower() in ('y', 'yes'):
            delete()
        else:
            print('Canceled')
    elif args.reindex:
        reindex()
    else:
        sys.exit()
    pass

if __name__ == '__main__':
    main()
