from flask import Flask, request
from fbmsgbot.bot import Bot
from config.info import TOKEN

token = TOKEN
app = Flask(__name__)
bot = Bot(TOKEN)

@app.route('/webhook', methods=['GET', 'POST'])
def listen():
    """
    NOTE request.args returns a multilist AKA a dict {k: []} where 
    values are lists
    """
    return (
        verify_token(request) if request.method=='GET'
                              else receive_message(request))

def receive_message(request):
    msg = request.json['entry'][0]['messaging'][0]['message']['text']
    return msg

def verify_token(request):
    """ Vertify user """
    if request.args.get("hub.verify_token") == token:
        return request.args.get("hub.challenge")

    return 'Failure'

if __name__ == "__main__":
    app.run()