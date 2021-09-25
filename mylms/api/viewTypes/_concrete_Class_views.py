from .models import StudentModel
from .serializers import StudentModelSerializer
from rest_framework import generics


# Concrete Views from rest_frameworks

#Read Only List Class GET
class studentsList_API(generics.ListAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer

#Write Only POST
class studentCreate_API(generics.CreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer

# Read and Write POST GET
class studentListCreate_API(generics.ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer


#Update Retrive Destroy PUT GET DELETE
class studentRetriveUpdateDelete_API(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer