from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from uploads.models import Image
from uploads.forms import ImageForm

# Create your views here.
def upload_view(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return HttpResponseRedirect('uploads.html')
    else:
        form = ImageForm()
        img=Image.objects.all()
    return render(request, 'form.html', {'img':img,'form':form})
