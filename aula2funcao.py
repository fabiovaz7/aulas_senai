# def formatar_real_replace(valor):
#     texto = f"R$ {valor:,.2f}" #padrão EUA: 1,234.56
#     texto = texto.replace(",", "X")
#     texto = texto.replace(",", "X")  
#     texto = texto.replace("X", ".") 
#     return texto

# #Uso 
# preco = 1234.5
# print(formatar_real_replace(preco)) # R$ 1.234,50

# Parametros com valor padrão (default)
# def saudacao(nome, mensagem="Bem vindo!"):
#     print(f"Olá, {nome}! {mensagem}")

# saudacao("Ana")
# saudacao("Bob", "Bom dia!")

# # Argumentos nomeados (keyword args)
# def cria_usuario(nome, idade, admin=False):
#     print(f"{nome} | {idade} anos | admin = {admin}")

# cria_usuario(idade=20, nome="Carol")
# cria_usuario("Dan", 25, admin=True)

def criar_perfil(nome, idade, cidade):
    print(f'{nome}, {idade} anos ,{cidade}')

criar_perfil(cidade="Curitiba", nome="Chupson", nome="40")
#Chupson, 40 anos, Curitiba - funciona independente da ordem!


