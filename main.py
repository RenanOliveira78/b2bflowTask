from supabase import create_client
from dotenv import load_dotenv
import os
import requests

#Carrega as variaveis em .env para o ambiente
load_dotenv()

#Carrega Supabase tokens e instance em varaveis
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

#Carrega Z-API tokens e instance em varaveis
ZAPI_INSTANCE = os.getenv("ZAPI_INSTANCE")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")

#Cria cliente Supabase
supabase = create_client(SUPABASE_URL ,SUPABASE_KEY)

#Função para buscar todos os dados da tabela contatos
def busca_contatos():
    dados = supabase.table("contatos").select("*").execute()
    return dados.data

#Função para enviar mensagem pela Z-API
def enviar_mensagem(numero_celular, nome):
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE}/token/{ZAPI_TOKEN}/send-text"
    #cabeçalho incluindo o token de auth e tipo de conteúdo
    headers = {
        "Client-Token": ZAPI_CLIENT_TOKEN,
        "Content-Type": "application/json"
    }
    payload = {
        "phone": numero_celular,
        "message": f"Olá {nome}, tudo bem com você?"
    }
    resp = requests.post(url, json=payload, headers=headers)
    print(resp.json())


if __name__ == "__main__":
    contatos = busca_contatos()
    for contato in contatos[:3]:
        enviar_mensagem(contato["numero_celular"], contato["nome"])