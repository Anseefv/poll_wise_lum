from django.urls import path
from .views import *
from rest_framework.authtoken.views import ObtainAuthToken 

urlpatterns = [

    path('register/',Register.as_view()),
    path('login/',ObtainAuthToken.as_view()),
    path('poll/',PollViewSet.as_view()),
    path('poll/<int:pk>/',PollRetriveView.as_view()),
    path('poll/<int:pk>/add/',ChoiseApiView.as_view()),
    path('poll/<int:pk>/addvote/',VoteCreateView.as_view()),
    path('list/',PollListView.as_view()),
    
]