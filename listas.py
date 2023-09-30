lista_compra = ["frutas", "pao", "carne", "arroz", "krokeros"]

print("hoje vou comprar no mercado: ", lista_compra)
print(type(lista_compra))
print("a quantidade de elemento na lista e: ",len(lista_compra))
lista_compra.append("feijao")
lista_compra.remove("krokeros")
nova_lista = sorted(lista_compra)
print(nova_lista)

terceiro_elemento = lista_compra[2]
print(terceiro_elemento)

#indicar o ultimo elemento
ultimo_elemento = lista_compra[-4]
print(ultimo_elemento)

lista_compra.pop(-4)
print(lista_compra)


#indicar os 3 primeiros
primeiros_elementos = lista_compra[:3]
print(primeiros_elementos)

print(terceiro_elemento)
print(primeiros_elementos)


