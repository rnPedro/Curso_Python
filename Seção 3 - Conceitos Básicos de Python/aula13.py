nome = 'Pedro'
altura = 1.84
peso = 115

imc = peso / altura ** 2


linha1 = f'{nome} tem {altura:.2f} de altura, {peso} de peso e seu IMC é {imc}' # Usando f-string para formatar a string


print(linha1) # Imprimindo a string formatada)
print(nome, 'tem', altura, 'de altura,', peso, 'de peso e seu IMC é', imc)