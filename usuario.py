class User:
    def __init__(self, nome, senha, cargo):
        self.nome = nome
        self.senha = senha
        self.cargo = cargo

    def set_nome(self):
        self.nome = input('Insira seu nome de Usuário:\n')

    def set_senha(self):
        self.senha = input('Insira sua Senha:\n')
        check = input('Confimre sua senha:\n')
        if self.senha == check:
            pass
        else:
            while self.senha != check:
                print('As senhas não estão semelhentes tente novamente')
                self.senha = input("Insira sua Senha novamente:\n")
                check = input('Confimre sua senha:\n')

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
                                self.cargo = 'Padrão'
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

    def ssuccess(self):
        print(f'Usuário criado com sucesso! \nBem vindo {self.nome}, você é o mais novo Usuário {self.cargo}')



usuario = User('standard', 'standard', 'standard') 

print('!Crie seu usuário!')
usuario.set_nome()
usuario.set_senha()
usuario.set_cargo()
usuario.ssuccess()

