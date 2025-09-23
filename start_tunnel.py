import os
import certifi
from pyngrok import ngrok, conf

# Ensure Python uses certifi's CA bundle for HTTPS requests
os.environ.setdefault("SSL_CERT_FILE", certifi.where())
os.environ.setdefault("REQUESTS_CA_BUNDLE", certifi.where())

# Optional: use authtoken from env var NGROK_AUTHTOKEN if present
AUTHTOKEN = os.environ.get("NGROK_AUTHTOKEN")
if AUTHTOKEN:
    conf.get_default().auth_token = AUTHTOKEN

# Start an HTTP tunnel to localhost:5002
public_url = ngrok.connect(addr=5002, proto="http")
print(f"Tunnel started: {public_url.public_url}")

# Persist URL to instance/tunnel_url.txt for easy access
instance_dir = os.path.join(os.path.dirname(__file__), "instance")
os.makedirs(instance_dir, exist_ok=True)
with open(os.path.join(instance_dir, "tunnel_url.txt"), "w") as f:
    f.write(public_url.public_url)

# Keep the tunnel open
try:
    import time
    while True:
        time.sleep(3600)
except KeyboardInterrupt:
    pass
finally:
    ngrok.disconnect(public_url.public_url)
    ngrok.kill()
