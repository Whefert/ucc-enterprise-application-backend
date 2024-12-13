from .models import Address
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

@api_view(['GET'])
def all_addresses(request):
    # query the database for all addresses
    addresses = Address.objects.all()
    serializer = AddressSerializer(addresses, many=True)
    return Response(serializer.data)

# Get all students
@api_view(['GET'])
def all_students(request):
    # query the database for all students
    students = Student.objects.all()

    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

# Get all users
@api_view(['GET'])
def all_users(request):
    # query the database for all users
    users = User.objects.select_related('title', 'address', 'contact_details', 'next_of_kin1').all()
    serializer = UserSerializer(users, many=True, )
    return Response(serializer.data)