from django.contrib import admin

from .models import Squad, Employee, Investment, DayName, SquadInvestment

admin.site.register(Squad)
admin.site.register(Employee)
admin.site.register(Investment)
admin.site.register(SquadInvestment)
admin.site.register(DayName)


