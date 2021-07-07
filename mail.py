from flask_mail import Mail, Message
import credentials

def create(app):
  mail = Mail(app)
  app.config['MAIL_SERVER'] = credentials.MAIL_SERVER
  app.config['MAIL_PORT'] = credentials.MAIL_PORT
  app.config['MAIL_USERNAME'] = credentials.MAIL_USERNAME
  app.config['MAIL_PASSWORD'] = credentials.MAIL_PASSWORD
  app.config['MAIL_USE_TLS'] = credentials.MAIL_USE_TLS
  app.config['MAIL_USE_SSL'] = credentials.MAIL_USE_SSL
  app.config['MAIL_DEFAULT_SENDER'] = credentials.MAIL_DEFAULT_SENDER
  mail = Mail(app)
  return mail