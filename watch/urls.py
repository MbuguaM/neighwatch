from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
  #landin page 
  
  # urls for neighbourhoods
  url(r'^$',views.neighborhoods, name ="home"),
  url(r'^view_neigh$',views.view_neigh, name ="view_neigh"),
  # urls for bussinesses
  url(r'^bussinesses$',views.bussinesses, name ="bussinesses"),
  url(r'^view_buss$',views.view_buss, name ="view_buss"),
  #urls for users
  url(r'^user$',views.view_user, name =" view_user "),
  url(r'^update_user$',views.update_user, name ="update_user"),
  
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)