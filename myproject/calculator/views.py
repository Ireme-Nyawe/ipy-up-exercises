from django.http import HttpResponse

def add(request):

    if request.method == 'POST':

        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))

        result = num1 + num2

        return HttpResponse(f"Result: {result}")

    return HttpResponse("""
        <h2>Simple Calculator</h2>

        <form method="POST">
            <input type="number" step="any" name="num1"
                   placeholder="First number" required>

            <input type="number" step="any" name="num2"
                   placeholder="Second number" required>

            <button type="submit">Add Numbers</button>

            <input type="hidden" name="csrfmiddlewaretoken">
        </form>
    """)