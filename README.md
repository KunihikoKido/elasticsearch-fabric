# elasticsearch-fabric
This package provides a unified command line interface to Elasticsearch in Fabric.

## Installation
The current release, published on PyPI, can be installed using the following command:

```sh
$ pip install elasticsearch-fabric
```

## Configuration

### Tasks
If you plan to use the built-in tasks, include the module in your fabfile module (e.g. fabfile.py). Most likely you might want to assign an alias for the task namespace:

``` python
from esfabric import tasks as es
```

### Environment

* `elasticsearch_clients`: Customize elasticsearch client configurations.
* `elasticsearch_alias`: Default Elasticsearch client alias in elasticsearch_clients. default "default"
* `elasticsearch_dest_alias`: Reindex dest Elasticsearch client alias in elasticsearch_clients. default elasticsearch_alias


#### Examples
``` python
# cat fabfile.py
from fabric.api import env
from elasticsearch import Elasticsearch
from esfabric import tasks as es


env.elasticsearch_clients = {
    "default": Elasticsearch(**{
        "host": "localhost",
        "port": 9200,
        "send_get_body_as": "POST"
    }),
    "example": Elasticsearch(**{
        "host": "search.example.org",
        "port": 443,
        "send_get_body_as": "POST",
        "use_ssl": True,
        "verify_certs": True
    })
}
```

### Elasticsearch with Shield
You can configure the client to use basic authentication:

``` python
# cat fabfile.py
from fabric.api import env
from elasticsearch import Elasticsearch
from esfabric import tasks as es


env.elasticsearch_clients = {
    "default": Elasticsearch(**{
      "host": "localhost",
      "port": 9200,
      "send_get_body_as": "POST",
      "http_auth": ('user', 'secret')
    })
}
```

### Running on AWS with IAM

``` python
# cat fabfile.py
from fabric.api import env
from elasticsearch import Elasticsearch
from elasticsearch import RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from esfabric import tasks as es

awsauth = AWS4Auth(YOUR_ACCESS_KEY, YOUR_SECRET_KEY, REGION, 'es')

env.elasticsearch_clients = {
    "default": Elasticsearch(**{
        "host": "YOURHOST.us-east-1.es.amazonaws.com",
        "port": 443,
        "send_get_body_as": "POST",
        "http_auth": awsauth,
        "use_ssl": True,
        "verify_certs": True,
        "connection_class": RequestsHttpConnection
    })
}
```

## Checking the setup
For checking if everything is set up properly, you can run the included task *info*. For example, running

``` sh
$ fab es.info
```
you can show a similar result:

```sh
{
  "cluster_name": "elasticsearch",
  "tagline": "You Know, for Search",
  "version": {
    "lucene_version": "5.5.0",
    "build_hash": "218bdf10790eef486ff2c41a3df5cfa32dadcfde",
    "number": "2.3.3",
    "build_timestamp": "2016-05-17T15:40:04Z",
    "build_snapshot": false
  },
  "name": "Ares"
}


Done.
```

## Basic Usage
You can do this for example with the following command:

*Example 1: Search*
``` sh
# curl -XGET 'http://localhost:9200/_search?pretty' -d ''
$ fab es.search
```

*Example 2: Index & Docment Type*
``` sh
# curl -XGET 'http://localhost:9200/blog/posts/_search?pretty' -d ''
$ fab es.search:blog,posts
```

*Example 3: Request simple search*
``` sh
# curl -XGET 'http://localhost:9200/blog/posts/_search?pretty&q=Hello+Elasticsearch' -d ''
$ fab es.search:blog,posts,q="Hello Elasticsearch"
```

*Example 4: Request body search*
``` sh
# curl -XPOST 'http://localhost:9200/blog/posts/_search?pretty' -d '{
#   "query": {
#     "match_all": {}
#   }
# }'
$ cat query.json
{
  "query": {"match_all": {}}
}

$ cat query.json | fab es,search:blog,posts
```

## Command help

``` sh
$ fab es.search:help=true
```

## Client selection

``` python
# fabfile.py
from esfabric import tasks as es
from esfabric.tasks import client_selection

env.elasticsearch_clients = {
    "client1": Elasticsearch(**{
      ...
    }),
    "client2": Elasticsearch(**{
      ...
    })
}
```

``` sh
$ fab c:client2 es.info
```

`c` is client_selection alias

## Custom Task

``` python
from esfabric import tasks as es
from fabric.api import execute, task


@task
def change_replicas(number_of_replicas=1):
    execute(es.cat.indices, v=1)
    execute(es.helpers.change_replicas, number_of_replicas)
    execute(es.cat.indices, v=1)
```

``` sh
$ fab change_replicas:10
```

1. Show number of replicas
2. Change number of replicas 10
3. Show number of replicas

## Available commands
The following command will show a list of avaliable commands.

``` sh
$ fab -l
```

* Available commands
  * es.bulk
  * es.c
  * es.clear_scroll
  * es.client_selection
  * es.count
  * es.count_percolate
  * es.create
  * es.delete
  * es.delete_by_query
  * es.delete_script
  * es.delete_template
  * es.exists
  * es.explain
  * es.field_stats
  * es.get
  * es.get_script
  * es.get_source
  * es.get_template
  * es.index
  * es.info
  * es.mget
  * es.mpercolate
  * es.msearch
  * es.msearch_template
  * es.mtermvectors
  * es.percolate
  * es.ping
  * es.put_script
  * es.put_template
  * es.reindex
  * es.reindex_rethrottle
  * es.render_search_template
  * es.scroll
  * es.search
  * es.search_shards
  * es.search_template
  * es.suggest
  * es.termvectors
  * es.update
  * es.update_by_query
  * es.cat.aliases
  * es.cat.allocation
  * es.cat.count
  * es.cat.fielddata
  * es.cat.health
  * es.cat.indices
  * es.cat.master
  * es.cat.nodeattrs
  * es.cat.nodes
  * es.cat.pending_tasks
  * es.cat.plugins
  * es.cat.recovery
  * es.cat.repositories
  * es.cat.segments
  * es.cat.shards
  * es.cat.snapshots
  * es.cat.thread_pool
  * es.cluster.allocation_explain
  * es.cluster.get_settings
  * es.cluster.health
  * es.cluster.pending_tasks
  * es.cluster.put_settings
  * es.cluster.reroute
  * es.cluster.state
  * es.cluster.stats
  * es.helpers.bulk
  * es.helpers.change_replicas
  * es.helpers.reindex
  * es.helpers.scan
  * es.indices.analyze
  * es.indices.clear_cache
  * es.indices.close
  * es.indices.create
  * es.indices.delete
  * es.indices.delete_alias
  * es.indices.delete_template
  * es.indices.exists
  * es.indices.exists_alias
  * es.indices.exists_template
  * es.indices.exists_type
  * es.indices.flush
  * es.indices.flush_synced
  * es.indices.forcemerge
  * es.indices.get
  * es.indices.get_alias
  * es.indices.get_field_mapping
  * es.indices.get_mapping
  * es.indices.get_settings
  * es.indices.get_template
  * es.indices.get_upgrade
  * es.indices.open
  * es.indices.put_alias
  * es.indices.put_mapping
  * es.indices.put_settings
  * es.indices.put_template
  * es.indices.recovery
  * es.indices.refresh
  * es.indices.rollover
  * es.indices.segments
  * es.indices.shard_stores
  * es.indices.shrink
  * es.indices.stats
  * es.indices.update_aliases
  * es.indices.upgrade
  * es.indices.validate_query
  * es.nodes.hot_threads
  * es.nodes.info
  * es.nodes.stats
