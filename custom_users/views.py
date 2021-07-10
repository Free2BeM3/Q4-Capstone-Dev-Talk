from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect, reverse
from custom_users.models import Uzer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from custom_users.forms import LoginForm, SignupForm, ProfileForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View
from uploads.models import Image 

# Create your views here

def home_view(request):
    posts = Image.objects.all()
    return render(request, 'index.html', {'posts':posts})



class SignUpView(View):

    def get(self, request):
        form = SignupForm()
        return render(request, "form.html", {'form': form})


    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = Uzer.objects.create_user(username=data['username'],
                                            password=data['password'],
                                            email=data['email'],
                                            first_name=data['first_name'],
                                            last_name=data['last_name'])
            user.save()
            return HttpResponseRedirect(reverse('homepage'))
    



class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, "form.html", {'form': form})

    def post(self, request):
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(
                    username=data['username'], password=data['password'])
                if user:
                    login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
            

def logout_view(request):
    log = logout(request)
    return redirect('homepage')


def profile_view(request, user_id: int):
    owner = Uzer.objects.get(id=user_id)
    followers = owner.followers.all()
    following = owner.following.all()
    posts = Image.objects.filter(author=owner)
    return render(request, 'profile.html', {'owner': owner, 'followers': followers, 'following': following, 'posts': posts})



class CreateProfileView(LoginRequiredMixin, View):

    def get(self, request, user_id):
        obj = Uzer.objects.get(id=user_id)
        data = {
                'avatar': obj.avatar,
                'bio': obj.bio,
                'location': obj.location,
                'github': obj.github,
                'linkedin': obj.linkedin,
                'portfolio': obj.portfolio,
            } 
        template_name = 'form.html'
        form = ProfileForm(initial=data)
        return render(request, template_name, {'form': form, 'header': 'Create Profile'})

    def post(self, request, user_id):
            obj = Uzer.objects.get(id=user_id)
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                data = form.cleaned_data
                profile = Uzer.objects.filter(id=user_id).update(
                    avatar=data.get('avatar'),
                    bio=data.get('bio'),
                    location=data.get('location'),
                    github=data.get('github'),
                    linkedin=data.get('linkedin'),
                    portfolio=data.get('portfolio')
                )
                
            return redirect(reverse('profile', args=[user_id]))
               
               
@login_required
def follow(request, user_id: int):
    user = Uzer.objects.get(id=user_id)
    follower = Uzer.objects.get(id=request.user.id)
    user.followers.add(follower)
    follower.following.add(user)
    
    return HttpResponseRedirect(reverse("profile", args=[user_id]))

    


@login_required
def unfollow(request, user_id: int):
    user = Uzer.objects.get(id=user_id)
    follower = Uzer.objects.get(id=request.user.id)
    user.followers.remove(follower)
    follower.following.remove(user)
    
    return HttpResponseRedirect(reverse("profile", args=[user_id]))

