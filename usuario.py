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
        print('Cargos Dispiníveis:\n [1] Visualizador   \n [2] Padrão \n [3] Administrador  \n [4] Super Administrador')
        while True:
            n_cargo= input('Qual tipo de Cargo desse usuario ?\n(Insira o valor numérico correspondente)\n')
            try:
                n_cargo = int(n_cargo)
                while n_cargo in [1,2,3,4]:
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
                            print("Cargo não encontrado")
                break 
            except ValueError:
                i = 2
                print('Deve ser inserido um valor numérico')


    def ssuccess(self):
        print('Usuário criado com sucesso!')



usuario = User('standard', 'standard', 'standard') 

print('Crie seu usuário:')
usuario.set_nome()
usuario.set_senha()
usuario.set_cargo()
usuario.ssuccess()

