from django.shortcuts import render
from . models import Log

# Create your views here.
def logs(request):
    """Index of logs by date"""
    user_logs = Log.objects.filter(owner=request.user).order_by('date_added')
    context = {'logs': user_logs}
    return render(request, 'logs/logs.html', context)