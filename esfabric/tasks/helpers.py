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
    es = get_client(env.elasticsearch_alias)
    body = {"index": {"number_of_replicas": number_of_replicas}}
    res = es.indices.put_settings(body, index=index, ignore=IGNORE, **kwargs)
    jsonprint(res)
    return res

@task
def scan(index=None, doc_type=None, **kwargs):
    es = get_client(env.elasticsearch_alias)
    docs = helpers.scan(es, index=index, doc_type=doc_type, ignore=IGNORE, **kwargs)
    for doc in docs:
        jsonprint(doc)

from .utils import stdin_body

@task
def bulk(chunk_size=100, filepath=None, **kwargs):
    if sys.stdin.isatty() is False:
        infile = sys.stdin
    elif filepath is not None:
        infile = open(filepath, "r")
    else:
        abort(bulk.__doc__)

    es = get_client(env.elasticsearch_alias)
    actions = []
    for action in infile.readlines():
        actions.append(json.loads(action))

    success, errors = helpers.bulk(es, actions, ignore=IGNORE, **kwargs)
    res = {
        "success": success, "errors": errors,
        "bulk": {
            "host": es.transport.get_connection().host
        }
    }
    infile.close()

    jsonprint(res)
    return res

@task
def reindex(source_index=None, dest_index=None, chunk_size=500, **kwargs):
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
