from django.http import HttpResponse

def saludo(request):
    return HttpResponse("""
        <h1>Bienvenido a mi página</h1>
        <p>Esta es la presentación oficial del sitio web que estoy desarrollando con Django.</p>
        <p>Aquí vas a encontrar información, recursos y mucho más.</p>
    """)

