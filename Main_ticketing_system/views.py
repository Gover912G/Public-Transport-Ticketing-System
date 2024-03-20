from django.shortcuts import render
import requests

from .credentials import MpesaPassword, MpesaAccessToken

def home(request):
    return render(request, 'main/index.html', {'nav':'home'})

def Stk(request):
    if request.method =="POST":
        phone = request.POST['name']
        amount = request.POST.get('amount')
        access_token = MpesaAccessToken.validated_access_token
        api_URL = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
                "BusinessShortCode": MpesaPassword.short_code,
                "Password": MpesaPassword.decoded,
                "Timestamp": MpesaPassword.pay_time,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": amount,
                "PartyA": phone,
                "PartyB": MpesaPassword.short_code,
                "PhoneNumber": phone,
                "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
                "AccountReference": "Dondaa Fare Services",
                "TransactionDesc": "Transport Charges"
            }
        response = requests.post(api_url, json=request, headers=headers)


    return HttpResponse("success")
