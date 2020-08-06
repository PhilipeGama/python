cities = {
	'city_1' : { 
		'nome' : 'manaus',
		'contry' : 'brasil',
		'population' : '1,793 milhão',
		'fact' : 'Manaus, nos bancos do Rio Negro no noroeste do Brasil, é a capital do vasto estado do Amazonas',
	},

	'city_2' : {
		'nome' : 'miami',
		'contry' : 'estados unidos',
		'population': '470.914',
		'fact': 'Miami é uma cidade internacional no extremo sudeste da Flórida.',
	},
}

for city,city_info in cities.items():
	cit = city
	nome = city_info['nome']
	country = city_info['contry']
	population = city_info['population']
	fact = city_info['fact']


	print('Cidade: ',city.title())
	print('Nome: ' + nome.title())
	print('País: ' + country.title())
	print('População: ' + population.title())
	print('Fato: ' + fact)
	print('')


