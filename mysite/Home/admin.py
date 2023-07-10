from django.contrib import admin

from .models import Employee
from .models import Monitor
#Register your models here.

admin.site.register(Employee)
admin.site.register(Monitor)
