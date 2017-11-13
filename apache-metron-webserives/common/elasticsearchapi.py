from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


class ElasticsearchAPI(object):

    @staticmethod
    def queryWithTimestamp(index_name, timestamp):
        client = Elasticsearch([{"host": "222.255.102.149", "port": "9200"}])
        s = Search(using=client, doc_type=index_name + "_doc") \
            .filter("range", timestamp={"gte": str(int(timestamp) - 3600), "lte": str(timestamp)}) \
            .sort("timestamp")

        response = s.execute()
        return response['hits']['hits']
