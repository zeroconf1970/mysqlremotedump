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
		self.__bpath = os.path.join(self.__path, self.__sshHost)
		self.__checkPath()

	def __checkPath(self):
		if not(os.path.exists(self.__bpath)):
			os.makedirs(self.__bpath)

	def maintenance(self):
		ts = time.time()
		ts = ts - 15552000
		ts = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d')
		dirlist = os.listdir(self.__bpath)
		oplist = []
		for i in dirlist:
			oplist.append((int((i.split('_')[0]).replace('-','')), i))
		for i in oplist:
			if i[0]<int(ts):
				os.remove(os.path.join(self.__bpath, i[1]))
		
	def backup(self):
		if self.__TCPOSSH == 1:
			os.system('sshpass -p %s ssh %s@%s mysqldump -u %s --password="%s" -h %s %s > "%s"' % (self.__sshPasswd, self.__sshUser, self.__sshHost, self.__dbUser, self.__dbPasswd, self.__dbHost, self.__dbName, os.path.join(self.__bpath, datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H%M%S')+'.sql')))
		else:
			self.__mailer.sendMail(self.__mail, self.__subject, '[%s] No Protocol for Backup!' %( time.ctime()))
