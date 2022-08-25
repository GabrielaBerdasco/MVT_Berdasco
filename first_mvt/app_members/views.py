from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from app_members.models import Family_Members

def index(request) :
    return HttpResponse("Hello, world. You're at the family member index.")

def save_members(request) :

    members = Family_Members.objects.all()
    fam_dict = { 'lista': members }
    temp_1 = loader.get_template("members_template.html")
    doc_html = temp_1.render(fam_dict)

    return HttpResponse(doc_html)
    
