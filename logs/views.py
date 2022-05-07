from django.shortcuts import render, redirect
from . models import Log
from .forms import EntryForm

# Create your views here.
def logs(request):
    """Index of logs by date"""
    user_logs = Log.objects.filter(owner=request.user).order_by('date_added')
    context = {'logs': user_logs}
    return render(request, 'logs/logs.html', context)

def log_entry(request, log_id):
    """An individual log entry"""
    entry = Log.objects.get(id=log_id)
    context = {'log': entry}
    return render(request, 'logs/log_entry.html', context)

def new_entry(request):
    """Create a new log entry"""
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_log_entry = form.save(commit=True)  # commit = True means save to db
            return redirect('logs:logs')

    context = {'form': form}
    return render(request, 'logs/new_entry.html', context)

def edit_entry(request, log_id):
    """Edit an existing log entry"""
    entry = Log.objects.get(id=log_id)

    if request.method != 'POST':
        # Fill new form with existing content to edit
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('logs:logs')

    context = {'log': entry, 'form': form}
    return render(request, 'logs/edit_entry.html', context)

