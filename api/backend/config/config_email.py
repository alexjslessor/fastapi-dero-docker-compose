from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from .config import get_settings

settings = get_settings()


async def get_email_config(_from, _recipients, _cc, _subject, _email_body):
    
    email_conf = ConnectionConfig(MAIL_USERNAME=settings.MAIL_USERNAME, 
                                  MAIL_PASSWORD=settings.MAIL_PASSWORD, 
                                  MAIL_FROM=settings.MAILJET_SENDER,
                                  MAIL_PORT=settings.MAIL_PORT, 
                                  MAIL_SERVER=settings.MAIL_SERVER, 
                                  MAIL_FROM_NAME=_from, 
                                  MAIL_TLS=settings.MAIL_TLS,
                                  MAIL_SSL=settings.MAIL_SSL)
    
    message = MessageSchema(subject=_subject,
                            recipients=_recipients,
                            body=_email_body,
                            cc=_cc,
                            subtype="html")
    
    fm = FastMail(email_conf)
    await fm.send_message(message)        
