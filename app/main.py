from flask import Flask, render_template, request, redirect, url_for
import socket
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']
        data = {'username': username, 'message': message}
        send_to_socket_server(data)
        return redirect(url_for('index'))
    return render_template('message.html')

def send_to_socket_server(data):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('socket_server', 5000))  # Всередині контейнера, порт залишається 5000
    client_socket.sendall(json.dumps(data).encode('utf-8'))
    client_socket.close()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
