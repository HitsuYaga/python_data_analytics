class LogAlert(object):
    def __init__(self, start_timestamp, end_timestamp, count, full_log, type_log="alert_count"):
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp
        self.count = count
        self.full_log = full_log
        self.type_log = "alert_count" if type_log is None else type_log

    def json(self):
        return {
            "start_timestamp": self.start_timestamp,
            "end_timestamp": self.end_timestamp,
            "count": self.count,
            "full_log": self.full_log,
            "type_log": self.type_log
        }
