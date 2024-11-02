from rest_framework import serializers
from .models import Task


class TaskListSerializers(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = '__all__'
