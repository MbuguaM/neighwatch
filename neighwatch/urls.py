"""neighwatch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from watch import views as auth_views
from watch.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('watch.urls')),
    # entrry urls
    url(r'^accounts/login/$', views.LoginView.as_view(template_name = 'registration/login.html', authentication_form = LoginForm,  ), name='login'),
    url(r'^signup/$', auth_views.signup, name='signup'),
    url(r'^logout/$', views.logout, {'next_page': 'login'}, name='logout'),
    # mail confimation urls
    url(r'^account_activation_sent/$', auth_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.activate, name='activate'), 
]
