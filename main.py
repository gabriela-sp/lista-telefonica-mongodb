from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

uri = "mongodb+srv://gabrielapereira:admin@cluster0.wbnna.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client['senac']
collection = db["contatos"]

def criar_contato():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    contato = {"nome": nome, "telefone": telefone}
    collection.insert_one(contato)
    print("Contato adicionado com sucesso!\n")

def listar_contatos():
    contatos = collection.find()
    for contato in contatos:
        print(f"ID: {contato['_id']} | Nome: {contato['nome']} | Telefone: {contato['telefone']}")
    print()

def atualizar_contato():
    id_contato = input("Digite o ID do contato que deseja atualizar: ")
    nome = input("Digite o novo nome: ")
    telefone = input("Digite o novo telefone: ")
    try:
        id_up = ObjectId(id_contato)
    except:
        print("ID inválido. Verifique o formato e tente novamente.")
        return
    collection.update_one({"_id": id_up}, {"$set": {"nome": nome, "telefone": telefone}})
    print("Contato atualizado com sucesso!\n")

def deletar_contato():
    id_contato = input("Digite o ID do contato que deseja deletar: ")
    
    try:
        id_del = ObjectId(id_contato)
    except:
        print("ID inválido. Verifique o formato e tente novamente.")
        return
    collection.delete_one({"_id": id_del})
    print("Contato deletado com sucesso!\n")

def menu():
    while True:
        print("==== LISTA TELEFONICA ====")
        print("1. Criar Contato")
        print("2. Listar Contatos")
        print("3. Atualizar Contato")
        print("4. Deletar Contato")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            atualizar_contato()
        elif opcao == "4":
            deletar_contato()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()