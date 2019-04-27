"""
APP - Flask server endpoint

Sets up a super-simple HTTP POST endpoint, for the
GroupMe API to ping with new messages from the group

Flask parts were made almost entirely with this tutorial:
http://www.apnorton.com/blog/2017/02/28/How-I-wrote-a-Groupme-Chatbot-in-24-hours/
"""
import firstblood as bot
from flask import Flask, Request
app = Flask(__name__)


@app.route("/", methods=['POST','GET'])
def webhook():
    data = Request.get_json()

    if data['name'] != "Groupmebot":
        # msg = 'You (name={}) sent "{}"'.format(data['name'], data['text'])
        # send_message(msg)
        bot.incoming_message(data)

    return "ok", 200


# (use for debugging; GET only)
# @app.route("/")
# def hello():
#     return "Hello world!"

if __name__ == '__main__':
    app.run()