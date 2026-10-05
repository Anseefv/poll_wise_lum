from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView,mixins,ListCreateAPIView,RetrieveAPIView,DestroyAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import ValidationError

from .models import*
from .serializers import*


class Register(CreateAPIView):

    serializer_class=CustomUserSerializer


class PollViewSet(ListCreateAPIView):

    serializer_class=PollSerializer
    queryset=Poll.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class PollListView(ListAPIView):

    serializer_class=PollSerializer
    queryset=Poll.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]



class PollRetriveView(RetrieveAPIView,DestroyAPIView):
    serializer_class=PollSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Poll.objects.all()




class ChoiseApiView(CreateAPIView):
    serializer_class=ChoiceSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]


    def perform_create(self, serializer):

        poll_id=self.kwargs.get('pk')
        poll_obj=Poll.objects.get(id=poll_id)
        return serializer.save(poll_object=poll_obj)






class VoteCreateView(CreateAPIView):

    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=VoteSeializer


    def perform_create(self, serializer):

        pid=self.kwargs.get('pk')
        poll_object=Poll.objects.get(id=pid)
        valid_choice_objects=Choice.objects.filter(poll_object=poll_object)
        choice_object=serializer.validated_data.get('choice_object')
        # choice_object=Choice.objects.get(id=choice_id)
        if choice_object not in valid_choice_objects:
            raise serializers.ValidationError("invaliod choice")

        return  serializer.save(poll_object=poll_object,owner_object=self.request.user)



