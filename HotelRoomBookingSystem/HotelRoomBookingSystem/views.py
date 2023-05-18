from django.http import HttpResponse
from django.shortcuts import render




def home(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")



def service(request):
    return render(request,"service.html")


def Room(request):
    return render(request,"Room.html")



def Booking(request):
    return render(request,"Booking.html")




def ourteam(request):
    return render(request,"OurTeam.html")



def Testtimonial(request):
    return render(request,"Testimonial.html")


def Contact(request):
    return render(request,"Contact.html")
