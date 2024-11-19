from django.shortcuts import render

# Create your views here.
# blog/views.py
from django.shortcuts import render
from django.http import JsonResponse

def json(request):
    data = {
        "title": "Hello, Django!",
        "content": "Esta é uma resposta JSON gerada por uma view do Django.",
        "author": "Admin",
        "created_at": "2024-10-27"
    }
    return JsonResponse(data)

def post_list(request):
    # Dados constantes para simular as postagens
    posts = [
        {
            'title': 'Primeira Postagem',
            'content': 'Conteúdo da primeira postagem.',
            'created_at': '2024-10-25'
        },
        {
            'title': 'Segunda Postagem',
            'content': 'Conteúdo da segunda postagem.',
            'created_at': '2024-10-26'
        },
        {
            'title': 'Terceira Postagem',
            'content': 'Conteúdo da terceira postagem.',
            'created_at': '2024-10-27'
        }
    ]
    # Envia os dados para o template
    return render(request, 'post_list.html', {'posts': posts, 'test': 'MY TEST'})

def about(request):
    return render(request, 'about.html', {'test': 'MY TEST'})
