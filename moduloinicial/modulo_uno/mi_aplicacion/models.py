from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    grupo_tutor = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='tutor', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    ESTADO_CIVIL_CHOICES = [
        ('Soltero', 'Soltero'),
        ('Casado', 'Casado'),
        ('Divorciado', 'Divorciado'),
        ('Otro', 'Otro')
    ]

    VIVE_CON_CHOICES = [
        ('Mamá', 'Mamá'),
        ('Papá', 'Papá'),
        ('Ambos', 'Ambos'),
        ('Otros', 'Otros')
    ]

    TIPO_CASA_CHOICES = [
        ('Propia', 'Propia'),
        ('Rentada', 'Rentada'),
        ('Prestada', 'Prestada'),
        ('Otros', 'Otros')
    ]

    TIPO_COMPUTADORA_CHOICES = [
        ('PC', 'PC'),
        ('Laptop', 'Laptop')
    ]

    FORMA_TRABAJAR_CHOICES = [
        ('Solo', 'Solo'),
        ('En equipo', 'En equipo'),
        ('Binas', 'Binas'),
        ('Grupal', 'Grupal')
    ]

    DEPENDENCIA_CHOICES = [
        ('Mamá', 'Mamá'),
        ('Papá', 'Papá'),
        ('Tú', 'Tú'),
        ('Ambos', 'Ambos'),
        ('Otros', 'Otros')
    ]

    nombre = models.CharField(max_length=200, verbose_name='Nombre completo')
    edad = models.IntegerField(verbose_name='Edad')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name='Sexo')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    lugar_nacimiento = models.CharField(max_length=200, verbose_name='Lugar de nacimiento')
    numero_matricula = models.CharField(max_length=100, unique=True, verbose_name='Número de matrícula')
    direccion = models.TextField(verbose_name='Dirección')
    telefono = models.CharField(max_length=15, verbose_name='Teléfono Casa')
    celular = models.CharField(max_length=15, verbose_name='Teléfono Celular')
    telefono_emergencia = models.CharField(max_length=15, verbose_name='Teléfono de emergencia')
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, verbose_name='Carrera')
    cuatrimestre = models.CharField(max_length=100, verbose_name='Cuatrimestre')
    grupo_escolar = models.ForeignKey(Grupo, on_delete=models.CASCADE, verbose_name='Grupo escolar')
    estado_civil = models.CharField(max_length=10, choices=ESTADO_CIVIL_CHOICES, verbose_name='Estado civil')
    estado_civil_otro = models.CharField(max_length=100, blank=True, null=True, verbose_name='Otro (estado civil)')
    nombre_tutor = models.CharField(max_length=200, verbose_name='Nombre del tutor')
    numero_seguro_social = models.CharField(max_length=20, verbose_name='Número de seguro social')
    correo_electronico = models.EmailField(verbose_name='Correo electrónico')
    tipo_sangre = models.CharField(max_length=3, verbose_name='Tipo de sangre')
    tipo_religion = models.CharField(max_length=100, verbose_name='Tipo de religión')

    # Aspectos socioeconómicos del estudiante
    lugar_procedencia = models.CharField(max_length=200, verbose_name='Lugar de procedencia')
    con_quien_vives = models.CharField(max_length=20, choices=VIVE_CON_CHOICES, verbose_name='¿Con quién vives?')
    otros_familiares = models.CharField(max_length=200, blank=True, null=True, verbose_name='Otros familiares')
    trabajas = models.BooleanField(verbose_name='¿Trabajas? si la respuesta es SI marca la casilla en caso contrario omite las siguientes preguntas')
    tipo_empresa = models.CharField(max_length=100, blank=True, null=True, verbose_name='Tipo de empresa')
    horas_trabajo = models.IntegerField(blank=True, null=True, verbose_name='Horas de trabajo')
    ingreso_mensual = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Ingreso mensual')
    horario_laboral = models.CharField(max_length=100, blank=True, null=True, verbose_name='Horario laboral')
    dependes_economicamente = models.CharField(max_length=20, choices=DEPENDENCIA_CHOICES, verbose_name='¿De quién dependes económicamente?')
    otros_dependientes = models.CharField(max_length=200, blank=True, null=True, verbose_name='Otros dependientes')
    ocupacion_padre = models.CharField(max_length=100, verbose_name='Ocupación del padre')
    ingreso_padre = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Ingreso del padre')
    ocupacion_madre = models.CharField(max_length=100, verbose_name='Ocupación de la madre')
    ingreso_madre = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Ingreso de la madre')
    hermanos = models.IntegerField(blank=True, null=True, verbose_name='Número de hermanos')
    lugar_entre_hermanos = models.CharField(max_length=100, blank=True, null=True, verbose_name='Lugar entre hermanos')
    actividad_hermanos = models.TextField(blank=True, null=True, verbose_name='Actividad de los hermanos')
    tipo_casa = models.CharField(max_length=10, choices=TIPO_CASA_CHOICES, verbose_name='Tipo de casa')
    tipo_casa_otros = models.CharField(max_length=100, blank=True, null=True, verbose_name='Otros (tipo de casa)')
    beca_bachillerato = models.BooleanField(verbose_name='¿Tuviste beca en el bachillerato? si la respuesta es SI marca la casilla')
    tipo_beca_bachillerato = models.CharField(max_length=100, blank=True, null=True, verbose_name='Tipo de beca en bachillerato')
    requieres_beca = models.BooleanField(verbose_name='¿Requieres beca? si la respuesta es SI marac la casilla')
    motivo_beca = models.CharField(max_length=200, blank=True, null=True, verbose_name='Motivo de la beca')

    # Aspectos personales del estudiante
    cualidades = models.TextField(blank=True, null=True, verbose_name='Cualidades')
    habilidades = models.TextField(blank=True, null=True, verbose_name='Habilidades')
    debilidades = models.TextField(blank=True, null=True, verbose_name='Debilidades')
    valores = models.TextField(blank=True, null=True, verbose_name='Valores')
    disgustos = models.TextField(blank=True, null=True, verbose_name='Disgustos')
    temores = models.TextField(blank=True, null=True, verbose_name='Temores')
    pareja_sentimental = models.CharField(max_length=100, blank=True, null=True, verbose_name='Pareja sentimental')
    planes_matrimonio = models.CharField(max_length=100, blank=True, null=True, verbose_name='Planes de matrimonio')
    futuro_personal = models.TextField(blank=True, null=True, verbose_name='Futuro personal')
    futuro_academico = models.TextField(blank=True, null=True, verbose_name='Futuro académico')
    futuro_profesional = models.TextField(blank=True, null=True, verbose_name='Futuro profesional')
    problemas_personales = models.TextField(blank=True, null=True, verbose_name='Problemas personales')
    tiempo_libre = models.TextField(blank=True, null=True, verbose_name='Tiempo libre')
    motivacion_estudio = models.BooleanField(verbose_name='¿Tienes motivación para estudiar?')
    motivo_motivacion = models.TextField(blank=True, null=True, verbose_name='Motivo de la motivación')
    transporte_universidad = models.TextField(blank=True, null=True, verbose_name='Transporte a la universidad')
    estado_salud = models.CharField(max_length=100, blank=True, null=True, verbose_name='Estado de salud')
    tratamiento_medico = models.BooleanField(verbose_name='¿Estás en tratamiento médico?')
    tipo_tratamiento = models.TextField(blank=True, null=True, verbose_name='Tipo de tratamiento médico')
    discapacidad = models.BooleanField(verbose_name='¿Tienes alguna discapacidad?')
    tipo_discapacidad = models.TextField(blank=True, null=True, verbose_name='Tipo de discapacidad')
    ayuda_psicologica = models.BooleanField(verbose_name='¿Recibes ayuda psicológica?')
    motivo_ayuda = models.TextField(blank=True, null=True, verbose_name='Motivo de la ayuda psicológica')
    dependientes_economicos = models.TextField(blank=True, null=True, verbose_name='Dependientes económicos')

    # Aspectos académicos del estudiante
    escuela_procedencia = models.CharField(max_length=200, verbose_name='Escuela de procedencia')
    especialidad_promedio = models.CharField(max_length=100, verbose_name='Especialidad y promedio')
    motivo_universidad = models.TextField(blank=True, null=True, verbose_name='Motivo para elegir esta universidad')
    universidad_primera_opcion = models.BooleanField(verbose_name='¿Es esta universidad tu primera opción?')
    motivo_universidad_opcion = models.TextField(blank=True, null=True, verbose_name='Motivo para elegir esta opción de universidad')
    carrera_primera_opcion = models.BooleanField(verbose_name='¿Es esta carrera tu primera opción?')
    motivo_carrera_opcion = models.TextField(blank=True, null=True, verbose_name='Motivo para elegir esta opción de carrera')
    expectativas_carrera = models.TextField(blank=True, null=True, verbose_name='Expectativas de la carrera')
    examen_admision = models.BooleanField(verbose_name='¿Realizaste el examen de admisión?')
    cual_otra_escuela = models.CharField(max_length=100, blank=True, null=True, verbose_name='¿En qué otra escuela estudiaste?')
    materias_dificultad = models.TextField(blank=True, null=True, verbose_name='Materias con dificultad')
    materias_reprobadas = models.BooleanField(verbose_name='¿Reprobaste materias?')
    cuales_materias_reprobadas = models.CharField(max_length=100, blank=True, null=True, verbose_name='¿Cuáles materias reprobaste?')
    materias_facil = models.TextField(blank=True, null=True, verbose_name='Materias fáciles')
    forma_trabajar = models.CharField(max_length=10, choices=FORMA_TRABAJAR_CHOICES, verbose_name='Forma de trabajar')
    motivo_forma_trabajar = models.TextField(blank=True, null=True, verbose_name='Motivo para la forma de trabajar')
    tecnica_estudio = models.BooleanField(verbose_name='¿Usas alguna técnica de estudio?')
    cual_tecnica_estudio = models.TextField(blank=True, null=True, verbose_name='¿Cuál técnica de estudio?')
    espacio_estudio = models.BooleanField(verbose_name='¿Tienes un espacio adecuado para estudiar?')
    cual_espacio_estudio = models.CharField(max_length=100, blank=True, null=True, verbose_name='¿Cuál es tu espacio de estudio?')
    libros_apoyo = models.BooleanField(verbose_name='¿Usas libros de apoyo?')
    cantidad_libros = models.CharField(max_length=100, blank=True, null=True, verbose_name='Cantidad de libros de apoyo')
    computadora_internet = models.BooleanField(verbose_name='¿Tienes computadora con internet?')
    tipo_computadora = models.CharField(max_length=10, choices=TIPO_COMPUTADORA_CHOICES, blank=True, null=True, verbose_name='Tipo de computadora')
    tipo_internet = models.CharField(max_length=100, blank=True, null=True, verbose_name='Tipo de conexión a internet')
    planes_terminar_carrera = models.TextField(blank=True, null=True, verbose_name='Planes para terminar la carrera')
    tipo_trabajo = models.TextField(blank=True, null=True, verbose_name='Tipo de trabajo que te gustaría tener')

    def __str__(self):
        return self.nombre


