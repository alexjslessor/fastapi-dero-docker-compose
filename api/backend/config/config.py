"""backend.config"""
'''https://fastapi.tiangolo.com/advanced/settings/'''
import functools
from pydantic import BaseSettings
from os import environ
from typing import List

class _BaseSettings(BaseSettings):
    '''Settings Docs: https://pydantic-docs.helpmanual.io/usage/settings/'''
    PORT: int = 8080
    SECRET = 'asd32el23mr2lwmfe'
    MIN_PASSWORD_LEN: int = 8
    MAIL_PORT: int = 465
    MAIL_SERVER: str = 'in-v3.mailjet.com'
    MAIL_TLS: bool = False
    MAIL_SSL: bool = True  
    MAILJET_SENDER: str = 'email@gmail.com'
    OID_ERROR: str = 'Please try again later.'

    DERO_DAEMON_URI: str = 'http://dero:20209/json_rpc'
    DERO_WALLET_URI: str = 'http://dero-wallet:20206/json_rpc'
    # url2 = 'http://localhost:20209/json_rpc'
    # url2 = 'http://blockchain:20209/json_rpc'
    # url2 = 'http://dero:20209/json_rpc'
    # url4 = 'http://localhost:20209/json_rpc'

class DevSettings(_BaseSettings):
    CORS_ORIGINS: List[str] = ["*"]
    URL_NAME = 'http://0.0.0.0:8080'
    DATABASE_URL = ""
    DB_NAME: str = 'dero-users'
    MAIL_USERNAME: str = ''
    MAIL_PASSWORD: str = ''
    NOTIFICATION_EMAIL_LIST: List[str] = ['email@gmail.com']
    OPENAPI_URL: str = '/docs_openapi'
    DOCS_URL: str = '/docs'
    REDOC_URL: str = '/redoc_url'

    KOMODO_CLI: str = str(environ.get('KOMODO_CLI'))
    PIRATE_USER: str = str(environ.get('PIRATE_USER'))
    PIRATE_PASSWORD: str = str(environ.get('PIRATE_PASSWORD'))


@functools.lru_cache()
def get_settings(**kwargs) -> BaseSettings:
    return DevSettings(**kwargs)