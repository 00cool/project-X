from flask import Flask
from flask import request

def application:
    app = Flask(__name__)

    @app.route('/jump/<email>')
    def pair_email_ip(email):
        if(email == NULL):
            return("Provide a valid email address")
        else:
            E_IP_PAIR ["ip"] = request.client_conn

    if __name__ == "__main__":
        app.run()