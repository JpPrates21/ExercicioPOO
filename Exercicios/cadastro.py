from abc import ABC, abstractmethod


def usuario_existe(email):
    try:
        with open("Exercicios/banco_usuarios.txt", "r", encoding="utf-8") as f:
            for linha in f:
                partes = linha.strip().split(",")

                if len(partes) >= 3 and partes[2].lower() == email.lower():
                       return True
            return False
    except FileNotFoundError:
        return False
    

def salvar_usuario_em_arquivo(tipo, nome, email, nivel_acesso=None):
    with open("Exercicios/banco_usuarios.txt", "a", encoding="utf-8") as f:
        if tipo == "comum":
            f.write(f"UsuarioComum,{nome},{email}\n")
        elif tipo == "admin":
            f.write(f"UsuarioAdministrador,{nome},{email},{nivel_acesso}\n")


class Usuario(ABC):

    @classmethod
    @abstractmethod
    def cadastrar(cls, *args, **kwargs):
        pass



class UsuarioComum(Usuario):
    def __init__(self, nome, email):

        self.nome = nome
        self.email = email

    @classmethod
    def cadastrar(cls, nome, email):
        if usuario_existe(email):
            print(f"Erro: email já cadastrado '{email}' já cadastrado")
            return None
        print(f"Cadastrando usuario comum: {nome}, {email}")  
        salvar_usuario_em_arquivo("comum", nome, email)      
        return cls(nome, email)



class UsuarioAdministrador(UsuarioComum):
    def __init__(self, nome, email, nivel_acesso: str):
        super().__init__(nome, email)

        self.nivel_acesso = nivel_acesso

    @classmethod
    def cadastrar(cls, nome, email, nivel_acesso: str):
        if usuario_existe(email):
            print(f"Erro: email já cadastrado '{email}' já cadastrado")
            return None
        print(f"Cadastrando usuario admin: {nome}, {email}, {nivel_acesso}")  
        salvar_usuario_em_arquivo("admin", nome, email, nivel_acesso)
        return cls(nome, email, nivel_acesso)




Admin1 = UsuarioAdministrador.cadastrar("Camila", "Camila@gmail.com", "admin")


