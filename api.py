from flask import Flask, request
from flask_mail import Mail, Message
from flask_cors import CORS, cross_origin

import credentials
import mail

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

mail_handler = mail.create(app)

#Start of endpoints

@app.route("/enquiry", methods=["POST"])
@cross_origin()
def enquiry_email():
  if request.get_json():
    msg = Message('Website Enquiry: ' + str(request.get_json()['name']), reply_to=request.get_json()['email'], recipients = ['cally@cally.dev'])
    msg.body = request.get_json()['msg']
    mail_handler.send(msg)
    return "Sent"
  else:
    return 'ERROR'

if __name__ == '__main__':
   app.run(debug = True)