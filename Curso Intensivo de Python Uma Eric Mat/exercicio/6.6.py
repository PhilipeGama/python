favorita_languages = {
				'jen' : 'python',
				'sarah' : 'c',
				'edward' : 'ruby',
				'phil' : 'python',
			}

pessoas = ['phil','john','pedro']

for favorita_language in favorita_languages.keys():
	print('Obrigado por responder a enquente, '+favorita_language.title())

for pessoa in pessoas:	
	if pessoa not in favorita_languages.keys():
		print('Por favor responda qual sua linguagem favorita '+pessoa.title())




