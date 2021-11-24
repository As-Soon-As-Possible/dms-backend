from django.shortcuts import render
from .serializers import UserSerializer, VictimSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser,AllowAny
from django.contrib.auth.models import User
from .models import Victim,Volunteer
from rest_framework.generics import GenericAPIView
from .models import Victim, Volunteer, Assigned
from geopy.distance import geodesic

class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    permission_classes = [IsAdminUser]
    http_method_names = ['get', 'head']

    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class RecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    http_method_names = ['get', 'head','post']

    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )





class VictimSMSAPI(GenericAPIView):
    def post(self, request, *args, **kwargs):

        serializer = VictimSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, format=None):
        vics = Victim.objects.all()
        serializer = VictimSerializer(vics, many=True)
        return Response(serializer.data)



class GetRescueMapAPI(GenericAPIView):
    def get(self, request, *args, **kwargs):
        try:
            vics = Victim.objects.all()
            serializer = VictimSerializer(vics, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'ERROR': type(e).__name__.upper(), "MESSAGE": str(e)}, status=status.HTTP_404_NOT_FOUND)

class FindVictim(APIView):
    http_method_names = ['get', 'head', 'post']
    def post(self, request):
        mobile_no = request.data['mobile_no'] 
        location = request.data['location']
        latitude = request.data['latitude']
        longitude = request.data['longitude']
        assigned_victims_queryset = Assigned.objects.all()
        assigned_victims = []
        for i in range(len(assigned_victims_queryset)):
            assigned_victims.append(assigned_victims_queryset[i].assigned_victim.mobile_no)
        print(assigned_victims)
        print(Victim.objects.all())
        victims_to_be_rescued = Victim.objects.exclude(mobile_no__in = assigned_victims).filter(location=location)
        print(victims_to_be_rescued)
        dist = float('inf')
        for victim in victims_to_be_rescued:
            victim_latitude = victim.latitude
            victim_longitude = victim.longitude
            curr_dist = geodesic((latitude, longitude),(victim_latitude, victim_longitude)).kilometers
            if(curr_dist < dist):
                dist = curr_dist
                victim_mobile_no = victim.mobile_no
            pass

        nearest_victim = Victim.objects.filter(mobile_no = victim_mobile_no).first()
        print(nearest_victim)
        volunteer =  Volunteer.objects.filter(mobile_no=mobile_no).first()
        print(volunteer)
        new = Assigned(assigned_volunteer = volunteer, assigned_victim = nearest_victim)
        new.save()
        return Response(request.data)

