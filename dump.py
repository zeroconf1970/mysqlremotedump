import configparser
import os.path
import datetime
import time
from subprocess import call
import shutil
import os

class dump:

	def __init__(self, path, cfile, mailer):
		self.__path = path
		self.__mailer = mailer
		self.__cfg = configparser.ConfigParser()
		self.__cfg.read(cfile)
		self.__def = 'DEFAULT'
		self.__mail = self.__cfg[self.__def]['MAIL']
		self.__TCPOSSH = int(self.__cfg[self.__def]['TCPOSSH'])
		self.__sshUser = self.__cfg[self.__def]['sshUser']
		self.__sshPasswd = self.__cfg[self.__def]['sshPasswd']
		self.__sshHost = self.__cfg[self.__def]['sshHost']
		self.__dbName = self.__cfg[self.__def]['dbName']
		self.__dbUser = self.__cfg[self.__def]['dbUser']
		self.__dbPasswd = self.__cfg[self.__def]['dbPasswd']
		self.__dbHost = self.__cfg[self.__def]['dbHost']
		self.__subject = 'Problem with %s' % (self.__sshHost)
		self.__checkPath()

	def __checkPath(self):
		if not(os.path.exists(os.path.join(self.__path, self.__sshHost))):
			os.makedirs(os.path.join(self.__path, self.__sshHost))

	def mainenance(self):
		pass

	def backup(self):
		if self.__TCPOSSH == 1:
			os.system('sshpass -p %s ssh %s@%s mysqldump -u %s --password="%s" -h %s %s > "%s"' % (self.__sshPasswd, self.__sshUser, self.__sshHost, self.__dbUser, self.__dbPasswd, self.__dbHost, self.__dbName, os.path.join(self.__path, self.__sshHost, datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H%M%S')+'.sql')))
		else:
			self.__mailer.sendMail(self.__mail, self.__subject, '[%s] No Protocol for Backup!' %( time.ctime()))
