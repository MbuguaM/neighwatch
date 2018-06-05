from django.shortcuts import render
# display dependencies 
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect, HttpResponseRedirect
# token dependencies 
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .forms import SignUpForm
from .tokens import account_activation_token
from .models import User_prof,Neighborhood,Bussiness
from django.contrib.auth.models import User
from django.contrib.auth import login
# decorators 
from django.contrib.auth.decorators import login_required
# Create your views here.


# Create your views here.
def signup(request):
    """ registration for the user """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your neighwatch Account'
            message = render_to_string('registration/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})



def account_activation_sent(request):
    """ view function to redirect user to the user registration complete page """
    current_user = request.user
    if current_user.is_authenticated():
        return HttpResponseRedirect('/')
    return render(request, 'registration/activation_complete.html')

def activate(request, uidb64, token):
    """ funtction to authenticate user activation from the email """
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'registration/activation_invalid.html')

@login_required
def home(request):
    """ displays the home page for all users """
    current_user = request.user

    # return_list = []
    # for image in all_images:
    #     return_list.append((image, image.image_likes.filter(profile_owner=request.user)))

    return render(request,'main_templates/landing.html',{'user':current_user})


@login_required
def neighborhoods(request):
    """ view all the avaliable neighbourhoods  and form to add new neighbourhood"""
    current_user = request.user
    
    
    return render(request,'main_templates/neighborhoods.html')


@login_required
def view_neigh(request):
    """ view all the details of a certain neighborhood and commenting """
    current_user = request.user
    
    return render(request,'main_templates/view_neigh.html')


@login_required
def bussinesses(request):
    """ view all the avaliable bussinesses  and form to add new bussiness"""
    current_user = request.user
    
    
    return render(request,'main_templates/view_bussiness.html')


@login_required
def view_buss(request):
    """ view all the details of a certain bussiness and commenting """
    current_user = request.user
    
    return render(request,'main_templates/view_buss.html')


@login_required
def search(request):
    """ displays the landing page """
    current_user = request.user

    return render(request,'main_templates/search.html')

@login_required
def view_user(request):
    """ displays user infomation """
    current_user = request.user

    return render(request,'main_templates/view_user.html')


@login_required
def update_user(request):
    """ displays user infomation """
    current_user = request.user

    return render(request,'main_templates/update_user.html')