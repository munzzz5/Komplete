from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import getActionUrls

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()
    body = request.values.get('Body', None)
    # Add a message

    if 'learn' in body or 'Learn' in body:
        x = getActionUrls.filteredResultMethod(str(body))
        displayString = ""
        for i in range(5):
            displayString += str(x['Title'][i])+"\n"+str(x["Link"][i])+"\n\n\n"

        resp.message(displayString)
    # resp.redirect('https://demo.twilio.com/welcome/sms/')

    return str(resp)


# def startServer():
#     from twilio.rest import Client
#     from pyngrok import ngrok
#     url = ngrok.connect(5000).public_url
#     print(url)
#     client = Client('AC57b5b2abed9c0e4b2f31daef947dfecf',
#                     'a78f3259eaca573c752940b630978957')
#     print([x for x in client.incoming_phone_numbers.list(
#         phone_number='+13124677853')])
#     client.incoming_phone_numbers.list(
#         phone_number='+14155238886')[0].update(sms_url=url+"/sms")


if __name__ == "__main__":

    app.run(debug=True, threaded=True)
