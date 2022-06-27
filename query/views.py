from django.http import HttpResponse
from .models import Contract
network = ''
contract = ''
def querytotalSupply(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def importContract(request):
    contract = Contract.objects.create(address='123')
    return HttpResponse("ook")