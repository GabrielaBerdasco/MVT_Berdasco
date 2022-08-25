from django.urls import path
from app_members.views import index, save_members

urlpatterns = [
    path('greetings/', index, name='index'),
    path('members-list/', save_members)
]