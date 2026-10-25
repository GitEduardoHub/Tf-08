class Commit:
    """
    Representa um commit individual no histórico.
    Guarda o id, a mensagem, o autor e uma referência para o commit anterior (pai).
    """
    def __init__(self, id, mensagem, autor, pai=None):
        """
        Inicializa o commit com as informações básicas e o commit pai.
        O primeiro commit não recebe pai, mantendo o padrão None.
        """
        self.id = id
        self.mensagem = mensagem
        self.autor = autor
        self.pai = pai

    def historico(self):
        """
        Imprime a formatação do commit atual e chama o histórico do pai.
        O caso base ocorre implicitamente quando self.pai é None.
        """
        print(f"#{self.id} {self.mensagem} ({self.autor})")
        
        # Evitando usar "else" através de um simples "if"
        if self.pai is not None:
            self.pai.historico()


class Repositorio:
    """
    Gerencia a cadeia de commits, mantendo controle do topo do histórico (head)
    e contando quantos commits foram feitos no total.
    """
    def __init__(self, nome, autor):
        """
        Inicia o repositório sem nenhum commit (head nulo) e com a contagem zerada.
        """
        self.nome = nome
        self.autor = autor
        self.head = None
        self.contador_de_commits = 0

    def commitar(self, mensagem):
        """
        Soma um no contador, cria um novo commit apontando o head antigo como pai
        e atualiza o head para este novo commit.
        """
        self.contador_de_commits += 1
        
        novo_commit = Commit(self.contador_de_commits, mensagem, self.autor, self.head)
        self.head = novo_commit

    def log(self):
        """
        Mostra todos os commits a partir do mais recente.
        Usa retorno antecipado (early return) para evitar a palavra "else".
        """
        if self.head is None:
            print("Nenhum commit ainda")
            return
            
        self.head.historico()

    def total_de_commits(self):
        """
        Conta a quantidade de commits percorrendo de pai em pai usando um laço while.
        """
        quantidade = 0
        commit_atual = self.head
        
        while commit_atual is not None:
            quantidade += 1
            commit_atual = commit_atual.pai
            
        return quantidade


# --- Área de Testes ---
# Substitua pelo seu nome e RA verdadeiros!
repositorio = Repositorio("meu-projeto", "Luis Eduardo Almeida - 6326294")

repositorio.log()
repositorio.commitar("Inicia o desenvolvimento do projeto base")
repositorio.commitar("Adiciona o arquivo de configuracoes e README")
repositorio.commitar("Corrige erros de digitacao na documentacao principal")
repositorio.log()
print(repositorio.total_de_commits())