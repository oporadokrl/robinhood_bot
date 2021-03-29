import requests
def consultar(message,bot):
	cmd = message.text[6:]
	print('Consulta por placa requisitada por {} {}'.format(message.chat.first_name,message.chat.last_name))
	api = requests.get('https://apicarros.com/v1/consulta/{}/json'.format(cmd), verify = False).json() # JSQ7436
	if (api['modelo']) == 'LIMITE DE CONSULTA ATINGIDO':
      		msg='LIMITE DE CONSULTA ATINGIDO'
      	#elif (placa_data['codigoRetorno']) == "1":
      	#	msg='{} :Placa inválida'.format(cmd)
	else:
		msg='''
        	Ano: {}
            Data: {}
            Modelo: {}
            Ano do modelo: {}
            Cor: {}
            Marca: {}
            Roubo/furto: {}
            Situação: {}
            Placa: {}
            Chassi: {}
            UF: {}
            Município: {}
            Modificada em: {}
            Alarme atualizado: {}
            Mensagem de retorno: {}
            Código de retorno: {}
      '''.format(api['ano'],api['data'],api['modelo'],api['anoModelo'],api['cor'],api['marca'],api['dataAtualizacaoRouboFurto'],api['situacao'],api['placa'],api['chassi'],api['uf'],api['municipio'],api['dataAtualizacaoCaracteristicasVeiculo'],api['dataAtualizacaoAlarme'],api['mensagemRetorno'],api['codigoRetorno'])  
	bot.reply_to(message,msg)