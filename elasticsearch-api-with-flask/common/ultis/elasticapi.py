from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

class ElasticAPIInteract(object):

  @staticmethod
  def queryWithIPandTimestamp(src_ip, timestamp):
    client = Elasticsearch([{"host":"222.255.102.149", "port":"9200"}])
    s = Search(using=client, doc_type="zimbra_doc") \
            .filter("term", src_ip_addr= str(src_ip)) \
            .filter("term", typelog= "info") \
            .filter("range", timestamp={"gte": str(int(timestamp)-3600), "lte": str(timestamp)}) \
            .sort("timestamp")

    response = s.execute()
    return response['hits']['hits']