from django.urls import path
from MyApps.discusiones.views import ForoList, ForoDetail, MensajeList, MensajeDetail

app_name = "discusiones"
urlpatterns = [
    path('foro/', ForoList.as_view()),
    path('foro/<int:pk>', ForoDetail.as_view()),
    path('mensaje/', MensajeList.as_view()),
    path('mensaje/<int:pk>', MensajeDetail.as_view()),
]