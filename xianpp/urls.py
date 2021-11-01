from django.urls import path,include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('categories/',views.categories,name='categories'),
    path('categories/<int:id>',views.categories,name='categories'),

    path('services/',views.services,name='services'),
    path('services/<int:id>',views.services,name='services'),

    path('sample',views.sample,name='sample'),
 

]