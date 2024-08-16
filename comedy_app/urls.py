from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('open-mics/', views.OpenMicList.as_view(), name='open_mic_list'),
    path('open-mics/<int:pk>', views.OpenMicDetail.as_view(), name='open_mic_detail'),
   ]