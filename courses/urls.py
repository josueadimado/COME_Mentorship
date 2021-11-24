from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^get-courses/$',views.getCourses),
    url(r'^get-categories/$',views.getCategories),
    url(r'^get-modules/$',views.getCourseModules),
    url(r'^get-assignments/$',views.getCourseAssigments),
    url(r'^get-subscriptions/$',views.getUserSubscriptions),
]