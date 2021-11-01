from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from xianpp.models import *


class salonapi(serializers.ModelSerializer):
    class Meta:
        model=tbl_category
        fields=('id','vchr_category_name','vchr_category_image','vchr_delete_status','vchr_last_modified_by','vchr_last_modified_time')
    

class serviceapi(serializers.ModelSerializer):
    class Meta:
        model=tbl_services
        fields=('id','fk_int_salon_id','fk_int_branch_id','fk_int_category_id','vchr_services_name','vchr_services_price','vchr_services_off_days','vchr_services_spec_time','vchr_services_duration','vchr_services_speciality','vchr_services_image','text_services_desc','text_services_special_instructions','int_services_view_count','int_services_status','vchr_delete_status','vchr_last_modified_by','vchr_last_modified_time')