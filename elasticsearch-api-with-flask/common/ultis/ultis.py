import re
import json
from models.log_alert.log_alert import LogAlert

class Ultis(object):
  
  @staticmethod
  def summarizeLog(src_ip, results):
    count = 0
    full_log = []
    logs_alert = []
    start_timestamp = results[0]['_source']['timestamp']

    for hit in results:
      timestamp = hit['_source']['timestamp']
      message_origin = hit['_source']['original_string']
			
      if (timestamp - start_timestamp) <= 2 and (timestamp - start_timestamp) >= 0:
        count = count + 1
        end_timestamp = timestamp
        full_log.append(message_origin)
				
      else:
        log_alert = LogAlert(start_timestamp, end_timestamp, src_ip, count, full_log).json()
        logs_alert.append(log_alert.copy())
        count = 1
        full_log = []
        start_timestamp = timestamp;
        end_timestamp = timestamp;
        full_log.append(message_origin)
			
      if results.index(hit) == len(results) - 1:
        log_alert = LogAlert(start_timestamp, end_timestamp, src_ip, count, full_log).json()
        logs_alert.append(log_alert.copy())

    return logs_alert
