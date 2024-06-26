# Secure Message Exchange with MITM Attack Detection and Digital Signature

## Description

This project develops a secure message exchange system incorporating Man-In-The-Middle (MITM) attack detection and digital signatures for authentication. It aims to ensure the confidentiality and integrity of messages exchanged over insecure channels.

## Features

- MITM attack detection
- Digital signatures for authentication
- Secure message exchange

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage
1- Generate Keys:
```bash
python gen_keys.py
```

2- Start the Server:
```bash
python simple_server.py
```

3- Start the Client:
```bash
python simple_client.py
```

4- Start the MITM Forwarder:
```bash
python mitm_forwarder.py
```

5- Start the MITM Attacker:
```bash
python mitm_attacker.py
```

## Contributing
Feel free to contribute by submitting a pull request.

## License
This project is licensed under the MIT License.

## Contact
Email: career.zainzaidi@gmail.com
