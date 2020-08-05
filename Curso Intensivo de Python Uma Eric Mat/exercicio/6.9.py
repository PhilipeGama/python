favorite_places = {
	'user_01': {'nome' : 'philipe',
		'local_1' : 'ponta negra',
		'local_2': 'millenium',
		'local_3' : 'parque dos bilhares',
	},
	'user_02':{'nome' : 'carolina',
		'local_1' : 'ponta negra',
		'local_2' : 'porão do alemão',
		'local_3' : 'studio 5',
	},
	'user_03':{'nome': 'joed',
		'local_1' : 'porão do alemão',
		'local_2' : 'ponta negra',
		'local_3' : 'careiro',
	},
}

for user,user_info in favorite_places.items():
	print('User: '+user)
	nome = user_info['nome']
	local_1 = user_info['local_1']
	local_2 = user_info['local_2']
	local_3 = user_info['local_3']

	print('Nome: '+nome.title())
	print('Locais Favoritos: '+local_1+','+local_2+','+local_3)

	print('')