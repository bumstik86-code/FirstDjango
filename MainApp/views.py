from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    author_name = 'Сиволобов И. В.'
    html_content = f'''
    <h1>Изучаем django</h1>
    <strong>Автор</strong>: <i>{author_name}</i>
    '''
    return HttpResponse(html_content)