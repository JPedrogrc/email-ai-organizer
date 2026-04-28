import os
import json
from typing import List, Dict, Any
from gmail_service import get_gmail_service
from utils import get_email_body
from ai_classifier import classify_email

# --- CONFIGURAÇÕES ---
MAX_EMAILS = 15
QUEUE_FILE = 'queue.json'

def load_queue() -> List[Dict[str, str]]:
    """Carrega a fila de IDs do arquivo JSON."""
    if os.path.exists(QUEUE_FILE):
        with open(QUEUE_FILE, 'r') as f:
            return json.load(f)
    return []

def save_queue(queue: List[Dict[str, str]]) -> None:
    """Salva a lista de IDs no arquivo JSON."""
    with open(QUEUE_FILE, 'w') as f:
        json.dump(queue, f, indent=4)

def main() -> None:
    service = get_gmail_service()
    queue = load_queue()
    
    # Filtro: Apenas não lidos, ignorando abas de promoções/social
    query_filter = "is:unread -category:promotions -category:social -category:forums"
    print("Buscando novos e-mails...")
    
    results = service.users().messages().list(userId='me', q=query_filter, maxResults=50).execute()
    new_messages = results.get('messages', [])
    
    # Adicionar novos IDs à fila evitando duplicidade
    existing_ids = {item['id'] for item in queue}
    for msg in new_messages:
        if msg['id'] not in existing_ids:
            queue.append({"id": msg['id']})
            
    # Lote de processamento
    batch_to_process = queue[:MAX_EMAILS]
    queue_to_save = queue[MAX_EMAILS:]
    
    save_queue(queue_to_save)
    
    print(f"\nStatus: {len(batch_to_process)} e-mails para processar.")
    print(f"Fila: {len(queue_to_save)} e-mails aguardando.\n")
    
    for item in batch_to_process:
        try:
            message = service.users().messages().get(userId='me', id=item['id']).execute()
            body = get_email_body(message)
            
            if body:
                result = classify_email(body)
                print(f"--- EMAIL ID: {item['id']} ---")
                print(result)
                print("-" * 30)
                
        except Exception as e:
            print(f"Erro ao processar o e-mail {item['id']}: {e}")

if __name__ == "__main__":
    main()