from django.shortcuts import render
from django.http import HttpResponse

def add(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))

        result = num1 + num2

        return HttpResponse(f"Result: {result}")

    return render(request, 'calculator/index.html')