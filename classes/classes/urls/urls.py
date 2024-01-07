from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from django.urls import re_path
from django.conf.urls.i18n import i18n_patterns

from django.urls import path, register_converter
from django.urls.converters import StringConverter

from classes import public

class IStringConverter(StringConverter):
    def to_python(self, value):
        return value.lower()

# once done, register it as:
register_converter(IStringConverter, 'istr')

urlpatterns = i18n_patterns(

    # Static Pages
    path('', public.home, name='home'),

    # localization
    path('i18n/', include('django.conf.urls.i18n')),

    prefix_default_language=False

)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler404 = 'classes.views.handle_page_notfound'
# handler500 = 'classes.views.handle_server_error'
