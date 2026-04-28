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
    print(f"{nome}, {idade} anos, {cidade}")

# Chamadas com argumentos nomeados (ordem não importa)
criar_perfil(cidade="Curitiba", nome="Chupson", idade=40)
criar_perfil(nome="Ana", idade=25, cidade="São Paulo")

# Função com quantidade variável de argumentos
def somar_tudo(*numeros):
    return sum(numeros)

# Exibindo os resultados
print(somar_tudo(1, 2))
print(somar_tudo(1, 2, 3, 4))
print(somar_tudo(20, 30))
