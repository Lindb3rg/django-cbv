from django.contrib import admin

from cbvapp import models


admin.site.register(models.School)
admin.site.register(models.Student)
admin.site.register(models.Car)


