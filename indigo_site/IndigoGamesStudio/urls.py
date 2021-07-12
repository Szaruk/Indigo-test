from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('', views.games_post_list, name="games_post_list"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.games_post_detail,
         name='games_post_detail'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)