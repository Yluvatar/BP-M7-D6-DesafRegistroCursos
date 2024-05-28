from app.models import *
from datetime import datetime, date


def crear_curso(codigo, nombre, version):
    resp = Curso.objects.create(codigo=codigo, nombre=nombre, version=version)
    if resp:
        respuesta = f"Se ha creado el curso: {codigo} - {nombre}, v:{version}"
    else:
        respuesta = f"Error al crear el curso: {codigo} - {nombre}, v:{version}"
    print(respuesta)
    return resp


def crear_profesor(rut, nombre, apellido):
    resp = Profesor.objects.create(nombre=nombre, apellido=apellido, rut=rut)
    if resp:
        respuesta = f"Se ha creado el profesor: {rut} - {nombre} {apellido}"
    else:
        respuesta = f"Error al crear el profesor: {rut} - {nombre} {apellido}"
    print(respuesta)
    return resp

def crear_estudiante(rut, nombre, apellido, fecha_nacimiento, creado_por = '', activo = True):
    resp = Estudiante.objects.create(rut=rut, nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, activo=activo, creado_por=creado_por)
    if resp:
        respuesta = f"Se ha creado el estudiante {rut}  - {nombre} {apellido}"
    else:
        respuesta = f"Error al crear el estudiante {rut}  - {nombre} {apellido}"
    print(respuesta)
    return resp


def crear_direccion(calle, numero, dpto, comuna, ciudad, region, estudiante_id):
    resp = Direccion.objects.create(calle=calle, numero=numero, dpto=dpto, comuna=comuna, ciudad=ciudad, region=region, estudiante_id=estudiante_id)
    if resp:
        respuesta = f"Se ha creado la direccion: {calle} {numero} {dpto} {comuna} {ciudad} {region} para el estudiante: {estudiante_id}"
    else:
        respuesta = f"Error al crear la direccion: {calle} {numero} {dpto} {comuna} {ciudad} {region} para el estudiante: {estudiante_id}"
    print(respuesta)
    return resp


def obtiene_estudiante(rut):
    if isinstance(rut, Estudiante):
        rut = rut.rut
    resp = Estudiante.objects.get(rut=rut)
    print(f"Se ha encontrado el estudiante: {resp.nombre} {resp.apellido}")
    return resp


def obtiene_profesor(rut):
    if isinstance(rut, Profesor):
        rut = rut.rut
    resp = Profesor.objects.get(rut=rut)
    print(f"Se ha encontrado el profesor: {resp.nombre} {resp.apellido}")
    return resp


def obtiene_curso(codigo):
    if isinstance(codigo, Curso):
        codigo = codigo.codigo
    return Curso.objects.get(codigo=codigo)


def agrega_profesor_a_curso(curso_id, rut):
    if isinstance(rut, Profesor):
        rut = rut.rut
    if isinstance(curso_id, Curso):
        curso_id = curso_id.codigo
    return Curso.objects.get(codigo=curso_id).profesor_id.add(rut)


def agrega_cursos_a_estudiante(rut, curso):
    if isinstance(rut, Estudiante):
        rut = rut.rut
    if isinstance(curso, Curso):
        curso = curso.codigo
    return Curso.objects.get(codigo=curso).estudiante_id.add(rut)


def imprime_estudiante_cursos(rut):
    if isinstance(rut, Estudiante):
        rut = rut.rut
    cursos = Curso.objects.filter(estudiante_id=rut).all()
    print(f"Los cursos que el estudiante {rut} tiene son:")
    for curso in cursos:
        print(f"- {curso}")
    #return Estudiante.objects.get(rut=rut).curso.all()
