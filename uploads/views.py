from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from uploads.models import Image
from uploads.forms import ImageForm


# Create your views here
# def upload_view(request):
#     if request.method == "POST":
#         form=ImageForm(data=request.POST,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             obj=form.instance
#             return HttpResponseRedirect('uploads.html')
#     else:
#         form = ImageForm()
#         img=Image.objects.all()
#     return render(request, 'form.html', {'img':img,'form':form})

def AddPostView(request):
    if request.method == 'POST':

        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            post = Image.objects.create(
                caption=data['caption'],
                image=data['image'],
                author= request.user,
        )
        return HttpResponseRedirect(reverse('homepage'))
    form = ImageForm()
    return render(request, 'form.html', {'form': form})