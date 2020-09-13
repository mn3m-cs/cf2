from django.urls import path
from cof import views
from django.views.generic import TemplateView

app_name = 'cof'


urlpatterns = [
    path('machines_api/',views.MachineList.as_view(),name='machine_list'),
    path('pods_api/',views.PodList.as_view(), name='pod_list'),
    
    ######
    path('machines/',TemplateView.as_view(template_name='cof/machines.html')),
    path('pods/',TemplateView.as_view(template_name='cof/pods.html')),

]