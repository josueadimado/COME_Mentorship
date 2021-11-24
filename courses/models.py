from django.db import models
from django.conf import settings


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    image = models.FileField(upload_to="categories",null=True,blank=True)


currencies = (
    ("GHC","GHC"),
    ("$","$")
)
class Course(models.Model):
    name = models.CharField(max_length=150,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    price = models.FloatField(default=99)
    currency = models.CharField(max_length=5,null=True,blank=True,choices=currencies)
    free = models.BooleanField(default=True)
    lecturer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True,related_name="courses")
    image = models.FileField(upload_to="courses",null=True,blank=True)

    def __str__(self):
        return self.name


class Module(models.Model):
    title = models.CharField(max_length=150,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    time = models.CharField(max_length=10,null=True,blank=True, help_text="for example 04:54")
    thumbnail = models.FileField(upload_to="courses",null=True,blank=True)
    video = models.FileField(upload_to="resources",null=True,blank=True)
    transcript = models.TextField(null=True,blank=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True,related_name="modules")

    def __str__(self):
        return self.title


class Material(models.Model):
    module = models.ForeignKey(Module,on_delete=models.CASCADE,null=True,blank=True,related_name="materials")
    file = models.FileField(upload_to="materials",null=True,blank=True)


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.user.username



class SubscriptionCourse(models.Model):
    subscription = models.ForeignKey(Subscription,on_delete=models.CASCADE,null=True,blank=True,related_name="subscription_courses")
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)
    paid = models.BooleanField(default=False)
    progress = models.FloatField(default=0.0)



class Assignment(models.Model):
    title = models.CharField(max_length=150,null=True,blank=True)
    instruction = models.TextField(null=True,blank=True)
    file = models.FileField(upload_to="assignments",null=True,blank=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True,related_name="assignments")


grades = (
    ("A","A"),
    ("B","B"),
    ("C","C")
)
class Submission(models.Model):
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE,null=True,blank=True,related_name="submissions")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    marked = models.BooleanField(default=False)
    score = models.FloatField(default=5)
    grade = models.CharField(max_length=3,null=True,blank=True,choices=grades)

