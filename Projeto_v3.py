import sys
import pyodbc
import json
from Projeto_v3classes import dbHandle
#Testa o primeiro argumento: o reconhecimento do banco de dados
try:
    if sys.argv[1]=="":		#Se o conteúdo for vazio aparecerá uma mensagem de erro
        print("No param file seted")
        sys.exit(-1)
except:
    print("No param file seted")	#Se não houver o parâmetro aparecerá uma mensagem de erro
    sys.exit(-1)
#Envia os parâmetros da conexão com o banco para a classe, e armazena o retorno da conexão na variável ob
ob = dbHandle(sys.argv[1])	##Envia parâmetros para a classe e armazena a saída da classe na variável ob
#Testa o segundo argumento: a consulta
try:
	f = open(sys.argv[2],'r')	##Abre o arquivo e lê o conteúdo do arquivo
	conteudo = f.read()		##Guarda dentro da variável f o conteúdo do arquivo
	f.close()	##Fecha para o arquivo aberto não ocupar espaço na memória
except:
	print("o arquivo nao pode ser aberto")
	sys.exit(-1)

separador = conteudo.split(";") 	#Transforma o conteúdo em "vetor" e armazena na variável separador
cmd=[]		#Cria um vetor
for comando in separador:
	cmd.append(comando)		#Concatena o conteúdo do "vetor" separador no vetor cmd. Ou seja, transforma realmente o separador em vetor
#Envia o conteúdo do vetor cmd para a classe	
ob.doQuery(cmd)		##Envia o conteúdo do cmd para a classe
