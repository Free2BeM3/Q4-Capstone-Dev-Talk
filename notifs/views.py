from django.shortcuts import render
from notifs.models import Notifs
from custom_users.models import Uzer

# Create your views here.


def notifs_view(request, pk):
    user = Uzer.objects.get(id=pk)
    notif = Notifs.objects.filter(reciever=user)
    return render(request, 'notifs.html', {'notifs': notif})
