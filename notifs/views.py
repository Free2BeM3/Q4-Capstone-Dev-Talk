from django.shortcuts import render
from notifs.models import Notifs
from custom_users.models import Uzer

# Create your views here.


def notifs_view(request):
    notif = Notifs.objects.filter(
        reciever=request.user).filter(user_has_seen=False)
    notif_list = list(Notifs.objects.filter(
        reciever=request.user).filter(user_has_seen=False))
    Notifs.user_has_seen.update = True
    return render(request, 'notifs.html', {'notifs': notif})
