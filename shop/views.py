from django.shortcuts import render, render_to_response
from .models import Item


def items(request):
    item = Item.objects.all()[:10]
    username = request.user.username
    return render_to_response('item.html', {'list': item, 'username': username})
