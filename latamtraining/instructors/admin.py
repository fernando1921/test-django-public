from django.contrib import admin
from .models import Instructor, Language, Course

admin.site.register(Instructor)
admin.site.register(Language)


#### Task 1.1: (Not required but nice to have) Add Course Model on Django Admin
admin.site.register(Course)

### Task 1.1 - End
