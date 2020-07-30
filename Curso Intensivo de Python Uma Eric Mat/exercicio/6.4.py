glossario = {'if':'teste condicional',
			  'for':'estrutura de repetição',
			  'lista':'conjuto de dados',
			  'pep8':'manual de boas práticas do Python',
			  'append':'comando para adicionar um artefato no final da lista',
			  'set':'excluir repetição em lista',
			  'sorted':'ordernar a lista',
			  'lower':'tranformar em lowercase'}


for palavra,significado in glossario.items():
	print(palavra.title() + ': ' +significado)

