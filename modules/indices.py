from elasticsearch import helpers


def delete(args, conn):
    # To delete an index specified
    index_to_remove = args.delete_index

    try:
        conn.indices.delete(index=index_to_remove)
        print("The index '{remove}' has been removed").format(remove=index_to_remove)
    except:
        print("Unable to delete the '{remove}' index").format(remove=index_to_remove)


def list_all(conn):
    try:
        for index in conn.indices.get('*'):
            print(index)
    except:
        print("Unable to list all indices")


def reindex(args, conn):
    # To reindex a specified index and appends the new index with "-reindexed" if the --new_index_name options has not been specified
    src_index_name = args.reindex

    if args.new_index_name is not None:
        des_index_name = args.new_index_name
    else:
        des_index_name = "{source}-reindexed".format(source=src_index_name)

    try:
        helpers.reindex(client=conn, source_index=src_index_name, target_index=des_index_name)
        print("'{source}' has been reindexed to '{dest}'").format(source=src_index_name, dest=des_index_name)
    except Exception as e:
        print(e)
        print("Unable to reindex '{source}'").format(source=src_index_name)
