#Exemplos com input():
nome = input("Digite seu nome: ")

#Comandos de saida:
print(nome)
print(f"Boa noite, seu nome é {nome} \n \n")

#Exercicio nome e idade:
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Seu nome é {nome} e você tem {idade} anos \n \n")

#Mostrando o dobro da idade:
dobro = idade * 2
print(f"O dobro da sua idade é {dobro} \n \n")

#Estrutura condicional (if):

if idade >= 18:
  print("Você é maior de idade.")
else:
  print("Você é menor de idade.")

#Exercicio com gênero e se já prestou serviço militar (minha resposta)

genero = input("Qual seu Genêro? (M/F)")

if genero == "M":
  if idade >= 18:
    sm = input("Já prestou serviço militar? (S/N)")
    if sm == "S":
      print("Você está OK")
    else:
      print("Você não esta OK")
  else:
    print("Você é de menor")
elif genero == "F":
  print("Você é mulher")
else:
  print("Resposta inválida")

#Exercicio com gênero e se já prestou serviço militar (resposta do professor)

gen = input("Informe o gênero M=Masculino, F=Feminino, O=Outros: ")

if idade >= 18 and gen == "M":
  print(
    "... e você também precisa/precisou prestar o serviço militar obrigatório")

#Pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "{nome} Você é bichão, mesmo..."

nome = input("Informe seu nome: ")
nota = float(input("Digite sua nota de 0 a 10: "))

if nota == 10:
  print(f"{nome}, Você é bichão, mesmo...")
elif nota >= 6 and nota < 10:
  print(f"{nome}, bom trabalho.")
else:
  print("Burro, não tirou 10")
