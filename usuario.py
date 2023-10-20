import json
from hashlib import sha256

#Criação da classe User
class User:
    def __init__(self, nome, senha, cargo):
        self.nome = nome
        self.senha = senha
        self.cargo = cargo

#Definição dos parametros que irão ser utilizados para o nome do usuario
    def set_nome(self):
        print(' - Minímo 4 caracteres\n - Máximo 16 caracteres\n - Não pode conter espações em branco\n')
        while True:
            self.nome = input("User: ")
            user_sem_espacos = self.nome.replace(" ", "")
            if user_sem_espacos == self.nome:
                while True:
                    if 3 >= len(self.nome) > 0:
                        print("Nome deve ter no mínimo 4 caracter")
                        self.nome = input("User: ")

                    elif 16 >= len(self.nome) >= 4:
                        print("User valido")
                        break
                    else:
                        print("O nome deve ter no maximo 16 caracter")
                        self.nome = input("User: ")
                break
            else:
                print("Não é permintido espaços em branco")

#Definição dos parametros que irão ser utilizados para a criação da senha, sendo ela armazenada de forma criptografada com sha256 em hexadecimal
    def set_senha(self):
        senha_inserida = input('Insira sua Senha:\n')
        hash_senha = sha256(senha_inserida.encode())
        self.senha = hash_senha.hexdigest()
        check = sha256(input('Confimre sua senha:\n').encode()).hexdigest()
        if self.senha == check:
            pass
        else:
            while self.senha != check:
                print('As senhas não estão semelhentes tente novamente')
                self.senha = input("Insira sua Senha novamente:\n")
                check = input('Confimre sua senha:\n')

#Definição dos parametros que irão ser utilizados para definir o cargo de cada usuario
    def set_cargo(self):
        print('Cargos Dispiníveis:\n [1] Visualizador   \n [2] Padrão \n [3] Administrador  \n [4] Super Administrador \n Qual é o tipo de cargo desse usuário?')
        while True:
            n_cargo= input('(Insira o valor numérico correspondente)\n')
            try:
                n_cargo = int(n_cargo)
                if n_cargo in [1,2,3,4]:
                    if n_cargo == 1:
                                print('Usuário configurado como Visualizador')
                                self.cargo = 'Visualizador'
                    elif n_cargo == 2:
                                print('Usuário configurado como Padrão')
                                self.cargo = 'Padrao'
                    elif n_cargo == 3:
                                print('Usuário configurado como Administrador')
                                self.cargo = 'Administrador'
                    elif n_cargo == 4:
                                print('Usuário configurado como Super Administrador')
                                self.cargo = 'Super Administrador'
                else:
                    raise(Exception)    
                break
            except Exception:
                print('Cargo não identificado')
            except ValueError:
                print('Cargo não identificado')

#Sucesso ao criar um usuario
    def ssuccess(self):
        print(f'Usuário criado com sucesso! \nBem vindo {self.nome}, você é o mais novo Usuário {self.cargo}')

lista_de_usuarios=[]

#enquanto o loop rodar será permitido criar varios usuarios e definir seus cargos e tudo será salvo em usuarios.json
while True:  
    print('!Crie um usuário! ou !Digite "sair" para encerrar!')
    usuario = User('standard', 'standard', 'standard')
    usuario.set_nome()

    nome = usuario.nome
    if nome.lower() == 'sair':  #Comando sair permite que se encerre a criação de usuarios
        break
    
    usuario.set_senha()
    senha = usuario.senha

    usuario.set_cargo()
    cargo = usuario.cargo

#Criação do dicionario com informações especificas de cada usuarios 
    dicionario_user = {
        "User": nome,
        "Senha": senha,
        "Cargo": cargo
    }

#Inserir as informações do usuario criado em uma lista cque comportarão todos os usuarios criado
    lista_de_usuarios.append(dicionario_user)
    usuario.ssuccess() 

#Escreve a lista criada no aquivo usuarios.json
with open ("usuarios.json","w") as arquivo_json:
    json.dump(lista_de_usuarios,arquivo_json)
