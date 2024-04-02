import requests

import json

from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

class Credentials:
    consumer_key = 'ahly43tjOUkoWvVqOy05ieudJ5MKADV39GOZI9CQZGMPCkCh'
    consumer_secret = 'oPTsjG2tQAAlngX4fCWEBxqpUbjnwVU49usYAuJ6B0xVu3uIN5qvCUaYYCgyeGf1'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    t = requests.get(Credentials.api_URL, auth=HTTPBasicAuth(Credentials.consumer_key, Credentials.consumer_secret))

    if t.status_code == 200:
        mpesa_access_token = json.loads(t.text)
        validated_mpesa_access_token = mpesa_access_token['access_token']
    else:
        print("Failed to retrieve Mpesa access token. Status code:", t.status_code)
        validated_mpesa_access_token = None  # or handle the error appropriately

class MpesaPassword:
    pay_time = datetime.now().strftime('%Y%m%d%H%M%S')
    short_code = '174379'
    OffSetValue = '0'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

    encode = short_code + passkey + pay_time

    encode = base64.b64encode(encode.encode())
    decoded = encode.decode('utf-8')