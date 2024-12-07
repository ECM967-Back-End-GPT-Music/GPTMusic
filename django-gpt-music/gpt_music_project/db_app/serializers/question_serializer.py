from rest_framework import serializers
from db_app.models import QuestionAnswer

class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = '__all__'