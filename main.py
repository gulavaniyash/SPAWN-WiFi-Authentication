import hashlib
import time
import os
import socket
import threading
import hmac
import graphs

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

SECRET_KEY = b"mysecretkey"


# ---------------- Temp-ID ----------------
def generate_temp_id(device_id):
    nonce = os.urandom(8).hex()
    timestamp = str(time.time())
    data = device_id + nonce + timestamp
    temp_id = hashlib.sha256(data.encode()).hexdigest()
    return temp_id, nonce, timestamp


# ---------------- HMAC ----------------
def generate_hmac(message):
    return hmac.new(SECRET_KEY, message.encode(), hashlib.sha256).hexdigest()


# ---------------- ECC ----------------
def generate_ecc_keys():
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()
    return private_key, public_key


def serialize_public_key(public_key):
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )


def deserialize_public_key(public_bytes):
    return serialization.load_pem_public_key(public_bytes)


# ---------------- SERVER ----------------
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 5000))
    server.listen(1)

    print("\n[AP] Waiting for client...")

    conn, addr = server.accept()
    print("[AP] Connected with client:", addr)

    data = conn.recv(4096).decode()
    parts = data.split("|")

    message = "|".join(parts[:-2])
    received_hmac = parts[-2]
    client_pub_key_bytes = parts[-1].encode()

    if generate_hmac(message) == received_hmac:
        print("[AP] HMAC Verified ✅")
    else:
        print("[AP] HMAC Failed ❌")

    ap_private, ap_public = generate_ecc_keys()
    client_public = deserialize_public_key(client_pub_key_bytes)

    shared_key = ap_private.exchange(ec.ECDH(), client_public)
    print("[AP] Shared Key:", shared_key.hex())

    ap_pub_bytes = serialize_public_key(ap_public)
    conn.send(ap_pub_bytes)

    conn.close()
    server.close()


# ---------------- CLIENT ----------------
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 5000))

    device_id = "AA:BB:CC:DD:EE:FF"

    temp_id, nonce1, timestamp = generate_temp_id(device_id)
    message = f"{temp_id}|{nonce1}|{timestamp}"

    mac = generate_hmac(message)

    client_private, client_public = generate_ecc_keys()
    client_pub_bytes = serialize_public_key(client_public)

    full_message = f"{message}|{mac}|".encode() + client_pub_bytes

    print("\n[Client] Sending Temp-ID + HMAC + Public Key")
    client.send(full_message)

    ap_pub_bytes = client.recv(4096)
    ap_public = deserialize_public_key(ap_pub_bytes)

    shared_key = client_private.exchange(ec.ECDH(), ap_public)
    print("[Client] Shared Key:", shared_key.hex())

    client.close()


# ---------------- MAIN ----------------
if __name__ == "__main__":
    start_time = time.time()

    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    time.sleep(1)

    start_client()

    end_time = time.time()

    latency_ms = (end_time - start_time) * 1000
    print("\nLatency:", latency_ms, "ms")

    # Generate graphs automatically
    graphs.plot_graphs(latency_ms)