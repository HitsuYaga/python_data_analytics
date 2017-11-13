# Define class log alert and method print log alert
class LogAlert(object):
	def __init__(self, start_timestamp, end_timestamp, ip, count, full_log, type_log="alert_count"):
		self.start_timestamp = start_timestamp
		self.end_timestamp = end_timestamp
		self.ip = ip
		self.count = count
		self.full_log = full_log
		self.type_log = "alert_count" if type_log is None else type_log
	
	def json(self):
		return {
			"start_timestamp": self.start_timestamp,
			"end_timestamp": self.end_timestamp,
			"ip": self.ip,
			"count": self.count,
			"full_log": self.full_log,
			"type_log": self.type_log
		}