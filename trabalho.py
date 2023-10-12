#primeiro exercicios

#soma = 0
#for i in range(1, 16):
   # soma += i
#print(soma)

#segundo exercicio

#numero = int(input("digite um número para ver sua tabuada: "))

#for i in range(1, 11):
 #   resultado = numero * i
#    print(numero, "x", i, "=", resultado)
    
#terceiro exercicio

#print("Bem-vindo ao Sistema de Atendimento Imoboliário!")

#Solicitar ao usuário que escolha uma opção

#opcao = input("Escolha um numero desejado: \n1. Alugar\n2. Comprar\n3. falar com o corretor\n4. Atendimento no seotr jurídico\n")

#Processar a escolha do usuário
#if opcao == "1":
#     print("A opção escolhida foi de alugar. Aguarde um atendente.")
#elif opcao == "2": 
     #print("A opção escolhida foi de comprar. Aguarde um atendente.")
#elif opcao == "3": 
     #print("Você deseja falar com o corretor. Iremos te direcionar ao corretor Imobiliário.")
#elif opcao == "4":
    # print("Você deseja se comunicar com o setor jurídico. Iremos te direcionar a um advogado responsavel pelo imovel.")
#else:
   #print("Opção inexistente. Por favor, escolha uma opção disponivel.")
    
    #print("Agradecemos sua preferencia ao nosso serviço. Volte sempre!") 
    
    #quarto exercicio
senha_correta = "proz2022"
tentativas = 0
    
while tentativas < 3:
    senha_digitada = input(" usuario,digite uma senha: ")
    if senha_digitada == senha_correta: 
         print("acesso liberado!")
    break
    elif tentativas == 2:
    print("conta bloqueada!")
    break
else:
    print("/senha incorreta!")
tentativas = tentativas + 1
if tentativas = 2:
         print("senha incorreta. Voce excedeu o numero maximo de tentativas. Acesso bloqueado.")
        
            
#quinto exercicio

def analisar_idades(idades):
        maior_idade = max(idades)
        menor_idade = min(idades)
        media_idade = sum(idades)/ len(idades)
 
        return maior_idade, menor_idade, media_idade
idades: []

for i in range(5):
    idade: int(input(f"digite a idade da pessoa {i + 1}"))
    idade.append(idade)

maior, menor, media =
analisar_idade(idade)                
    
print(f"a maior idade e: {maior}")
print(f"a menor idade e: {menor}")
print(f"a media idade e: {media:.2f}")
            
    
           
         