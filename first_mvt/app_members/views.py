from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from models import Family_Members

def index(request) :
    return HttpResponse("Hello, world. You're at the polls index.")

def save_members(request) :
    member_1 = Family_Members(name="Pablo",last_name="Ríos",
    email="pablorios@gmail.com",birthday="23/7/81", phone_number=2614567890)
