"""
Query Elasticsearch and send email alert if detect alert log.
"""
import time
from common.ultis import Ultis
from common.elasticinteract import ElasticAPI

current_time = int(time.time()) + 7*3600
src_ip = "0.0.0.0"

results = ElasticAPI.query(src_ip, current_time)

if len(results) == 0:
  print "No found any alert log"
else:
  logs_alert = Ultis.createLogAlert(results)
  body = Ultis.createBodyEmail(logs_alert)
  msg = Ultis.initializeEmail()
  Ultis.sendingEmailAlert(msg,body)