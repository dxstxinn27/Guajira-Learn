from django.urls import path
from MyApps.usuarios import views
from MyApps.usuarios.views import DocenteList, DocenteDetail, DocenteLoginView, EstudianteList, EstudianteDetail, EstudianteLoginView, TutorList, TutorDetail, HorarioDisponibilidadList, HorarioDisponibilidadDetail

app_name = "usuarios"

urlpatterns = [
    path('docentes/', DocenteList.as_view()),
    path('docentes/<int:pk>', DocenteDetail.as_view()),
    path('docentes/login', DocenteLoginView.as_view()),
    path('estudiantes/', EstudianteList.as_view()),
    path('estudiantes/<int:pk>', EstudianteDetail.as_view()),
    path('estudiantes/login', EstudianteLoginView.as_view()),
    path('tutores/', TutorList.as_view()),
    path('tutores/<int:pk>', TutorDetail.as_view()),
    path('horarios/', HorarioDisponibilidadList.as_view()),
    path('horarios/<int:pk>', HorarioDisponibilidadDetail.as_view()),
]