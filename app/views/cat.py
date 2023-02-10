from django.shortcuts import render, redirect
from app.cat import Cat


def home(request):
    if request.method == 'POST':
        Cat.name = request.POST['name']
        return redirect('/cat')
    return render(request, 'index.html')


def cat(request):
    if request.method == 'POST':
        action = request.POST['action']
        if action == 'feed':
            Cat.feed()
        elif action == 'play':
            Cat.play()
        elif action == 'sleep':
            Cat.sleep()
        Cat.update_avatar()
    return render(request, 'cat.html', {
        'cat': Cat
    })
