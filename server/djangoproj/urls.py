
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # Django Application
    path('djangoapp/', include('djangoapp.urls')),

    # Home Page
    path(
        '',
        TemplateView.as_view(template_name="Home.html"),
        name='home'
    ),

    # About Us Page
    path(
        'about/',
        TemplateView.as_view(template_name="About.html"),
        name='about'
    ),

    # Contact Us Page
    path(
        'contact/',
        TemplateView.as_view(template_name="Contact.html"),
        name='contact'
    ),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
