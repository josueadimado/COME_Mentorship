from django.shortcuts import render
from manager.activity import *
import json
from .models import *
from django.views.decorators.csrf import csrf_exempt
from courses.models import *

# Create your views here.
# Utility functions
def file_check(name,allowed=['jpg','jpeg','png','svg','webp']):
    #TODO: validate other files
    images = allowed
    # videos = ['mp4','webm']
    files = ['pdf','docx']
    name_list = name.split(".")
    if name_list[-1] in images:
        return "image"
    # elif name_list[-1] in videos:
    #     return "video"
    elif name_list[-1] in files:
        return "file"
    else:
        return "not allowed"

# def auto_create_hq_admin(request):
#     data = json.loads(str(request.body, encoding='utf-8'))
#     response = {}
#     # this will enable you to hydrate the incoming data => data
#     for key,val in data.items():
#         objects[key]=val
#     activity = Activity("HQSuperAdmin")
#     try:
#         execution = activity.create(**objects)
#     except Exception as e:
#         response = {'success':False,'message':str(e)}
#     else:
#         response = execution
#     dump = json.dumps(response,cls=ExtendedEncoderAllFields)
#     return HttpResponse(dump, content_type='application/json')
@csrf_exempt
def getCategories(request):
    data = json.loads(str(request.body, encoding='utf-8'))
    response = {}
    # this will enable you to hydrate the incoming data => data
    for key,val in data.items():
        objects[key]=val
    cats = [model_to_dict(o) for o in Category.objects.all()]
    response['success']=True
    response['objects'] = cats
    dump = json.dumps(response,cls=ExtendedEncoderAllFields)
    return HttpResponse(dump, content_type='application/json') 


@csrf_exempt
def getCourses(request):
    data = json.loads(str(request.body, encoding='utf-8'))
    response = {}
    # this will enable you to hydrate the incoming data => data
    for key,val in data.items():
        objects[key]=val
    try:
        cat = Category.objects.get(id=int(objects['id']))
    except:
        response['success']=False
        response['message']="Could not get the category with id provided"
        dump = json.dumps(response,cls=ExtendedEncoderAllFields)
        return HttpResponse(dump, content_type='application/json') 
    courses = [model_to_dict(o) for o in cat.courses.all()]
    response['success']=True
    response['objects'] = courses
    dump = json.dumps(response,cls=ExtendedEncoderAllFields)
    return HttpResponse(dump, content_type='application/json') 


@csrf_exempt
def getCourseModules(request):
    data = json.loads(str(request.body, encoding='utf-8'))
    response = {}
    # this will enable you to hydrate the incoming data => data
    for key,val in data.items():
        objects[key]=val
    try:
        course = Course.objects.get(id=int(objects['id']))
    except:
        response['success']=False
        response['message']="Could not get the course with id provided"
        dump = json.dumps(response,cls=ExtendedEncoderAllFields)
        return HttpResponse(dump, content_type='application/json') 
    modules = [model_to_dict(o) for o in course.modules.all()]
    response['success']=True
    response['objects'] = modules
    dump = json.dumps(response,cls=ExtendedEncoderAllFields)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def getCourseAssigments(request):
    data = json.loads(str(request.body, encoding='utf-8'))
    response = {}
    # this will enable you to hydrate the incoming data => data
    for key,val in data.items():
        objects[key]=val
    try:
        course = Course.objects.get(id=int(objects['id']))
    except:
        response['success']=False
        response['message']="Could not get the course with id provided"
        dump = json.dumps(response,cls=ExtendedEncoderAllFields)
        return HttpResponse(dump, content_type='application/json') 
    modules = [model_to_dict(o) for o in course.assignments.all()]
    response['success']=True
    response['objects'] = modules
    dump = json.dumps(response,cls=ExtendedEncoderAllFields)
    return HttpResponse(dump, content_type='application/json') 


@csrf_exempt
def getUserSubscriptions(request):
    data = json.loads(str(request.body, encoding='utf-8'))
    response = {}
    # this will enable you to hydrate the incoming data => data
    for key,val in data.items():
        objects[key]=val
    try:
        user = CustomUser.objects.get(id=int(objects['id']))
    except:
        response['success']=False
        response['message']="Could not get the user, please make sure you are logged in"
        dump = json.dumps(response,cls=ExtendedEncoderAllFields)
        return HttpResponse(dump, content_type='application/json') 
    try:
        subs = Subscription.objects.get(user=user)
    except:
        response['success']=False
        response['message']="Could not get any suibscription for this user"
        dump = json.dumps(response,cls=ExtendedEncoderAllFields)
        return HttpResponse(dump, content_type='application/json') 
    modules = [model_to_dict(o) for o in subs.subscription_courses.all()]
    response['success']=True
    response['objects'] = modules
    dump = json.dumps(response,cls=ExtendedEncoderAllFields)
    return HttpResponse(dump, content_type='application/json') 