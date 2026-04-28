import base64
from typing import Any, Dict

def get_email_body(message: Dict[str, Any]) -> str:
    """Extrai o conteúdo de texto de uma mensagem do Gmail."""
    payload = message.get('payload', {})
    parts = payload.get('parts', [])
    
    # Caso 1: E-mail multipart (comum)
    if parts:
        for part in parts:
            if part['mimeType'] == 'text/plain':
                data = part['body'].get('data', '')
                return base64.urlsafe_b64decode(data).decode('utf-8')
    
    # Caso 2: E-mail simples (sem parts)
    else:
        data = payload.get('body', {}).get('data', '')
        if data:
            return base64.urlsafe_b64decode(data).decode('utf-8')
    
    return ""