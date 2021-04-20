def buscar(alunos, matricula):
	try:
		if (type(matricula) is not int):
			raise TypeError
		if matricula is not 100000 <= matricula <= 999999:
			raise ValueError
		return (aluno, matricula)
	except TypeError:
			print("O parametro matricula deve ser inteiro!")
	except ValueError: 
			print("O numero de matricula deve ter 6 digitos!")
	except KeyError:
			print("Nao existe aluno com este numero de matricula!")
	
	
	return (alunos)



























