"""djangoresume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from resume import views #import my views
from django.urls import path



from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^resume/$', views.index, name='index'),
]
urlpatterns += [ #Add Django site authentication urls (for login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls')),
    path(r'cv/', include('resume.urls'))
]


if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += [
#] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#urlpatterns += [
#] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
### TODO <int:pk> can be a slug - https://chriskief.com/2012/12/29/django-generic-detailview-without-a-pk-or-slug/
urlpatterns += [
    path('overview/create/', views.OverviewCreate.as_view(), name='overview_create'),
    path('overview/<int:pk>/update/', views.OverviewUpdate.as_view(), name='overview_update'),
    path('overview/<int:pk>/delete/', views.OverviewDelete.as_view(), name='overview_delete'),
    path('personalinfo/create/', views.PersonalInfoCreate.as_view(), name='personalinfo_create'),
    path('personalinfo/<int:pk>/update/', views.PersonalInfoUpdate.as_view(), name='personalinfo_update'),
    path('personalinfo/<int:pk>/delete/', views.PersonalInfoDelete.as_view(), name='personalinfo_delete'),
    path('education/create/', views.EducationCreate.as_view(), name='education_create'),
    path('education/<int:pk>/update/', views.EducationUpdate.as_view(), name='education_update'),
    path('education/<int:pk>/delete/', views.EducationDelete.as_view(), name='education_delete'),
]
'''
