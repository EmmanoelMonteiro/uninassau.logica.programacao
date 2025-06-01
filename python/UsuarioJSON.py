import json
import os
import sys

# Caminho do arquivo JSON na mesma pasta do script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, 'usuarios.json')


def carregar_usuarios(caminho):
    """
    Carrega a lista de usuários do arquivo JSON.
    Retorna lista de dicionários com campos: id (int), nome, email, idade (int).
    """
    if not os.path.exists(caminho):
        return []
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)


def salvar_usuarios(usuarios, caminho):
    """
    Salva a lista de usuários no arquivo JSON.
    """
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=4)


def adicionar_usuario(usuarios, novo):
    usuarios.append(novo)
    return usuarios


def listar_usuarios(usuarios, filtro_nome=None):
    if filtro_nome:
        return [u for u in usuarios if filtro_nome.lower() in u['nome'].lower()]
    return usuarios


def excluir_usuario(usuarios, user_id):
    inicial_len = len(usuarios)
    usuarios = [u for u in usuarios if u['id'] != user_id]
    return usuarios, len(usuarios) < inicial_len


def alterar_usuario(usuarios, user_id, nome=None, email=None, idade=None):
    for u in usuarios:
        if u['id'] == user_id:
            if nome:
                u['nome'] = nome
            if email:
                u['email'] = email
            if idade is not None:
                u['idade'] = idade
            return True
    return False


def print_usuarios(usuarios):
    if not usuarios:
        print('Nenhum usuário encontrado.')
        return
    print(f"{'ID':<5}{'Nome':<20}{'Email':<30}{'Idade':<6}{'Ano':<6}")
    print('-' * 67)
    for u in usuarios:
        print(f"{u['id']:<5}{u['nome']:<20}{u['email']:<30}{u['idade']:<6}{u['ano']:<6}")


def menu():
    print('\n=== Gerenciador de Usuários ===')
    print('1. Listar todos os usuários')
    print('2. Listar usuários por nome')
    print('3. Adicionar novo usuário')
    print('4. Alterar usuário por ID')
    print('5. Excluir usuário por ID')
    print('6. Sair')


def main():
    usuarios = carregar_usuarios(JSON_PATH)

    while True:
        menu()
        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            print_usuarios(listar_usuarios(usuarios))

        elif opcao == '2':
            nome = input('Digite parte do nome para filtrar: ').strip()
            print_usuarios(listar_usuarios(usuarios, filtro_nome=nome))

        elif opcao == '3':
            try:
                novo = {
                    'id': max((u['id'] for u in usuarios), default=0) + 1,
                    'nome': input('Nome: ').strip(),
                    'email': input('Email: ').strip(),
                    'idade': int(input('Idade: ').strip()),
                    'ano': int(input('Ano: ').strip())
                }
            except ValueError:
                print('Entrada inválida. Tente novamente.')
                continue
            usuarios = adicionar_usuario(usuarios, novo)
            salvar_usuarios(usuarios, JSON_PATH)
            print('Usuário adicionado com sucesso.')

        elif opcao == '4':
            try:
                uid = int(input('Digite o ID do usuário a alterar: ').strip())
            except ValueError:
                print('ID inválido. Tente novamente.')
                continue
            nome = input('Novo nome (enter para manter): ').strip()
            email = input('Novo email (enter para manter): ').strip()
            idade_input = input('Nova idade (enter para manter): ').strip()
            idade = int(idade_input) if idade_input else None
            alterou = alterar_usuario(usuarios, uid, nome or None, email or None, idade)
            if alterou:
                salvar_usuarios(usuarios, JSON_PATH)
                print(f'Usuário com ID {uid} alterado com sucesso.')
            else:
                print(f'Usuário com ID {uid} não encontrado.')

        elif opcao == '5':
            try:
                uid = int(input('Digite o ID do usuário a excluir: ').strip())
            except ValueError:
                print('ID inválido. Tente novamente.')
                continue
            usuarios, excluiu = excluir_usuario(usuarios, uid)
            if excluiu:
                salvar_usuarios(usuarios, JSON_PATH)
                print(f'Usuário com ID {uid} excluído com sucesso.')
            else:
                print(f'Usuário com ID {uid} não encontrado.')

        elif opcao == '6':
            print('Saindo...')
            sys.exit(0)

        else:
            print('Opção inválida. Escolha de 1 a 6.')


if __name__ == '__main__':
    main()
