# ################# Deploying Flask in Ubuntu ####################################################################################################################################
# sudo apt update 
# sudo apt install python3 python3-pip python3-venv 
# mkdir flask-app && cd flask-app 
# python3 -m venv venv
# source venv/bin/activate
# pip3 install Flask 
# python3 -m flask --version 
################## app.py #######################################################################################################################################################################
import flask
import time
import socket

h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)

app = flask.Flask(__name__)

@app.route('/')
def index():
        Time= time.strftime("%H:%M:%S")
        return Time+" Serving from "+h_name+" ("+IP_addres+")\n"
#
if __name__=='__main__':
        app.run(host='0.0.0.0', port=5000,debug=True)
