from django.shortcuts import render
from historico.models import Historico
from django.http import HttpResponse
from .forms import Numero



# Create your views here.
def index(request):

    # Setagens
    numero = 0
    num = 0
    nums = []
    z = 0
    primo = True

    if request.method=="GET":
        try:
            numero = request.GET['campo_numero']
        except:
            numero = 0

    num = int(numero)
    # Loop para listar os divisores.
    for x in range((num // 2) + 1):
        if x > 0:
            if (num / x) == (num // x): 
                nums.append(x)
    if num != 0: nums.append(num)

    #Se tiver 2 divisores armazenados em y é primo, senão não
    if (len(nums) == 2):
        primo = True
    else:
        primo = False
    

    context = {'nums': nums, 'num': num, 'numero': numero }

    if num > 0:
        numeros = Historico(num=num, primo=primo)
        numeros.save()

    return render(request, "calculo/index.html", context)