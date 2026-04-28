# 📧 AI Email Organizer

Um organizador de e-mails inteligente que automatiza a triagem e o resumo de mensagens usando IA, reduzindo o tempo gasto na leitura e priorização de e-mails.

## 🚀 Funcionalidades

- **Automação de E-mails:** Busca e processa automaticamente mensagens não lidas.
- **Classificação Inteligente:** Organiza e-mails em categorias relevantes.
- **Resumos Rápidos:** Gera descrições curtas para leitura eficiente.
- **Controle de Processamento:** Limita execuções diárias para evitar excessos.
- **Filtragem Automática:** Ignora conteúdos irrelevantes como promoções.
  
## ⚙️ Como funciona

1. Autenticação com a API do Gmail via OAuth2.
2. Coleta de e-mails não lidos da caixa de entrada.
3. Envio do conteúdo para a IA (Llama 3 via Groq).
4. Classificação e geração de resumo com base no contexto.
5. Persistência dos dados em `queue.json` para controle de execução.

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Gmail API:** Para leitura de e-mails.
- **Groq Cloud (Llama 3.1 8B):** Para processamento de linguagem natural ultra-rápido.
- **Pydantic/Type Hinting:** Para um código robusto e manutenível.
- **Python-dotenv:** Gerenciamento de variáveis de ambiente.

## 📋 Pré-requisitos

1. Uma conta no [Google Cloud Console](https://console.cloud.google.com/) com a Gmail API ativada.
2. Credenciais OAuth2 (arquivo `credentials.json`).
3. Uma chave de API da [Groq Cloud](https://console.groq.com/).

## 🔧 Instalação e Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/JPedrogrc/email-ai-organizer
   cd email-ai-organizer
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:
   - Renomeie `.env.example` para `.env`.
   - Adicione sua chave da Groq em `GROQ_API_KEY`.

5. Adicione seu arquivo `credentials.json` (baixado do Google Cloud) na raiz do projeto.

## 🏃 Como Usar

Execute o script principal:
```bash
python main.py
```
*Na primeira execução, uma aba do navegador abrirá para você autorizar o acesso à sua conta do Gmail.*

---
Desenvolvido por João Pedro Garcia - [LinkedIn](https://www.linkedin.com/in/jpedrogrc/)
