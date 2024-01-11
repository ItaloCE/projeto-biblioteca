from livro.livro_repositorio import livros
from livro.buscar_livro import buscarLivro

def emprestarLivro(id: int):
    livro = buscarLivro(id)

    if not livro:
        print('Erro: Livro não encontrado!')
        return

    if not livro['disponivel']:
        print('Erro: O livro está indisponivel!')
        return

    livro['disponivel'] = False
    print('Emprestimo realizado com sucesso!')

def devolverLivro(id: int):
    livro = buscarLivro(id)
    if not livro:
        print('Erro: Livro não encontrado!')
        return

    if livro['disponivel']:
        print('Erro: O livro ja está disponivel!')
        return

    livro['disponivel'] = True
    print('Livro devolvido com sucesso!')

if __name__ == '__main__':
    emprestarLivro(1)
    print(livros)