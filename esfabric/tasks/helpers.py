# coding=utf-8
import sys
import json
from fabric.api import *
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from .utils import jsonprint
from .utils import get_client


IGNORE = [400, 401, 404, 500]

@task
def change_replicas(index=None, number_of_replicas=1, **kwargs):
    """change_replicas(index=None, number_of_replicas=1, **kwargs)"""
    if "help" in kwargs.keys():
        return help(change_replicas)
    es = get_client(env.elasticsearch_alias)
    body = {"index": {"number_of_replicas": number_of_replicas}}
    res = es.indices.put_settings(body, index=index, ignore=IGNORE, **kwargs)
    jsonprint(res)
    return res

@task
def scan(index=None, doc_type=None, outfile="dump.txt", **kwargs):
    """scan(index=None, doc_type=None, outfile="dump.txt", **kwargs)"""
    if "help" in kwargs.keys():
        return help(scan)

    es = get_client(env.elasticsearch_alias)
    docs = helpers.scan(es, index=index, doc_type=doc_type, ignore=IGNORE, **kwargs)

    success = 0
    with open(outfile, "w") as f:
        for doc in docs:
            f.write(json.dumps(doc, ensure_ascii=False).encode("utf-8"))
            f.write("\n")
            success += 1

    res = {
        "success": success,
        "scan": {
            "host": es.transport.get_connection().host,
            "index": index,
            "doc_type": doc_type,
            "outfile": outfile
        }
    }
    jsonprint(res)
    return res

@task
def bulk(infile="dump.txt", **kwargs):
    """bulk(infile="dump.txt", **kwargs)"""
    if "help" in kwargs.keys():
        return help(bulk)

    try:
        with open(infile, "r") as f:
            actions = []
            indices = {}
            for line in f:
                doc = json.loads(line)
                actions.append(doc)
                index = doc["_index"]
                indices[index] = 1 + indices.get(index, 0)
    except Exception as e:
        abort(e)

    es = get_client(env.elasticsearch_alias)
    success, errors = helpers.bulk(es, actions, ignore=IGNORE, **kwargs)

    res = {
        "success": success, "errors": errors,
        "bulk": {
            "host": es.transport.get_connection().host,
            "indices": indices
        }
    }
    jsonprint(res)
    return res

@task
def reindex(source_index=None, dest_index=None, chunk_size=500, **kwargs):
    """reindex(source_index=None, dest_index=None, chunk_size=500, **kwargs)"""
    if "help" in kwargs.keys():
        return help(reindex)

    source_es = get_client(env.elasticsearch_alias)
    dest_es = get_client(env.elasticsearch_dest_alias)
    dest_index = dest_index or source_index

    try:
        success, errors = helpers.reindex(source_es, source_index=source_index,
            target_client=dest_es, target_index=dest_index,
            chunk_size=chunk_size, **kwargs)
    except Exception as e:
        abort(e)

    res = {
        "success": success, "errors": errors,
        "source": {
            "host": source_es.transport.get_connection().host,
            "index": source_index
        },
        "dest": {
            "host": dest_es.transport.get_connection().host,
            "index": dest_index
        }
    }
    jsonprint(res)
    return res
