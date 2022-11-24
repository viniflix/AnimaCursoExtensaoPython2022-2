#Exemplo repetição com while
contador = 1

while(contador <= 10):
  print(contador)
  contador = contador+1 


#Exemplo com listas
frutas = ["morango", "pera", "laranja"]

print(frutas)
print(frutas[2])

#Contador de itens em lista
print(len(frutas))

#Adicionar item a lista
frutas.append("uva")


i=0 
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1

print("Exemplo das frutas com FOR")
for fruta in frutas:
  print(fruta)

