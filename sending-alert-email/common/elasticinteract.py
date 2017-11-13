from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

# count = s.count()
# response = s[0:count].execute()
class ElasticAPI(object):

	@staticmethod
	def query(src_ip, timestamp):
		client = Elasticsearch([{"host":"222.255.102.149", "port":"9200"}])
		s = Search(using=client, doc_type="zimbra_doc") \
						.filter("term", typelog= "info") \
						.filter("term", src_ip_addr=src_ip) \
						.filter("term", unnormal_access= "false") \
						.filter("range", timestamp={"gte": str(int(timestamp)-86400), "lte": str(timestamp)}) \
						.sort('timestamp')
		
		response = s.execute()
		return response['hits']['hits']