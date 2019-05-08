from django.shortcuts import render
from django.http import HttpResponse
from .models import Touroku
from .forms import IdKensaku

def index(request):

    params = {
        'title':'筋トレ管理',
        'msg':'',
        'form':IdKensaku(),
        'data':[],
    }

    if (request.method =='POST'):
        number = request.POST['id']
        item = Touroku.objects.get(id = number)
        params['data'] = [item]
        params['form'] = IdKensaku(request.POST)
    else:
        params['data'] = Touroku.objects.all()
    return render(request, 'app1/index.html', params)
