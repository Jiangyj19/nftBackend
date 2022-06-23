from http.client import HTTPResponse
from django.http import JsonResponse
import json
from web3.auto import w3
from django.shortcuts import render
from eth_account.messages import encode_defunct
from web3 import Web3
msg = "I♥SF"
private_key = "1097357688da8d96a32e11037cc1b53a77db5bb26ed860cfc304a0941c7cbbfa"
message = encode_defunct(text=msg)
signed_message = w3.eth.account.sign_message(message, private_key=private_key)
msghash = Web3.toHex(signed_message.messageHash)
signature = signed_message.signature.hex()
def getCoupon(request):
    j = {"msg":msghash,"sig":signature}
    return JsonResponse(j)