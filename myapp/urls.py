from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="homepage"),
    path('signup', views.sign_up, name="signup"),
    path('login', views.log_in, name="login"),
    path('add', views.addpost, name="addpost"),
    path('logout', views.log_out, name="logout"),
    path('message', views.message_view, name="message")
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

