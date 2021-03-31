import requests,json
def consultar(message,bot,mode):
    print('aqui')
    if mode == 1:
        cmd = (message.text).replace('/cpf ','').replace('/CPF ','')
        api = requests.get("http://45.178.183.3/cpf.php?cpf={}".format(cmd)).text
    if mode == 3:
        cmd = (message.text).replace('/nome ','').replace('/NOME ','')
        cmd = cmd.replace(' ','%20')
        api = requests.get("http://45.178.183.3/nome.php?nome={}".format(cmd)).text
    api = api.replace('</script>','').replace('</head>','').replace('</body>','').replace('</pre>','').replace('<body>','').replace('<pre style="word-wrap: break-word; white-space: pre-wrap;">','').replace('</pre>','').replace('!function(){let e=!1;function n(){if(!e){const n=document.createElement("meta");n.name="dapp-detected",document.head.appendChild(n),e=!0}}if(window.hasOwnProperty("ethereum")){if(window.__disableDappDetectionInsertion=!0,void 0===window.ethereum)return;n()}else{var t=window.ethereum;Object.defineProperty(window,"ethereum",{configurable:!0,enumerable:!1,set:function(e){window.__disableDappDetectionInsertion||n(),t=e},get:function(){if(!window.__disableDappDetectionInsertion){const e=arguments.callee;e&&e.caller&&e.caller.toString&&-1!==e.caller.toString().indexOf("getOwnPropertyNames")||n()}return t}})}}();','').replace('head','').replace('<html>','')
    api = json.loads(api)
    if mode == 1:
        msg = f'''
CPF: {api['cpf']}
Nome: {api['nome']}
Sexo: {api['sexo']}
Nascimento: {api['nascimento']}
    '''
    if mode == 3:
        msg = f'''
Resultados: {api['quantidadeResultados']}
CPF: {api['resultados'][0]['cpf']}
Nome: {api['resultados'][0]['nome']}
Sexo: {api['resultados'][0]['sexo']}
Nascimento: {api['resultados'][0]['nascimento']}
        '''
    bot.reply_to(message,msg)