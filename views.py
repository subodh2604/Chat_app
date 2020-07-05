from django.contrib import messages
from django.core import serializers
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import Context
from django.template.loader import get_template
from django.urls import reverse
from django.utils.html import escape
from io import StringIO, BytesIO

# Create your views here.


def Home(request):
    return render(request,"chat/home.html")

def chatting(request,room_name,person_name):
    return render(request,"chat/chat_page.html",{'room_name':room_name,'person_name':person_name})


