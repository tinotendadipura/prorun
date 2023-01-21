from django.db import models
from django.utils.timezone import datetime
import random
from django.contrib.auth.models import User

class ContactForm(models.Model):
    
    fullName     = models.CharField(max_length = 500)
    phone_number = models.IntegerField(default=0)
    email        = models.EmailField(default= "")
    city         = models.CharField(max_length = 500,default= "")
    product      = models.CharField(max_length = 500,default= "")
    quantity     = models.CharField(max_length = 500,default= "")
    your_message = models.CharField(max_length = 500 ,default= "")
    contact_created_time =   models.DateTimeField(default = datetime.now)
    
    def __str__(self):
        return self.fullName



class Gallery(models.Model):
    
    display_image          = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    

class Product(models.Model):
    
    product_tittle         = models.CharField(max_length = 500,default = "list - tittle")
    display_image          = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    product_price          = models.CharField(max_length = 500,default = "0")
    def __str__(self):
        return self.product_tittle
     
    



class Resources(models.Model):
    list_tittle                   = models.CharField(max_length = 500,default = "list - tittle")
    home_main_title               = models.CharField(max_length = 500,default = "home -main - tittle")
    main_tittle                   = models.CharField(max_length = 500)
    first_part_description        = models.TextField(max_length = 5000)
    second_part_description       = models.TextField(max_length = 5000)
    main_image                    = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    
    second_section_tittle          = models.CharField(max_length = 500)
    second_part_description1       = models.TextField(max_length = 5000)
    second_part_description2       = models.TextField(max_length = 5000)
    second_part_image              = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)

    third_section_tittle          = models.CharField(max_length = 500)
    third_part_description        = models.TextField(max_length = 5000)
    third_part_point1             = models.TextField(max_length = 5000)
    third_part_point2             = models.TextField(max_length = 5000)
    third_part_point3             = models.TextField(max_length = 5000)
    third_part_point4             = models.TextField(max_length = 5000)
    third_part_image              = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)

    Frequently_Asked_Questions          = models.CharField(max_length = 500,default = "Question")
    question_tittle_1                    = models.CharField(max_length = 5000,default = "tittle")
    question_description_1               = models.TextField(max_length = 5000,default = "description")
    question_tittle_2                    = models.CharField(max_length = 5000,default = "tittle")
    question_description_2               = models.TextField(max_length = 5000,default = "description")
    question_tittle_3                    = models.CharField(max_length = 5000,default = "tittle")
    question_description_3               = models.TextField(max_length = 5000,default = "description")
    question_tittle_4                    = models.CharField(max_length = 5000,default = "tittle")
    question_description_4               = models.TextField(max_length = 5000,default = "description")
    question_tittle_5                    = models.CharField(max_length = 5000,default = "tittle")
    question_description_5               = models.TextField(max_length = 5000,default = "description")

    
    def __str__(self):
        return self.list_tittle





class BranchLocator(models.Model):
    branchName                  = models.CharField(max_length = 500,default = "list - tittle")
    branch_adress               = models.CharField(max_length = 500,default = "home -main - tittle")
    phone_number                = models.CharField(max_length = 500,default = "-------")
    city                        = models.CharField(max_length = 500,default = "-------")
    longitude                   = models.CharField(max_length = 500)
    latitude                    = models.CharField(max_length = 500)
    main_image_1                  = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    main_image_2                  = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    main_image_3                  = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    main_image_4                  = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    main_image_5                  = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    main_image_6                  = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)
    main_image_7                  = models.FileField(upload_to='files/%Y/%m/%d/',null=True,blank=True)

    def __str__(self):
        return self.branchName

