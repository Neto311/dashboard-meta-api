# 📊 Dashboard Meta Ads

Uma solução robusta para automação de coleta, armazenamento e relatórios de dados do **Facebook Ads (Meta Ads)**. Esta aplicação integra a API do Facebook Insights, processa os dados de performance de anúncios e gera relatórios automáticos em PDF.

## 🚀 Principais Funcionalidades

- **Coleta Automatizada**: Integração direta com a API de Graph da Meta para buscar insights de anúncios.
- **Processamento de Dados**: Utiliza **Pandas** e **NumPy** para formatação e limpeza de métricas de marketing.
- **Armazenamento**: Persistência de dados utilizando **SQLAlchemy** e banco de dados relacional.
- **Relatórios em PDF**: Geração automática de relatórios visuais utilizando **FPDF2**.
- **Agendamento (Scheduler)**: Execução periódica de tarefas para manter o dashboard sempre atualizado.
- **API REST**: Interface construída com **FastAPI** para consulta de dados e gerenciamento de rotas.
- **Notificações**: Integração com **Twilio** para alertas e comunicações.

## 🛠️ Tecnologias Utilizadas

- **FastAPI**: Backend de alta performance.
- **Pandas/NumPy**: Análise e manipulação de dados.
- **SQLAlchemy**: ORM para gestão de banco de dados.
- **FPDF2**: Criação de documentos PDF personalizados.
- **Plotly**: Visualização de dados (gráficos e dashboards).
- **Twilio**: Serviço de mensagens e notificações.
- **Uvicorn**: Servidor ASGI para produção.

## 📋 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/SEU_USUARIO/dashboard-meta.git
   cd dashboard-meta
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configuração do Ambiente (.env):**
   Crie um arquivo `.env` na raiz com suas credenciais:
   ```env
   FACEBOOK_ACCESS_TOKEN=seu_token
   FACEBOOK_AD_ACCOUNT_ID=seu_id
   DATABASE_URL=sua_url_do_banco
   TWILIO_ACCOUNT_SID=seu_sid
   TWILIO_AUTH_TOKEN=seu_token
   ```

5. **Inicie a aplicação:**
   ```bash
   python main.py
   ```

## 🛠️ Estrutura do Projeto

```text
├── app/
│   ├── api/            # Rotas e controladores da API
│   ├── db/             # Configuração e inicialização do banco
│   ├── services/       # Lógica de negócio (Meta, PDF, DB, Scheduler)
│   └── models/         # Definições de tabelas e esquemas
├── assets/             # Recursos estáticos
├── reports/            # Relatórios PDF gerados
├── main.py             # Arquivo principal de execução
└── requirements.txt    # Lista de dependências
```

## ✒️ Autor

Desenvolvido por **Osvaldo Celotto**.
