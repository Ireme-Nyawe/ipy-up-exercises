from django.http import HttpResponse

def greet(request):
    name = request.GET.get('name')

    if name:
        return HttpResponse(f"Hello {name}! Welcome to Django.")

    return HttpResponse("""
        <form method="GET">
            <h2>Enter your name</h2>
            <input type="text" name="name" placeholder="Your name">
            <button type="submit">Greet Me</button>
        </form>
    """)