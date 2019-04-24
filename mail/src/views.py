# -*- coding: utf-8 -*-
from flask import (
    Blueprint,
    current_app,
    request,
    jsonify,
)
from flask_mail import Message

blueprint = Blueprint('v1', __name__)

DEFAULR_SENDER = current_app.config['MAIL_USERNAME']


@blueprint.route('/mail/send/<receiver>')
def send_basic_email(receiver):
    result = {'rc': -1}
    try:
        sender = DEFAULR_SENDER
        if not receiver:
            receiver = DEFAULR_SENDER
        subject = "Test flask-mail"
        body = "send by flask"

        msg = Message(
            subject=subject,
            body=body,
            sender=sender,
            recipients=[receiver]
        )
        with current_app.mail.record_messages() as outbox:
            current_app.mail.send(msg)
            if len(outbox) >= 1:
                if outbox[0].subject == subject:
                    result['rc'] = 0
                    return jsonify(result)
            result['message'] = 'Failed to send email'
            return jsonify(result)
    except Exception as e:
        result['message'] = str(e)
        return jsonify(result)
