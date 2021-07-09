from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from uploads.models import Image, Comment
from uploads.forms import ImageForm, AddCommentForm
from django.contrib.auth.mixins import LoginRequiredMixin

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

#class AddComment(LoginRequiredMixin,View):
def AddComment(request, pk):
    target_post = Image.objects.get(pk = pk)
    if request .method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            posts = Comment.objects.create(
            sender = request.user,
            post = target_post,
            body = data['body']
        )
        return HttpResponseRedirect(reverse('homepage'))

    form = AddCommentForm()
    return render(request, 'form.html', {'form': form})