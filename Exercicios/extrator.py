from abc import ABC, abstractmethod



class ExtratorDados(ABC):
    
    @classmethod
    @abstractmethod
    def extrair_dados(cls, *args, **kwargs):
        pass
class ExtratorTXT(ExtratorDados):
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.usuarios = []

    def extrair_dados(self):
        try:
            with open(self.caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(',')
                    tipo = dados[0]

                    if tipo == 'UsuarioComum' and len(dados) == 3:
                        _, nome, email = dados
                        self.usuarios.append({
                            'tipo': 'Comum',
                            'nome': nome,
                            'email': email
                        })

                    elif tipo == 'UsuarioAdministrador' and len(dados) == 4:
                        _, nome, email, funcao = dados
                        self.usuarios.append({
                            'tipo': 'Administrador',
                            'nome': nome,
                            'email': email,
                            'funcao': funcao
                        })

        except FileNotFoundError:
            print(f"Arquivo '{self.caminho_arquivo}' não encontrado.")
        except Exception as e:
            print(f"Erro ao processar o arquivo: {e}")
     
    def exibir_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário carregado.")
            return

        print("\n--- Lista de Usuários ---")
        for i, usuario in enumerate(self.usuarios, start=1):
            print(f"{i}. Tipo: {usuario['tipo']}")
            print(f"   Nome: {usuario['nome']}")
            print(f"   Email: {usuario['email']}")
            if usuario['tipo'] == 'Administrador':
                print(f"   Função: {usuario['funcao']}")
            print(" ")

extrator = ExtratorTXT("Exercicios/banco_usuarios.txt")
extrator.extrair_dados()
extrator.exibir_usuarios()
