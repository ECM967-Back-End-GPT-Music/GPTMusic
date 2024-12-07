from rest_framework import serializers

class ChatGPTRequestSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=500)