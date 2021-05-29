from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def home(request):
    
    context = {
        'user': User.objects.get(id=request.session['id']),
        'wishes': User.objects.get(id=request.session['id']).wishes.all(),
        'granted_wishes': Granted_wish.objects.all()
    }
    return render(request, 'wish/home.html', context)

def new(request):
    context = {
        'user': User.objects.get(id=request.session['id'])
    }
    return render(request, 'wish/new.html', context)



def stats(request):
    context = {
        'user': User.objects.get(id=request.session['id']),
        'granted_wishes': Granted_wish.objects.count(),
        'user_granted_wishes': User.objects.get(id=request.session['id']).granted_wishes.count(),
        'user_pending_wishes': User.objects.get(id=request.session['id']).wishes.count()
    }
    return render(request, 'wish/stats.html', context)


def logout(request):
    if request.method == 'POST':
        request.session.clear()
        return redirect('/')
    else:
        return redirect('/')

def new_wish(request):
    if request.method == 'POST':
        errors = Wish.objects.wish_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/wish/new')
        else:
            Wish.objects.create(item=request.POST['item'], desc=request.POST['desc'], user=User.objects.get(id=request.POST['user_id']))
            return redirect('/wish/home')
    else:
        return redirect('/')

def grant(request):
    if request.method == 'POST':
        Granted_wish.objects.create(item=request.POST['wish_item'], user=User.objects.get(id=request.POST['user_id']), date_added=request.POST['wish_created'])
        wish = Wish.objects.get(id=request.POST['wish_id'])
        wish.delete()
        return redirect('/wish/home')
    else:
        return redirect('/')

def edit(request, id):
    context = {
        'user': User.objects.get(id=request.session['id']),
        'wish': Wish.objects.get(id=id)
    }
    return render(request, 'wish/edit.html', context)

def update(request, id):
    if request.method == 'POST':
        errors = Wish.objects.wish_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/edit/id')
        else:
            wish = Wish.objects.get(id= id)
            wish.item = request.POST['item']
            wish.desc = request.POST['desc']
            wish.save()
            return redirect('/wish/home')    
    else:
        return redirect('/')

def like(request):
    if request.method == 'POST':
        granted = Granted_wish.objects.get(id=request.POST['grant_id'])
        user = User.objects.get(id=request.POST['user_id'])
        if granted.user_id == user.id:
            messages.error(request, "Users may not like their own wishes.")
            return redirect('/wish/home')
        if len(granted.likes.filter(id=request.POST['user_id'])) > 0:
            messages.error(request, "You have already liked this wish.")
            return redirect('/wish/home')
        else:
            granted.likes.add(user)
            return redirect('/wish/home')

def delete(request):
    if request.method == 'POST':
        wish = Wish.objects.get(id=request.POST['wish_id'])
        wish.delete()
        return redirect('/wish/home')
    else:
        return redirect('/')