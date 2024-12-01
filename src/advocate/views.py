from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def advocate(request):
    data = ["harsh", "Dennis"]
    return Response(data)

@api_view(["GET"])
def advocate_detail(request,username):
    data = {"username" : username}
    return Response(data)