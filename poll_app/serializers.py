from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError


class CustomUserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=CustomUser
        fields=['username','password','email']
        read_only_fields=['id']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
class ChoiceSerializer(serializers.ModelSerializer):

    poll_object=serializers.StringRelatedField(read_only=True)
    total_vote=serializers.SerializerMethodField()
    voters=serializers.SerializerMethodField()
    
    class Meta:
        model=Choice
        fields='__all__'

    def get_total_vote(self,obj):
        votes_qs=Vote.objects.filter(choice_object=obj)
        return votes_qs.count()
    def get_voters(self,obj):
        votes_qs=Vote.objects.filter(choice_object=obj)
        return votes_qs.values_list('owner_object__username',flat=True)




class PollSerializer(serializers.ModelSerializer):

    owner=serializers.StringRelatedField(read_only=True)
    choices=serializers.SerializerMethodField()
    total_vote=serializers.SerializerMethodField()

    
    class Meta:
        model=Poll
        fields='__all__'

    def get_choices(self,obj):
        choiceqS=Choice.objects.filter(poll_object=obj)
        serializer_instance=ChoiceSerializer(choiceqS,many=True)
        return serializer_instance.data

    def get_total_vote(self,obj):
        votes_qs=Vote.objects.filter(poll_object=obj)
        return votes_qs.count()



class VoteSeializer(serializers.ModelSerializer):

    class Meta:
        model=Vote
        fields="__all__"
        read_only_fields=['id','poll_object','owner_object']
