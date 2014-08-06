import smtplib
from email.mime.text import MIMEText
import configparser

class sendMail:

	def __init__(self):
		self.__cfg = configparser.ConfigParser()
		self.__cfg.read('config.ini')
		self.__key = 'MAIL'
		self.__loadEmailServerConfig()

	def __loadEmailServerConfig(self):
		self.__SERVER = self.__cfg[self.__key]['SERVER']
		self.__FROM = self.__cfg[self.__key]['FROM']
		self.__USER = self.__cfg[self.__key]['USER']
		self.__PASSWD = self.__cfg[self.__key]['PASSWD']

	def sendMail(self, to, subject, msg):
		mime = MIMEText(msg)
		mime['TO'] = to
		mime['FROM'] = self.__FROM
		mime['SUBJECT'] = subject
		server = smtplib.SMTP_SSL(self.__Server)
		server.login(self.__USER, self.__PASSWD)
		server.sendmail(self.__FROM, [to], mime.as_string())
		server.quit()
