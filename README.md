# 📧 AI Email Organizer

Um organizador de e-mails inteligente que utiliza a **API do Gmail** para buscar mensagens não lidas e a **IA (Llama 3 via Groq)** para classificar e resumir automaticamente seu conteúdo.

## 🚀 Funcionalidades

- **Integração com Gmail:** Busca e-mails automaticamente usando OAuth2.
- **Classificação Inteligente:** Categoriza e-mails em `Faculdade`, `Programação`, `Importante` ou `Promoção/Lixo`.
- **Resumos Concisos:** Gera resumos de uma única linha para leitura rápida.
- **Gerenciamento de Fila:** Sistema de persistência local (`queue.json`) para respeitar limites de processamento diário.
- **Filtros Personalizados:** Ignora automaticamente e-mails de abas de Promoções e Redes Sociais.

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
   git clone https://github.com/seu-usuario/email-ai-organizer.git
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
Desenvolvido por [João Pedro Garcia] - [Seu LinkedIn]
