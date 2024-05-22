import csv

# Função para carregar usuários do arquivo CSV
def carregar_usuarios(arquivo):
    usuarios = {}
    with open(arquivo, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            usuarios[row['nome_usuario']] = {'senha': row['senha'], 'tipo': row['tipo_usuario']}
    return usuarios

# Função para salvar usuários no arquivo CSV
def salvar_usuarios(usuarios, arquivo):
    with open(arquivo, mode='w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['nome_usuario', 'senha', 'tipo_usuario'])
        for usuario, dados in usuarios.items():
            writer.writerow([usuario, dados['senha'], dados['tipo']])

# Função para carregar produtos do arquivo CSV
def carregar_produtos(arquivo):
    produtos = []
    with open(arquivo, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            produtos.append({
                'nome': row['nome'],
                'autor': row['autor'],
                'preco': float(row['preco']),
                'quantidade': int(row['quantidade'])
            })
    return produtos

# Função para salvar produtos no arquivo CSV
def salvar_produtos(produtos, arquivo):
    with open(arquivo, mode='w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['nome', 'autor', 'preco', 'quantidade'])
        for produto in produtos:
            writer.writerow([produto['nome'], produto['autor'], produto['preco'], produto['quantidade']])

# Função para adicionar um novo usuário
def adicionar_usuario(usuarios, nome_usuario, senha, tipo_usuario):
    if nome_usuario in usuarios:
        print(f"Erro: Usuário '{nome_usuario}' já existe.")
    else:
        usuarios[nome_usuario] = {'senha': senha, 'tipo': tipo_usuario}
        print(f"Usuário '{nome_usuario}' adicionado com sucesso.")

# Função para listar todos os usuários
def listar_usuarios(usuarios):
    for usuario, dados in usuarios.items():
        print(f"Nome: {usuario}, Tipo: {dados['tipo']}")

# Função para atualizar um usuário existente
def atualizar_usuario(usuarios, nome_usuario, nova_senha=None, novo_tipo=None):
    if nome_usuario in usuarios:
        if nova_senha:
            usuarios[nome_usuario]['senha'] = nova_senha
        if novo_tipo:
            usuarios[nome_usuario]['tipo'] = novo_tipo
        print(f"Usuário '{nome_usuario}' atualizado com sucesso.")
    else:
        print(f"Erro: Usuário '{nome_usuario}' não encontrado.")

# Função para remover um usuário
def remover_usuario(usuarios, nome_usuario):
    if nome_usuario in usuarios:
        del usuarios[nome_usuario]
        print(f"Usuário '{nome_usuario}' removido com sucesso.")
    else:
        print(f"Erro: Usuário '{nome_usuario}' não encontrado.")

# Função para adicionar um novo produto
def adicionar_produto(produtos, nome, autor, preco, quantidade):
    produtos.append({'nome': nome, 'autor': autor, 'preco': preco, 'quantidade': quantidade})
    print(f"Produto '{nome}' adicionado com sucesso.")

# Função para listar todos os produtos
def listar_produtos(produtos):
    for produto in produtos:
        print(f"Nome: {produto['nome']}, Autor: {produto['autor']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

# Função para atualizar um produto existente
def atualizar_produto(produtos, nome, novo_autor=None, novo_preco=None, nova_quantidade=None):
    for produto in produtos:
        if produto['nome'] == nome:
            if novo_autor:
                produto['autor'] = novo_autor
            if novo_preco:
                produto['preco'] = novo_preco
            if nova_quantidade:
                produto['quantidade'] = nova_quantidade
            print(f"Produto '{nome}' atualizado com sucesso.")
            return
    print(f"Erro: Produto '{nome}' não encontrado.")

# Função para remover um produto
def remover_produto(produtos, nome):
    for produto in produtos:
        if produto['nome'] == nome:
            produtos.remove(produto)
            print(f"Produto '{nome}' removido com sucesso.")
            return
    print(f"Erro: Produto '{nome}' não encontrado.")

# Função para buscar um produto pelo nome
def buscar_produto(produtos, nome):
    for produto in produtos:
        if produto['nome'] == nome:
            print(f"Produto encontrado: Nome: {produto['nome']}, Autor: {produto['autor']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")
            return produto
    print(f"Erro: Produto '{nome}' não encontrado.")
    return None

# Função para listar produtos ordenados por nome
def listar_produtos_ordenados_nome(produtos):
    produtos_ordenados = sorted(produtos, key=lambda x: x['nome'])
    listar_produtos(produtos_ordenados)

# Função para listar produtos ordenados por preço
def listar_produtos_ordenados_preco(produtos):
    produtos_ordenados = sorted(produtos, key=lambda x: x['preco'])
    listar_produtos(produtos_ordenados)

# Exemplo de uso
if __name__ == "__main__":
    usuarios = carregar_usuarios('usuarios.csv')
    produtos = carregar_produtos('produtos.csv')

    # Adicionar novos usuários
    adicionar_usuario(usuarios, 'novo_gerente', 'senha123', 'gerente')
    adicionar_usuario(usuarios, 'novo_funcionario', 'senha123', 'funcionario')
    
    # Listar todos os usuários
    listar_usuarios(usuarios)

    # Atualizar usuário
    atualizar_usuario(usuarios, 'novo_funcionario', nova_senha='nova_senha123')

    # Remover usuário
    remover_usuario(usuarios, 'novo_funcionario')

    # Salvar usuários no arquivo
    salvar_usuarios(usuarios, 'usuarios.csv')

    # Adicionar novos produtos
    adicionar_produto(produtos, 'Livro X', 'Autor X', 29.90, 10)
    adicionar_produto(produtos, 'Livro Y', 'Autor Y', 19.90, 5)

    # Listar todos os produtos
    listar_produtos(produtos)

    # Atualizar produto
    atualizar_produto(produtos, 'Livro X', novo_preco=24.90)

    # Remover produto
    remover_produto(produtos, 'Livro Y')

    # Buscar produto
    buscar_produto(produtos, 'Livro X')

    # Listar produtos ordenados por nome
    listar_produtos_ordenados_nome(produtos)

    # Listar produtos ordenados por preço
    listar_produtos_ordenados_preco(produtos)

    # Salvar produtos no arquivo
    salvar_produtos(produtos, 'produtos.csv')
