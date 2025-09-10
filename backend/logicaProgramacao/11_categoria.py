import json
produto = []
categoria = []

id_categoria = 0 
id_produto = 0 



def exibir_menu():
    print ("-------loja generico-------:")
    print ("1.cadastrar categoria")
    print ("2.listar categoria")
    print ("3.categoria associada")
    print ("4.sair")

def cadastrar_categoria():
   print ("/cadastrar produto:")
   nome_categorias = input ("nome: ")
   id_categoria +=1 

   categoria_estoque = {
       "nome_categoria" : nome_categorias, 
       "id_categoria" : id_categoria
}
   
   def cadastrar_produto(): 
       id_produto +=1 
       nome_produto = input ("nome: ")
       preco = input ("preco: ")
       id_categoria_associada = input 

       produto_estoque = {
         "nome_produto" : nome_produto,
         "id_produto" : id_produto,
         "preco" : preco,
         "id_categoria_associada" : id_categoria_associada, 
 }

while True:
   exibir_menu()
   opcao = input("Escolha uma opcao: ")

   if opcao == '1':
        cadastrar_categoria()
   elif opcao == '2':
        cadastrar_produto()
   elif opcao == '3':
        listar_produtos()
   elif opcao == '4':
        print("Encerrando sistema. Até logo!")
        break
   else:
        print("Opção inválida. Tente novamente.")