"""bandz2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from public.views import HomepageView, CountyListView, BandListView, BandDetailView, BandCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path("",
    #     TemplateView.as_view(template_name="public_index.html"),
    #     name="home",
    # ),
    # path('', include(('home.urls', 'home'), namespace='home'))
    path('', HomepageView.as_view(), name='home'),
    path('counties/', CountyListView.as_view(template_name="county_list.html"), name='counties'),
    path('bands/', BandListView.as_view(template_name="public_list.html"), name='bands'),
    path('bands/add/', view=BandCreateView.as_view(template_name="band_add.html"), name='band_add'),
    path('bands/<slug:slug>/', view=BandDetailView.as_view(template_name="band_detail.html"), name='band_detail')
]
