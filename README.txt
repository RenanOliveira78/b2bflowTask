b2bflow 1ª etapa do processo para Estágio.
Projeto de envio de mensagen, implementando Suparbase e Z-API.

--------------

# Passos de Setup:
    1. Criar Projeto no Supabase
        1.2 Criar e popular a tabela do projeto
        1.3 Criar política de acesso para a tabela criada

    2. Criar uma instância web de teste  na Z-API
        2.2 Conectar instância

# Variáveis de ambiente:
    SUPABASE_URL=https://agsfapqfsegwneyywwpf.supabase.co
    SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFnc2ZhcHFmc2Vnd25leXl3d3BmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTUwMDg0MDksImV4cCI6MjA3MDU4NDQwOX0.LZJStT53oDV_0nkIPMgDCa4jMFPpj8OReMR2w6a9dzY
    ZAPI_INSTANCE=3E59B824ED32C0721C7B8EFA95C651E6
    ZAPI_TOKEN=D6DBB2A57917059B172CA5D6

# Como rodar:
    1. Ativar ambiente virtual
        python -m venv venv
        venv\Scripts\activate

    2. Instalar dependências
        pip install -r dependencias.txt
    
    3. Executar o script
        python main.py