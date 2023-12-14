from django.contrib import admin

from services.models import Service, Subscription, Plan


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    pass


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass
