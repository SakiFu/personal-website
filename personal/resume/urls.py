from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
import views
from resume.views import ResumeView


urlpatterns = [
               url(r'^$', views.ResumeView.as_view(), name='index'),
               url(r'^admin/', include(admin.site.urls)),
               # url(r'^$/', include('resume.urls')),
               url(r'^resume/', views.ResumeView.as_view(), name='resume'),
               ]