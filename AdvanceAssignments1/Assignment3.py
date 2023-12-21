from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import random
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    emit('notification',f'{get_live_data()} is data',broadcast=True)
    for i in range(1,5):
        
        emit('notification',get_live_data(),broadcast=True)
        time.sleep(2)


def get_live_data():
   return random.uniform(4,100)
if __name__ == '__main__':
    socketio.run(app)