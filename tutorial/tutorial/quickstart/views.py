from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from tutorial.quickstart.models import User
from tutorial.quickstart.serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET'])
def userList(request):
    """Create Users and return list Users"""
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data,  safe=False)

@csrf_exempt
@api_view(['POST'])
def userCreate(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def userDetail(request, pk,):
    """Retrieve, update or delete"""
    try:
        users = User.objects.get(id=pk)
    except User.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(users)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        users.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)



