from django.shortcuts import render


# Create your views here.
class DoctorViews:
    def __init__(self):
        pass

    def index(request):
        return render(request, 'doctor/index.html')
