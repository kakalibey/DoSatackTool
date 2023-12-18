from django.shortcuts import render
import subprocess
from django.http import JsonResponse
from .forms import CommandForm
# Create your views here.

def execute_command(request):
    if request.method == 'POST':
        form = CommandForm(request.POST)
        if form.is_valid():
            command = form.cleaned_data['command']
            try:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
                return JsonResponse({'result': output})
            except subprocess.CalledProcessError as e:
                return JsonResponse({'error': str(e)})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def home(request):
    return render(request, 'home.html')