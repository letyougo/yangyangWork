from django.shortcuts import render
from django.http.response import JsonResponse
from django.http.response import HttpResponseRedirect
# Create your views here.
from models import Course
def index(request):

    try :
        item = Course.objects.get(id=request.GET['id'])

        list = [c.to_obj() for c in Course.objects.all()]
        for i in range(0, len(list)):
            if request.GET['id'] == str(list[i]['id']):
                list[i]['className'] = 'active'
            else:

                list[i]['className'] = 'no-active'

        return render(request, 'index.html', dict(list=list,item=item.to_obj2()))
    except:
        id = Course.objects.first().id
        return HttpResponseRedirect('/?id='+str(id))



