from django.urls import include, path
from django.conf import settings

urlpatterns = [
    path('', include('core.urls', namespace='app')),
]

