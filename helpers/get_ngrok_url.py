import requests
import json

ngrok_api_url = "http://127.0.0.1:4040/api/tunnels"

def get_ngrok_url():
    try:
       response = requests.get(ngrok_api_url)
       if response.status_code == 200:
            data = json.loads(response.text)
            tunnels = data["tunnels"]
            if tunnels:
               for tunnel in tunnels:
                   if tunnel["proto"] == "https":
                       return tunnel["public_url"]
            else:
               return None
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    
ngrok_url = get_ngrok_url()

if ngrok_url:
    print(f"NGROK URL: {ngrok_url}")
else:
    print("not found")