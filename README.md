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

* `elasticsearch_clients`: Customize elasticsearch client configurations.
* `elasticsearch_alias`: Default Elasticsearch client alias in elasticsearch_clients. default "default"
* `elasticsearch_dest_alias`: Dest Elasticsearch client alias in elasticsearch_clients. default elasticsearch_alias


#### Examples
``` python
# cat fabfile.py
from fabric.api import env
from elasticsearch import Elasticsearch
from esfabric import tasks as es


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

### Running on AWS with IAM

``` python
# cat fabfile.py
from fabric.api import env
from elasticsearch import Elasticsearch
from elasticsearch import RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from esfabric import tasks as es

host = 'YOURHOST.us-east-1.es.amazonaws.com'
awsauth = AWS4Auth(YOUR_ACCESS_KEY, YOUR_SECRET_KEY, REGION, 'es')

env.elasticsearch_clients = {
    "default": Elasticsearch(**{
        "host": "YOURHOST.us-east-1.es.amazonaws.com",
        "port": 443,
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
