from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('HIDDEN_admin/', admin.site.urls),
    path('', include('quizapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)