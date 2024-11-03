from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import Task
from .serializers import *
from datetime import datetime

class TaskListView(APIView):

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskListSerializers(tasks, many=True)

        return Response(serializer.data)

    def post(self, request):
        task = TaskCreateSerializers(data=request.data)
        if task.is_valid():
            task.save(user=request.user)

        return Response(status=201)


class TaskDetailView(APIView):

    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskDetailSerializers(task)

        return Response(serializer.data)

    def delete(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskDeleteSerializers(task)
        task.delete()

        return Response(status=200)

    def patch(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskUpdateSerializers(task, data=request.data)
        if serializer.is_valid():
            serializer.validated_data['update'] = datetime.now()
            serializer.save()

        return Response(status=200)