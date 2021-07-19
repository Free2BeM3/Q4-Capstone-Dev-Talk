from django.dispatch.dispatcher import receiver
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from uploads.models import Image, Comment
from uploads.forms import ImageForm, AddCommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from notifs.models import Notifs

@login_required
def AddPostView(request):
    if request.method == 'POST':

        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            post = Image.objects.create(
                caption=data['caption'],
                image=data['image'],
                author=request.user,
            )
        return HttpResponseRedirect(reverse('homepage'))
    form = ImageForm()
    return render(request, 'form.html', {'form': form})

@login_required
def AddComment(request, pk):
    target_post = Image.objects.get(pk=pk)
    if request .method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            posts = Comment.objects.create(
                sender=request.user,
                post=target_post,
                body=data['body']
            )
        commenter = request.user
        owner = target_post.author
        message = "Just commented on your Post."
        if commenter != owner:
            notify = Notifs.objects.create(
                reciever=owner, sender=commenter, comment=posts, message=message)
        return HttpResponseRedirect(reverse('homepage'))

    form = AddCommentForm()
    return render(request, 'form.html', {'form': form})

@login_required
def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.user.id == comment.sender.id:
        comment.delete()
        return redirect('homepage')

@login_required
def post_likes(request, pk):
    post = Image.objects.get(pk=pk)
    owner = post.author
    user = request.user
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        if user != owner:
            message = "Just liked your post."
            notify = Notifs.objects.create(
                reciever=owner, sender=user, message=message)
    return HttpResponseRedirect(reverse('homepage'))
