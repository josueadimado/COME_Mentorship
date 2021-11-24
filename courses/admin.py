from django.contrib import admin
from .models import *


class CourseInline(admin.TabularInline):
    model = Course
    extra = 0

class ModuleInline(admin.TabularInline):
    model = Module
    extra = 0


class AssignmentInline(admin.TabularInline):
    model = Assignment
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleInline,AssignmentInline,]
    model = Course


class CategoryAdmin(admin.ModelAdmin):
    inlines = [CourseInline,]
    model = Category



# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Module)
admin.site.register(Subscription)
admin.site.register(SubscriptionCourse)
admin.site.register(Assignment)