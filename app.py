from flask import Flask, render_template
from flask_socketio import SocketIO, emit



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)



@app.route('/')
def index():
   
    return render_template('index.html')  # Pass my_dict as a parameter

@socketio.on('connect')
def on_connect():
    socketio.emit('hello')

def on_emit_complete():
    print('Data has been sent to the client.')
    
@socketio.on('chat message')
def handle_chat_message(msg):
    socketio.emit('chat message', msg)


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, debug=True)
    # print(type(socketio.run()))
