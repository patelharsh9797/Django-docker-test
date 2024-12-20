from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer

# GET /advocates
# POST /advocates

# GET /advocates/:id
# PUT /advocates/:id
# DELETE /advocates/:id


@api_view(["GET", "POST"])
def advocate(request):
    if request.method == "GET":
        query = request.GET.get("query")

        if query is None:
            query = ""

        advocates = Advocate.objects.filter(
            Q(username__icontains=query) | Q(bio__icontains=query)
        )
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        advocates = Advocate.objects.create(
            username=request.data["username"],
            bio=request.data["bio"],
        )
        serializer = AdvocateSerializer(advocates, many=False)
        return Response(serializer.data)


# @api_view(["GET", "PUT", "DELETE"])
# def advocate_detail(request,username):
#     advocate = Advocate.objects.get(username=username)

#     if request.method == "GET":
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)

#     if request.method == "PUT":
#         advocate.username = request.data["username"]
#         advocate.bio = request.data["bio"]
#         advocate.save()
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)

#     if request.method == "DELETE":
#         advocate.delete()
#         return Response("Advocate deleted")


class AdvocateDetail(APIView):
    def get_object(self, username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist:
            raise Response("Advocate not found!!!")

    def get(self, request, username):
        advocate = self.get_object(username)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    def put(self, request, username):
        advocate = self.get_object(username)
        advocate.username = request.data["username"]
        advocate.bio = request.data["bio"]
        advocate.save()
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    def delete(self, request, username):
        advocate = self.get_object(username)
        advocate.delete()
        return Response("Advocate deleted")


@api_view(["GET"])
def companies_list(request):
    componies = Company.objects.all()
    serializer = CompanySerializer(componies, many=True)
    return Response(serializer.data)


class CompanyDetail(APIView):
    def get_object(self, company_name):
        try:
            return Company.objects.get(name=company_name)
        except Company.DoesNotExist:
            raise Response("Company not found!!!")

    def get(self, request, company_name):
        company = self.get_object(company_name)
        serializer = CompanySerializer(company, many=False)
        return Response(serializer.data)

    def put(self, request, company_name):
        company = self.get_object(company_name)
        company.username = request.data["username"]
        company.bio = request.data["bio"]
        company.save()
        serializer = CompanySerializer(company, many=False)
        return Response(serializer.data)

    def delete(self, request, company_name):
        company = self.get_object(company_name)
        company.delete()
        return Response("Company deleted")
