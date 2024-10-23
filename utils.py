import json

def credentials_to_dict(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

def save_token(user, token, provider):
    if provider == 'google':
        user.google_token = json.dumps(token)
    elif provider == 'microsoft':
        user.microsoft_token = json.dumps(token)
