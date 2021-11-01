from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import BigIntegerField
from rest_framework.fields import CharField

# Create your models here.
class tbl_category(models.Model):
    vchr_category_name=models.CharField(max_length=250)
    vchr_category_image=models.CharField(max_length=250)
    vchr_delete_status=models.CharField(max_length=5)
    vchr_last_modified_by=models.CharField(max_length=75)
    vchr_last_modified_time=models.CharField(max_length=110)

class tbl_user(models.Model):
    vchr_name=models.CharField(max_length=250)
    vchr_password=models.CharField(max_length=250)
    vchr_email=models.CharField(max_length=250)
    vchr_phone=models.CharField(max_length=250)
    vchr_location=models.CharField(max_length=250)
    enum_user_type=models.CharField(max_length=250)
    vchr_delete_status=models.CharField(max_length=5)
    vchr_last_modified_by=models.CharField(max_length=75)
    vchr_last_modified_time=models.CharField(max_length=110)


class tbl_salon(models.Model):
    fk_int_user_id=models.ForeignKey(tbl_user,on_delete=DO_NOTHING)
    vchr_salon_name=models.CharField(max_length=250)
    vchr_salon_place=models.CharField(max_length=250)
    vchr_salon_pincode=models.CharField(max_length=250)
    vchr_salon_latitude=models.CharField(max_length=250)
    vchr_salon_longitude=models.CharField(max_length=250)
    vchr_salon_image=models.CharField(max_length=250)
    text_salon_address=models.TextField()
    int_salon_view_count=BigIntegerField()
    int_is_salon_paid=BigIntegerField()
    vchr_delete_status=models.CharField(max_length=5)
    vchr_last_modified_by=models.CharField(max_length=75)
    vchr_last_modified_time=models.CharField(max_length=110)


class tbl_client(models.Model):
    fk_int_user_id=models.ForeignKey(tbl_user,on_delete=DO_NOTHING)
    vchr_client_phone_alt=models.CharField(max_length=250)
    vchr_client_email_alt=models.CharField(max_length=250)
    vchr_client_image=models.CharField(max_length=250)
    vchr_client_address=models.TextField()
    enum_client_gender=models.CharField(max_length=250)
    vchr_delete_status=models.CharField(max_length=5)
    vchr_last_modified_by=models.CharField(max_length=110)
    vchr_last_modified_time=models.CharField(max_length=75)


class tbl_branch(models.Model):
    fk_int_user_id=models.ForeignKey(tbl_user,on_delete=DO_NOTHING)
    fk_int_salon_id=models.ForeignKey(tbl_salon,on_delete=DO_NOTHING)
    vchr_branch_name=models.CharField(max_length=250)
    vchr_branch_place=models.CharField(max_length=250)
    vchr_branch_pincode=models.CharField(max_length=250)
    vchr_branch_latitude=models.CharField(max_length=250)
    vchr_branch_longitude=models.CharField(max_length=250)
    vchr_branch_image=models.CharField(max_length=250)
    text_branch_address=models.TextField()
    int_is_branch_paid=BigIntegerField()
    vchr_delete_status=models.CharField(max_length=5)
    vchr_last_modified_by=models.CharField(max_length=75)
    vchr_last_modified_time=models.CharField(max_length=110)


class tbl_services(models.Model):
    fk_int_salon_id=models.ForeignKey(tbl_salon,on_delete=DO_NOTHING)
    fk_int_branch_id=models.ForeignKey(tbl_branch,on_delete=DO_NOTHING)
    fk_int_category_id=models.ForeignKey(tbl_category,on_delete=DO_NOTHING)
    vchr_services_name=models.CharField(max_length=250)
    vchr_services_price=models.CharField(max_length=250)
    vchr_services_off_days=models.CharField(max_length=250)
    vchr_services_spec_time=models.CharField(max_length=250)
    vchr_services_duration=models.CharField(max_length=250)
    vchr_services_speciality=models.CharField(max_length=250)
    vchr_services_image=models.CharField(max_length=250)
    text_services_desc=models.TextField()
    text_services_special_instructions=models.TextField()
    int_services_view_count=models.BigIntegerField()
    int_services_status=models.BigIntegerField()
    vchr_delete_status=models.CharField(max_length=5)
    vchr_last_modified_by=models.CharField(max_length=75)
    vchr_last_modified_time=models.CharField(max_length=110)


