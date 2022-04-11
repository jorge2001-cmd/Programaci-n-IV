from flask import Flask, render_template, redirect, url_for
from flask_mail import Mail,  Message

app = Flask(__name__)
app.config.update(
    MAIL_SERVER='prueba@gmail.com',
    MAIL_PORT=587,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'jorgeisaacyt24@gmail.com',
    MAIL_PASSWORD = 'Zeus2019'
)

mail = Mail(app)

@app.route('/send-mail/')
def send_mail():
    msg = mail.send_message(
        'Send Mail tutorial!',
        sender='jorgeisaacyt24@gmail.com',
        recipients=['jorge.galvez@msn.com'],
        body="Congratulations you've succeeded!"
    )
    return 'Mail sent'
