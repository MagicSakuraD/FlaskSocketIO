from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import logging


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
app.logger.setLevel(logging.DEBUG)




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

num = "old value北极🤞"
app.logger.debug(num)
@socketio.on('change value')
def handle_change_value(new_value):
    # 在这里处理接收到的新值，例如修改相应的变量
    num = new_value
    app.logger.debug(num)



if __name__ == '__main__':
    socketio.run(app, debug=True)
    # print(type(socketio.run()))
