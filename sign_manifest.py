import os
import base64
import nacl.signing
import nacl.encoding

priv_key_hex = os.environ['ED25519_PRIVATE_KEY']
signing_key = nacl.signing.SigningKey(priv_key_hex, encoder=nacl.encoding.HexEncoder)

with open('manifest.json', 'rb') as f:
    data = f.read()

signed = signing_key.sign(data)
sig_b64 = base64.b64encode(signed.signature).decode('utf-8')

with open('manifest.sig', 'w', encoding='utf-8') as f:
    f.write(sig_b64)

print("manifest.sig успешно создан")
