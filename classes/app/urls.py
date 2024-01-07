from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = i18n_patterns(

    # Admin
    path('admin/', admin.site.urls),

    prefix_default_language=False

)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler404 = 'data.views.handle_page_notfound'
# handler500 = 'data.views.handle_server_error'