from django.shortcuts import redirect, render, HttpResponseRedirect, reverse
from custom_users.models import Uzer
from django.contrib.auth.mixins import LoginRequiredMixin
from custom_users.forms import LoginForm, SignupForm, ProfileForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View
from uploads.models import Image 

# Create your views here.

def home_view(request):
    posts = Image.objects.all()
    return render(request, 'home.html', {'posts':posts})

def signup_view(request):
    if request.method == 'POST':
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
    form = SignupForm()
    return render(request, "form.html", {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))

    form = LoginForm()
    return render(request, "form.html", {'form': form})


def logout_view(request):
    log = logout(request)
    return redirect('homepage')


def profile_view(request, user_id: int):
    owner = Uzer.objects.get(id=user_id)
    followers = owner.followers.all()
    following = owner.following.all()
    return render(request, 'profile.html', {'owner': owner, 'followers': followers, 'following': following})



class CreateProfileView(LoginRequiredMixin, View):

    def get(self, request, user_id):
        obj = Uzer.objects.get(id=user_id)
        data = {
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
            form = ProfileForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                profile = Uzer.objects.filter(id=user_id).update(
                    bio=data.get('bio'),
                    location=data.get('location'),
                    github=data.get('github'),
                    linkedin=data.get('linkedin'),
                    portfolio=data.get('portfolio')
                )
                return redirect(reverse('homepage'))
               
               


# class EditProfileView(LoginRequiredMixin, View):

#     def get(self, request, profile_id)