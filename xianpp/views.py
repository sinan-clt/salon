from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http.response import JsonResponse
from xianpp.serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from . models import *




# Create your views here.
def sample(request):
    if request.method=='POST':
        n1=request.POST['fk_int_salon_id']
        n2=request.POST['fk_int_branch_id']
        n3=request.POST['fk_int_category_id']
        n4=request.POST['vchr_services_name']
        n5=request.POST['vchr_services_price']
        n6=request.POST['vchr_services_off_days']
        n7=request.POST['vchr_services_spec_time']
        n8=request.POST['vchr_services_duration']
        n9=request.POST['vchr_services_speciality']
        n10=request.POST['vchr_services_image']
        n11=request.POST['text_services_desc']
        n12=request.POST['text_services_special_instructions']
        n13=request.POST['int_services_view_count']
        n14=request.POST['int_services_status']
        n15=request.POST['vchr_delete_status']
        n16=request.POST['vchr_last_modified_by']
        n17=request.POST['vchr_last_modified_time']

        obj=tbl_services(fk_int_salon_id=n1,fk_int_branch_id=n2,fk_int_category_id=n3,vchr_services_name=n4,
        vchr_services_price=n5,vchr_services_off_days=n6,vchr_services_spec_time=n7,vchr_services_duration=n8,
        vchr_services_speciality=n9,vchr_services_image=n10,text_services_desc=n11,text_services_special_instructions=n12,
        int_services_view_count=n13,int_services_status=n14,vchr_delete_status=n15,vchr_last_modified_by=n16,vchr_last_modified_time=n17)
        obj.save()

        return render(request,'sample.html')
    return render(request,'sample.html')

@csrf_exempt
def categories(request,id=0):
    if request.method=='GET':
        datass=tbl_category.objects.all()
        serializer_data=salonapi(datass, many='True')
        return JsonResponse(serializer_data.data, safe=False)

    elif request.method=='POST':
        datas=JSONParser().parse(request)
        serlzrdata=salonapi(data=datas)
        if serlzrdata.is_valid():
            serlzrdata.save()
            return JsonResponse('Category added Succesfully :)', safe=False)
        return JsonResponse('Failed to add Category', safe=False)

    elif request.method=='DELETE':
        del_data=tbl_category.objects.get(id=id)
        del_data.delete()
        return JsonResponse('Category Deleted :(', safe=False)

    elif request.method=='PUT':
        catdata=JSONParser().parse(request)
        user=tbl_category.objects.get(id=catdata['id'])
        serializerdata=salonapi(user,catdata)
        if serializerdata.is_valid():
            serializerdata.save()
            return JsonResponse('Category updated Succesfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)


def services(request,id=0):
    if request.method=='GET':
        servicess=tbl_services.objects.all()
        serializer_data=serviceapi(servicess, many='True')
        return JsonResponse(serializer_data.data, safe=False)

    elif request.method=='POST':
        datas=JSONParser().parse(request)
        serlzrdata=serviceapi(data=datas)
        if serlzrdata.is_valid():
            serlzrdata.save()
            return JsonResponse('Services added Succesfully :)', safe=False)
        return JsonResponse('Failed to add Services', safe=False)

    elif request.method=='DELETE':
        del_data=tbl_services.objects.get(id=id)
        del_data.delete()
        return JsonResponse('Services Deleted :(', safe=False)

    elif request.method=='PUT':
        service_data=JSONParser().parse(request)
        user=tbl_services.objects.get(id=service_data['id'])
        serializerdata=serviceapi(user,service_data)
        if serializerdata.is_valid():
            serializerdata.save()
            return JsonResponse('Services updated Succesfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)
        


