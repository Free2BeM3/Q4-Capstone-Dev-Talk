from django.shortcuts import render
from notifs.models import Notifs
from custom_users.models import Uzer
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def notifs_view(request):
    notif = Notifs.objects.filter(
        reciever=request.user).filter(user_has_seen=False)
    notif_list = list(Notifs.objects.filter(
        reciever=request.user).filter(user_has_seen=False))
    Notifs.user_has_seen.update = True
    return render(request, 'notifs.html', {'notifs': notif})
