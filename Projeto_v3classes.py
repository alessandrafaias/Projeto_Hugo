import sys
import pyodbc
import json


class dbHandle:
#O módulo init está iniciando o arquivo params
	def __init__(self,param_file):
		self.param_file = param_file
		self.params = {}
		self.startParams()

#Abre o arquivo params como arquivo json
	def startParams(self):
		params = {}
		with open(self.param_file) as json_file:
			self.params = json.load(json_file)		
		return True

#Retorna o arquivo params
	def getParams(self):
		return self.params
		
#Conexão com o SQL Server
	def doQuery(self,cmd):
		params = self.getParams()
		#print('Driver={SQL Server};'+'Server='+params['server']+';'+'Database='+params['database']+';'+'Trusted_Connection=yes;')
		cnxn = pyodbc.connect('Driver={SQL Server};'
			'Server='+params['server']+';'
			'Database='+params['database']+';'
			'Trusted_Connection=yes;')
		cursor = cnxn.cursor()	
		for co in cmd:
			print(co)
			cursor.execute(co)
			for linha in cursor:
				print(linha)
		cnxn.commit()



