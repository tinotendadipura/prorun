from django.contrib import admin
from .models import  ContactForm ,Gallery ,Resources ,BranchLocator,Product
from django.contrib.auth.models import Group


class ContactFormAdmin(admin.ModelAdmin):
    list_display = (

    'fullName',  
    'phone_number', 
    'email',        
    'city',      
    'product',    
    'quantity',    
    'your_message',
    'contact_created_time'

    )
    
    list_per_page = 10
    search_fields = ('fullName', 'phone_number', 'email','city', 'product','quantity', 'your_message',
    'contact_created_time',) 
    list_filter = (
        'fullName', 'phone_number', 'email', 'city', 'product', 'quantity', 'your_message','contact_created_time',
    )

admin.site.register( ContactForm , ContactFormAdmin)



class ResourcesAdmin(admin.ModelAdmin):
    list_display = (
    'list_tittle',
    'home_main_title',
    'main_tittle',      
    'first_part_description',       
    'second_part_description',   
    'main_image'         

    )
    
    list_per_page = 10
    search_fields = (
    'list_tittle',
    'main_tittle',      
    'first_part_description',       
    'second_part_description',   
    'main_image' ) 
    
admin.site.register( Resources , ResourcesAdmin)



class BranchLocatorAdmin(admin.ModelAdmin):
    list_display = (
    'branchName' ,'branch_adress' ,'city' ,'longitude',                  
    'latitude' ,'main_image_1','main_image_2', 'main_image_3'
    , 'main_image_4' ,'main_image_5','main_image_6','main_image_7'                

    )
    
    list_per_page = 10
    search_fields = (
    'branchName' ,'branch_adress' ,'city' ,'longitude',                  
    'latitude' ,'main_image_1','main_image_2', 'main_image_3'
    ,'main_image_4' ,'main_image_5','main_image_6','main_image_7'                
 ) 
    
admin.site.register(BranchLocator , BranchLocatorAdmin)


class GalleryAdmin(admin.ModelAdmin):
    list_display = (
    'display_image',         
         
    

    )
    
    

admin.site.register(Gallery , GalleryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
    'product_tittle',        
    'display_image',        
    'product_price',             
 
    )
    
admin.site.register(Product , ProductAdmin)



