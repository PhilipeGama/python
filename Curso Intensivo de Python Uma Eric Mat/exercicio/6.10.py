favorite_numbers = {
					'user_1' : {'nome':'maria',
					 'numeros' : [7,8,9]
					},
					'user_2' : {'nome':'pedro',
					 'numeros' : [3,4,5]
					},
					'user_3' : {'nome':'carol',
					 'numeros' : [1,2,3]	
					},
					'user_3' : {'nome': 'philipe',
					 'numeros' : [7,8,9]
					},
				}

for user,user_info in favorite_numbers.items():	
	nome = user_info['nome']
	numeros = user_info['numeros']

	print('User: ' + user.title())
	print('Nome: ' + nome.title())
	print('Numeros Favoritos: ' + str(numeros))