import smtplib
import config as CONFIG

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from models.log_alert.log_alert import LogAlert

class Ultis(object):

  @staticmethod
  def initializeEmail(fromaddr=CONFIG.MAIL_DEFAULT_SENDER, toaddr=CONFIG.MAIL_DEFAULT_RECEIVER):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "SIMN Apache Metron Alert Log"
    return msg
  
  @staticmethod
  def createBodyEmail(logs_alert):
    return  """\
            <html>
            <head></head>
            <body>
            <p>I found some unnormal access with your IP: """ + logs_alert['ip']  + """<br>
            <br>Start_timestam: """ + str(logs_alert['start_timestamp']) + """<br>
            <br>End_timestam: """ + str(logs_alert['end_timestamp']) + """<br>
            <br>Count: """ + str(logs_alert['count']) + """<br>
            <br>Full_log: <br>
            <ul>
              <li>""" + str(logs_alert['full_log']) + """</li>
            </ul>
            </body>
            </html>
            """

  @staticmethod
  def sendingEmailAlert(msg, body,
                        mailServerIP=CONFIG.SERVER_MAIL_DEFAULT['IP'],
                        mailServerPort=CONFIG.SERVER_MAIL_DEFAULT['PORT'],
                        loginName=CONFIG.SERVER_MAIL_DEFAULT['USER_LOGON'],
                        loginPassword=CONFIG.SERVER_MAIL_DEFAULT['PASSWORD_LOGON']
                        ):
    msg.attach(MIMEText(body, 'html'))
    server = smtplib.SMTP(mailServerIP, int(mailServerPort))
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(loginName, loginPassword)
    text = msg.as_string()
    server.sendmail(msg['From'], msg['To'], text)

  @staticmethod
  def createLogAlert(results):
    start_timestamp = results[0]['_source']['timestamp']
    end_timestamp = results[-1]['_source']['timestamp']
    src_ip = results[0]['_source']['src_ip_addr']
    count = len(results)
    full_log = []

    if len(results) < 4:
      for hit in results:
        message_origin = hit['_source']['original_string']
        full_log.append(message_origin)
    else:
      for hit in results:
        message_origin = hit['_source']['original_string']
        if results.index(hit) <= 1 or (len(results) - results.index(hit) <= 2):
          full_log.append(message_origin)
    
    return LogAlert(start_timestamp, end_timestamp, src_ip, count, full_log).json()
