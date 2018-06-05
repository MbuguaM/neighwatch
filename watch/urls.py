from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
  #landin page 
  url(r'^$',views.home, name ="home"),
  # urls for neighbourhoods
  url(r'^neigborhoods$',views.neighborhoods, name ="neighborhoods"),
  url(r'^view_neigh$',views.view_neigh, name ="view_neigh"),
  # urls for bussinesses
  url(r'^bussinesses$',views.bussinesses, name ="bussinesses"),
  url(r'^view_buss$',views.view_buss, name ="view_buss"),
  
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)