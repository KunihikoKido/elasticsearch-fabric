# elasticsearch-fabric
This package provides a unified command line interface to Elasticsearch in Fabric.

## Installation
The current release, published on GitHub, can be installed using the following command:

```sh
$ pip install git+https://github.com/KunihikoKido/elasticsearch-fabric.git
```

## Configuration

### Tasks
If you plan to use the built-in tasks, include the module in your fabfile module (e.g. fabfile.py). Most likely you might want to assign an alias for the task namespace:

``` python
from esfabric import tasks as es
```

### Environment

- `elasticsearch_clients`: Multi elasticsearch client configurations.


``` python
# cat fabfile.py
from elasticsearch import Elasticsearch
from esfabric import tasks as es
from esfabric.tasks.utils import server_selection
from fabric.api import env


env.elasticsearch_clients = {
    "default": Elasticsearch(**{
        "host": "localhost",
        "port": 9200
    }),
    "prod": Elasticsearch(**{
        "host": "search.example.org",
        "port": 443,
        "use_ssl": True,
        "verify_certs": True
    })
}
```

## Checking the setup

``` sh
$ fab es.version
```


```sh
$ fab es.info
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
