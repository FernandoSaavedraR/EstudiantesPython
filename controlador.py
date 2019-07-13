import click
from alumnos import Alumno
from alumnos_services import Services

@click.group()
def ini():
    """Gestiona los Alumnos registrados"""
    pass

@ini.command()
@click.option('-n','--name',
                type =str,
                prompt=True,
                help = 'The client name')
@click.option('-a','--age',
                type =int,
                prompt=True,
                help = 'The client age')
@click.option('-g','--group',
                type =str,
                prompt=True,
                help = 'The client group')
@click.option('-s','--score',
                type =float,
                prompt=True,
                help = 'The client score')
@click.option('-g','--gender',
                type =str,
                prompt=True,
                help = 'The client gender')
@click.pass_context
def alta(ctx,name,age,group,score,gender):
    """Da de alta un alumno con su calificacion"""
    alumno = Alumno(name,age,group,score,gender)
    servicios = Services(ctx.obj['alumnos'])
    servicios.Alta_usuario(alumno)

@ini.command()
@click.argument('uid',type=str)
@click.pass_context
def baja(ctx,uid):
    """da de baja un alumno con su id"""
    servicios = Services(ctx.obj['alumnos'])
    lista = servicios.Consulta_usuario()
    alumno = [alumno for alumno in lista if alumno['uid']==uid]
    if alumno:
        servicios.Baja_usuario(Alumno(**alumno[0]))
        click.echo('Alumno eliminado')
    else:
        click.echo('no se encontró')
    pass

@ini.command()
@click.argument('uid',type=str)
@click.pass_context
def cambio(ctx,uid):
    """actualiza un alumno"""
    servicios = Services(ctx.obj['alumnos'])
    lista = servicios.Consulta_usuario()
    alumno = [alumno for alumno in lista if alumno['uid']==uid]
    if alumno:
        alumnoN = _update_student_flow(Alumno(**alumno[0]))
        servicios.Cambio_usuario(alumnoN)
    else:
        click.echo('no se encontró')
    pass

@ini.command()
@click.pass_context
def consulta(ctx):
    """Revisa todos los alumnos"""
    servicios = Services(ctx.obj['alumnos'])
    alumnos = servicios.Consulta_usuario()
    #print(alumnos)
    click.echo('-'*171)
    click.echo('|  {uid}  |  {nombre}  |  {edad}  |  {grupo}  |  {promedio}  |  {sexo}  |'.format(
        uid = 'uid'.center(40,' '),
        nombre = 'nombre'.center(20,' '),
        edad = 'edad'.center(20,' '),
        grupo = 'grupo'.center(20,' '),
        promedio = 'promedio'.center(20,' '),
        sexo = 'sexo'.center(20,' '),
    ))
    click.echo('-'*171)
    for alumno in alumnos:
        click.echo('|  {uid}  |  {nombre}  |  {edad}  |  {grupo}  |  {promedio}  |  {sexo}  |'.format(
            uid = alumno['uid'].center(40,' '),
            nombre = alumno['nombre'].center(20,' '),
            edad = alumno['edad'].center(20,' '),
            grupo = alumno['grupo'].center(20,' '),
            promedio = alumno['promedio'].center(20,' '),
            sexo = alumno['sexo'].center(20,' '),
    ))
        click.echo('-'*171)
def _update_student_flow(student):
    click.echo('deje vacio si quiere modificar')
    student.nombre = click.prompt('nuevo nombre',type=str,default=student.nombre)
    student.edad = click.prompt('nueva edad',type=str,default=student.edad)
    student.grupo = click.prompt('nuevo grupo',type=str,default=student.grupo)
    student.sexo = click.prompt('nuevo sexo',type=str,default=student.sexo)
    student.promedio = click.prompt('nuevo promedio',type=str,default=student.promedio)
    return student


all = ini