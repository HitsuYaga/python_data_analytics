import requests
import json

from flask import session

import config as CONFIG


class MetronAPI(object):

    @staticmethod
    def query_config(type_config, name_config):
        auth = (session['username'], session['password'])
        if type_config == "grok pattern":
            payload = {'path': '/apps/metron/patterns/' + name_config}
            result = requests.get(
                CONFIG.DEFAULT_API_METRON + '/api/v1/hdfs', params=payload, auth=auth)
            return result.text

        elif type_config == "global":
            result = requests.get(
                CONFIG.DEFAULT_API_METRON + '/api/v1/global/config', auth=auth).json()
            return json.dumps(result, indent=4, sort_keys=True)

        elif type_config == "kafka topic":
            result = requests.get(
                CONFIG.DEFAULT_API_METRON + '/api/v1/kafka/topic/' + name_config, auth=auth).json()
            return json.dumps(result, indent=4, sort_keys=True)

        else:
            result = requests.get(CONFIG.DEFAULT_API_METRON + '/api/v1/sensor/' +
                                  type_config + '/config/' + name_config, auth=auth).json()
            return json.dumps(result, indent=4, sort_keys=True)

    @staticmethod
    def create_config(type_config, name_config, config_data):
		auth = (session['username'], session['password'])
		headers = {'content-type': 'application/json'}
		if (type_config == "grok pattern"):
			payload = config_data
			params = {'path': "/apps/metron/patterns/" + name_config}
			result = requests.post(CONFIG.DEFAULT_API_METRON + "/api/v1/hdfs", auth=auth
																			, data=payload
																			, params=params
																			, headers=headers)
			return result.status_code

		elif (type_config == "kafka topic"):
			payload = config_data
			result = requests.post(CONFIG.DEFAULT_API_METRON + "/api/v1/kafka/topic", auth=auth
																					, data=payload
																					, headers=headers)
			return result.status_code

		elif (type_config == "topology"):
			result = requests.get(CONFIG.DEFAULT_API_METRON + "/api/v1/storm/parser/start/" +
									name_config, auth=auth, headers=headers)
			result = json.loads(result.content)
			if result['status'] != "ERROR":
				return 200

		else:
			payload = config_data
			result = requests.post(CONFIG.DEFAULT_API_METRON + "/api/v1/sensor/" + type_config +
									"/config/" + name_config, auth=auth, data=payload, headers=headers)
			return result.status_code

    @staticmethod
    def delete_config(type_config, name_config):
		auth = (session['username'], session['password'])
		if (type_config == "grok pattern"):
			params = {
				'path': "/apps/metron/patterns/" + name_config,
				'recursive': 'false'
			}
			result = requests.delete(
				CONFIG.DEFAULT_API_METRON + '/api/v1/hdfs', auth=('metron', 'simn_metron'), params=params)
			return result.status_code

		elif (type_config == "kafka topic"):
			result = requests.delete(
				CONFIG.DEFAULT_API_METRON + '/api/v1/kafka/topic/' + name_config, auth=('metron', 'simn_metron'))
			return result.status_code

		elif (type_config == "topology"):
			result = requests.get(
				CONFIG.DEFAULT_API_METRON + '/api/v1/storm/parser/stop/' + name_config, auth=('metron', 'simn_metron'))
			return result.status_code

		else:
			result = requests.delete(CONFIG.DEFAULT_API_METRON + '/api/v1/sensor/' +
										type_config + '/config/' + name_config, auth=('metron', 'simn_metron'))
			return result.status_code

    @staticmethod
    def test_topology(topic_name, sample_data):
		auth = (session['username'], session['password'])
		payload = sample_data
		result = requests.post(CONFIG.DEFAULT_API_METRON + "/api/v1/kafka/topic/" + topic_name + "/produce", auth=auth
																											, data=payload)
		return result.status_code
