from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from MyApps.cursos.models import Asignatura

# Horario de Disponibilidad
class HorarioDisponibilidad(models.Model):
    DIA_OPCIONES = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo')
    ]
    dia = models.CharField(max_length=10, choices=DIA_OPCIONES, help_text="Día de la semana")
    hora_inicio = models.TimeField(help_text="Hora de inicio")
    hora_fin = models.TimeField(help_text="Hora de fin")

    def __str__(self):
        return f"{self.dia}: {self.hora_inicio} - {self.hora_fin}"

# Estudiante
class Estudiante(models.Model):
    nombre = models.CharField(max_length=15, help_text="Nombre del estudiante")
    apellido = models.CharField(max_length=15, help_text="Apellido del estudiante")
    TIPO_IDENTIFICACION_OPCIONES = [
        ['CÉDULA DE CIUDADANÍA', 'Cédula de Ciudadanía'],
        ['TARJETA DE IDENTIDAD', 'Tarjeta de Identidad']
    ]
    tipo_id = models.CharField(max_length=30, choices=TIPO_IDENTIFICACION_OPCIONES, help_text="Tipo de identificación")
    numero_id = models.IntegerField(unique=True, help_text="Número de identificación")
    CARRERAS_OPCIONES = [
        ['INGENIERÍA DE SISTEMAS', 'Ingeniería de Sistemas'],
    ]
    carrera = models.CharField(max_length=30, choices=CARRERAS_OPCIONES, help_text="Carrera del estudiante")
    semestre = models.IntegerField(help_text="Semestre actual", validators=[MinValueValidator(1), MaxValueValidator(10)])
    correo = models.EmailField(unique=True, help_text="Correo del estudiante")
    contraseña = models.CharField(max_length=15, help_text="Contraseña del estudiante")

    def __str__(self):
        return f'{self.nombre} {self.apellido} -> {self.correo}'
    
    class Meta:
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"

# Docente
class Docente(models.Model):
    nombre = models.CharField(max_length=15, help_text="Nombre del docente")
    apellido = models.CharField(max_length=15, help_text="Apellido del docente")
    numero_id = models.IntegerField(unique=True, help_text="Número de identificación del docente")
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, help_text="Asignaturas que dicta")
    correo = models.EmailField(unique=True, help_text="Correo del docente")
    contraseña = models.CharField(max_length=15, help_text="Contraseña del docente")

    def __str__(self):
        return f'{self.nombre} {self.apellido} -> {self.correo}'
    
    class Meta:
        verbose_name = "docente"
        verbose_name_plural = "docentes"

# Tutor (heredando de Estudiante)
class Tutor(Estudiante):
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, help_text="Asignatura que dictará")
    horario_disponibilidad = models.ManyToManyField(HorarioDisponibilidad, help_text="Horarios de disponibilidad")

    class Meta:
        verbose_name = "tutor"
        verbose_name_plural = "tutores"