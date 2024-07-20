import socket
import json
from datetime import datetime
from pymongo import MongoClient
import logging

client = MongoClient('mongodb://mongo:27017/')
db = client.messages_db
collection = db.messages

logging.basicConfig(level=logging.DEBUG)

def handle_client_connection(client_socket):
    try:
        request = client_socket.recv(1024)
        data = json.loads(request.decode('utf-8'))
        data['date'] = datetime.now().isoformat()
        logging.debug(f"Received data: {data}")
        collection.insert_one(data)
        logging.info(f"Data inserted into MongoDB: {data}")
        client_socket.close()
    except Exception as e:
        logging.error(f"Error handling client connection: {e}")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5000))
    server_socket.listen(5)
    logging.info('Socket server is listening on port 5000...')
    
    while True:
        client_socket, addr = server_socket.accept()
        logging.debug(f"Accepted connection from {addr}")
        handle_client_connection(client_socket)

if __name__ == '__main__':
    main()
