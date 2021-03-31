def about(message,bot,info):
    print('Sobre o bot requisitado')
    msg=f'''
    *{info[0]}*
    Visite meu github:
    http://github.com/oporadokrl
    '''
    bot.reply_to(message,msg)