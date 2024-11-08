from django.urls import path
from MyApps.cursos.views import AsignaturaList, AsignaturaDetail, TemaList, TemaDetail

app_name = "cursos"
urlpatterns = [
    path('asignatura/', AsignaturaList.as_view()),
    path('asignatura/<int:pk>', AsignaturaDetail.as_view()),
    path('tema/', TemaList.as_view()),
    path('tema/<int:pk>', TemaDetail.as_view()),
]