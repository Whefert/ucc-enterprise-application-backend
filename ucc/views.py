from .models import Address
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AddressSerializer

@api_view(['GET'])
def all_addresses(request):
    # query the database for all addresses
    addresses = Address.objects.all()
    serializer = AddressSerializer(addresses, many=True)
    return Response(serializer.data)

