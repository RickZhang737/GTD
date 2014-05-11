from django.shortcuts import render
from django.http import HttpResponse
from pomodoro.models import Activity

def inventory(request):
    activity_list = Activity.objects.all().filter(status='0')
    context = {'activity_list': activity_list}
    return render(request, 'pomodoro/inventory.html', context)