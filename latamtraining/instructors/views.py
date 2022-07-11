from tokenize import String
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404


from .models import Instructor, Language, Course


def index(request):
    return HttpResponse(
        "Hello candidate!<br><br> Check the details for this test on <a href=https://github.com/leocosta-io/test-django-public>https://github.com/leocosta-io/test-django-public</a> or on the file README.md in your project."
    )


def list(request, language=None):
    template = loader.get_template("instructors/list.html")

    instructors = None

    ### Task 3: Get instructors from database and filter them based on the language

    if language:
        ##l=Language.objects.get(code=language)
        l=get_object_or_404(Language, code=language) 
        instructors = Instructor.objects.filter(languages__in=[l])
    else:
        instructors = Instructor.objects.all()

    ### Task 3 - End

    context = {
        "instructors": instructors,
    }
    return HttpResponse(template.render(context, request))
