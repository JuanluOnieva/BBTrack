from flask import Flask, request, jsonify, request, make_response, render_template, abort, send_file, send_from_directory
from flask_restplus import Resource, Api, fields
from Paciente import Paciente
from Informe import Informe
from Prueba import Prueba
from Historial import Historial
from Paciente import get_historial, get_Licencia, lista_pacientes, pacientes_filter, get_paciente, lista_pacientes_embarazadas
from Informe import get_ICD10, get_prueba, lista_informes, get_informe, get_consultas, get_informe_historial
from Historial import get_historial, get_FRR, get_informes, lista_historial
from Prueba import lista_pruebas, get_prueba, get_prueba_from_informe
from ICD10 import lista_ICD10, get_ICD10, create_ICD10
from Medico import lista_medicos, get_medico
from Usuario import lista_usuarios
from pprint import pprint
from bbTrackXML import bbTrackXMLjar, bbTrackXMLjar_paciente
import os
from rdfParser import bbTrackRDF

app = Flask(__name__, static_folder="static")                  #  Create a Flask WSGI application

"""Version de la api, con titulo y descripcion"""
api = Api(app, version='1.0', title='bbTrack API', description='API para web bbTrack')

"""
Documentacion de las clases
"""


pacienteClass = api.model('Paciente', {
    'idPaciente': fields.String(readOnly=True, description='Identificador del paciente en la Base de Datos'),
    'Nombre': fields.String(required=True, description='Nombre del paciente'),
    'NUSS': fields.String(required=True, description='Número de la SS unico del paciente'),
    'Sexo': fields.String(required=True, description='Sexo del paciente'),
    'Fecha_nacimiento': fields.Date(required=True, description='Fecha de nacimiento del paciente'),
    'Localidad': fields.String(required=True, description='Localidad actual del paciente'),
    'Domicilio': fields.String(required=True, description='Domicilio actual del paciente'),
    'Apellidos': fields.String(required=True, description='Apellidos del paciente'),
    'Telefono': fields.String(required=False, description='Telefono del paciente'),
    'Correo_electronico': fields.String(required=False, description='Correo electronico del paciente'),
    'Embarazada': fields.String(required=True, description='Booleano para saber si la paciente se encuentra embarazada'),
    'FPP': fields.String(required=False, description='Fecha probable de parto en caso de que la paciente se encuentre embarazada'),
    'historial': fields.String(required=False, description='Identificador del historial del paciente en la Base de Datos'),
    'Licencia': fields.List(fields.String, required=False, description='Licencia del medico que ha atendido al paciente')
})




informeClass = api.model('Informe', {
    'idInforme': fields.String(readOnly=True, description='Identificador del informe en la Base de Datos'),
    'Estado_paciente': fields.String(required=True, description='Variable que indica la situacion actual de la paciente'),
    'Diagnostico': fields.String(required=True, description='Diagnostico realizado del paciente'),
    'idHistorial': fields.String(required=True, description='Identificador del historial del paciente en la Base de Datos'),
    'idConsulta': fields.String(required=True, description='Identificador de la consulta donde es atendido el paciente'),
    'Fecha_consulta': fields.String(required=True, description='Fecha de la consulta'),
    'Licencia_medico': fields.String(required=True, description='Licencia del medico que ha atendido al paciente'),
    'Pruebas': fields.List(fields.String, required=False, description='Lista de pruebas requeridas para el seguimiento del paciente'),
    'ICD10s': fields.List(fields.String, required=False, description='Lista de codigos de ICD10 referente al paciente')
})


FRRClass = api.model('FRR', {
        'Antecedentes_familiares': fields.String(required=False, description=''),
        'Factores_psicosociales': fields.String(required=False, description=''),
        'Antecedentes_obstetricos': fields.String(required=False, description=''),
        'Antecedentes_personales': fields.String(required=False, description=''),
        'Patologia_materna': fields.String(required=False, description=''),
        'Riesgos_especificos': fields.String(required=False, description=''),
        'Exposicion_a_teratogenos': fields.String(required=False, description='')
    })

historialClass = api.model('Historial', {
    'idHistorial': fields.String(required=True, description='Identificador del historial del paciente en la Base de Datos'),
    'fecha_primera_consulta': fields.Date(required=True, description='Fecha de la primera consulta'),
    'idPaciente': fields.String(required=True, description='Identificador del paciente al que pertenece el historial en la Base de Datos'),
    'vacunas': fields.String(required=True, description='Vacunas que tiene el paciente'),
    'informes': fields.List(fields.String, required=True, description='Lista de Informes que tiene un paciente'),
    'FRR': fields.Nested(FRRClass)
})


medicoClass = api.model('Medico', {
    'Licencia': fields.String(required=True, description='Licencia medica'),
    'Nombre': fields.String(required=True, description='Nombre del medico'),
    'Apellidos': fields.String(required=True, description='Apellidos del medico'),
    'Sexo': fields.String(required=True, description='Genero'),
    'Especialidad': fields.String(required=True, description='Especialidad del medico'),
    'informes': fields.List(fields.String, required=True, description='Informes que ha escrito un medico'),
    'Pacientes': fields.List(fields.String, required=True, description='Pacientes que atiende un medico'),
})




pruebaClass = api.model('Prueba', {
    'idPrueba': fields.String(required=True, description='Identificador de la prueba'),
    'Observaciones': fields.String(required=True, description='Observaciones del medico tecnico que realiza la prueba'),
    'idPrueba_Externo': fields.String(required=True, description=''),
    'Tipo': fields.String(required=True, description='Tipo de prueba Rutinaria o Especial'),
    'Nombre': fields.String(required=True, description='Nombre de la prueba'),
    'idInforme': fields.String(required=True, description='Identificador del informe al que pertenece la prueba')
})



ICD10Class = api.model('ICD10', {
    'Codigo': fields.String(required=True, description='Codigo ICD10'),
    'Nombre': fields.String(required=True, description='Nombre de la enfermedad'),
    'informes': fields.List(fields.String, required=True, description='Informes en los que aparece el ICD10'),
})


UsuarioClass = api.model('Usuario', {
    'idUsuario': fields.String(required=True, description='Usuario de un medico'),
    'PSS': fields.String(required=True, description='Contrasenya de un medico'),
})

listICD10Class = api.model('listICD10', {
    'Codigo': fields.List(fields.String, required=True, description='Informes en los que aparece el ICD10'),
})


## Render template

# Run python code

## Descargas
@app.route('/html/descargas')
def render_descargas():
    return render_template('Descargas/descargas.html')


@app.route("/computeXML/<string:argument>", methods=["POST"])  # consider to use more elegant URL in your JS
def compute_xml(argument):
    print(argument)
    bbTrackXMLjar(argument)
    return argument

@app.route("/computeXML/paciente/<string:idPaciente>", methods=["POST"])  # consider to use more elegant URL in your JS
def compute_xml_paciente(idPaciente):
    print(idPaciente)
    bbTrackXMLjar_paciente(idPaciente)
    return idPaciente

@app.route("/downloadXML/<string:argument>")  # consider to use more elegant URL in your JS
def download_xml(argument):
    try:
        print("aqui")
        return send_file('static/download/' + argument + '.zip', as_attachment=True)
        #return send_from_directory(directory = 'static/download/', filename= argument + '.zip')
    except Exception as e:
        return str(e)

@app.route("/downloadXML/paciente/<string:idPaciente>")  # consider to use more elegant URL in your JS
def download_xml_paciente(idPaciente):
    try:
        print("aqui")
        return send_file('static/download/' + idPaciente + '.zip', as_attachment=True)
        #return send_from_directory(directory = 'static/download/', filename= argument + '.zip')
    except Exception as e:
        return str(e)

@app.route("/computeRDF", methods=["POST"])  # consider to use more elegant URL in your JS
def compute_rdf():
    print("rdf")
    bbTrackRDF()
    return "ok"

@app.route("/downloadRDF")
def download_rdf():
    try:
        print("aqui")
        return send_file('static/download/bbTrack.rdf', as_attachment=True)
    except Exception as e:
        return str(e)

# Login
@app.route('/html/login')
def render_inicio():
    return render_template('Login/login.html')

# Home

## Home general
@app.route('/html/home')
def render_home():
    return render_template('Home/analisis_general.html', num_pacientes = len(lista_pacientes()), num_pacientes_embarazadas= len(lista_pacientes_embarazadas())
                           , num_medicos = len(lista_medicos())
                           , num_pruebas = len(lista_pruebas()), num_informes = len(lista_informes()))

## Home individual
@app.route('/html/home/individual')
def render_home_individual():
    return render_template('Home/analisis_individual.html')

## Home grupal
@app.route('/html/home/grupal')
def render_home_grupal():
    return render_template('Home/analisis_grupal.html')

## Lista Pacientes
@app.route('/html/pacientes')
def render_pacientes():
    return render_template('Pacientes/listaPacientes.html', pacientes=lista_pacientes())

## Paciente Particular
@app.route('/html/pacientes/<int:idPaciente>')
def render_paciente(idPaciente):
    paciente = get_paciente(idPaciente)
    historial = get_historial(paciente.historial)
    informes = get_informe_historial(historial.idHistorial)
    if paciente is None:
        abort(404)
    return render_template('Pacientes/paciente.html', paciente=paciente, historial=historial, informes=informes)

## Informe particular
@app.route('/html/informes/<string:idInforme>')
def render_informe(idInforme):
    informe = get_informe(idInforme)
    pruebas = get_prueba_from_informe(informe.idInforme)
    if informe is None:
        abort(404)
    return render_template('Informes/informe.html', informe=informe, pruebas=pruebas)

## Informes de un paciente
@app.route('/html/historial/<string:idHistorial>/informes')
def render_informe_historial(idHistorial):
    informe = get_informe_historial(idHistorial)
    if informe is None:
        abort(404)
    return render_template('Informes/informeHistorial.html', informes=informe)

## Pruebas de un informe
@app.route('/html/informes/<string:idInforme>/pruebas')
def render_prueba_informe(idInforme):
    prueba = get_prueba_from_informe(idInforme)
    if prueba is None:
        abort(404)
    return render_template('Pruebas/pruebas.html', pruebas=prueba)

## Buscador ICD10
@app.route('/html/buscador')
def render_buscador():
    return render_template('Buscador/buscador.html')

## Formulario Informe
@app.route('/html/formulario/informe')
def render_formulario_informe():
    return render_template('Formulario/informeFormulario.html', pacientes = lista_pacientes(), consultas = get_consultas())

## Añadir prueba o ICD10 a informe
@app.route('/html/informe/formulario/<string:idInforme>')
def render_informe_formulario(idInforme):
    return render_template('Formulario/informe.html', informe=get_informe(idInforme), ICD10s = lista_ICD10(), pruebas = get_prueba_from_informe(idInforme))


"""
LLAMADAS API
"""

@api.route('/api/pacientes')
class PacientesCollection(Resource):

    @api.doc('lista_pacientes')
    @api.response(400, 'Lista vacia')
    @api.marshal_list_with(pacienteClass)
    def get(self):
        pacientes = lista_pacientes()
        idPaciente = request.args.get('idPaciente')
        Apellidos = request.args.get('Apellidos')
        Embarazada = request.args.get('Embarazada')
        if len(pacientes) > 0:
            if idPaciente or Apellidos or Embarazada:
                return pacientes_filter(pacientes, idPaciente, Apellidos, Embarazada)
            else:
                pprint(vars(pacientes[0]))
                return pacientes
        else:
            return "Formato incorrecto", 400

@api.route('/api/pacientes/<string:idPaciente>')
@api.response(404, 'Paciente no encontrada.')
@api.param('idPaciente', 'El identificador de una paciente')
class PacienteItem(Resource):

    @api.doc('get_paciente')
    @api.marshal_with(pacienteClass)
    def get(self, idPaciente):
        paciente = get_paciente(idPaciente)
        if paciente is None:
            return "Error", 404
        else:
            pprint(vars(paciente))
            return paciente

    @api.response(204, 'Paciente actualizado correctamente')
    @api.expect(pacienteClass)
    @api.marshal_with(pacienteClass)
    def put(self, idPaciente):
        paciente = get_paciente(idPaciente)
        pprint(vars(paciente))
        if paciente is None:
            return "Error", 404
        paciente.update_paciente(request.json.get('Localidad', None), request.json.get('Domicilio', None),
                                 request.json.get('Telefono', None),
                                 request.json.get('Correo_electronico', None), request.json.get('Embarazada', None),
                                 request.json.get('FPP', None))
        if not request.json:
            return "Formato invalido", 400
        return paciente, 204

    @api.response(201, 'Informe creado correctamente')
    @api.response(400, 'Formato del informe incorrecto')
    @api.expect(informeClass)
    @api.doc('create_informe')
    @api.marshal_with(informeClass, code=201)
    def post(self):
        if not request.json or not 'Estado_paciente' in request.json or not 'Diagnostico' in request.json or not 'idHistorial' in request.json \
                or not 'idConsulta' in request.json or not 'Fecha_consulta' in request.json or not 'Licencia_medico' in request.json:
            return "Formato incorrecto", 400
        informe = Informe()
        informe.new_informe(None, request.json['Estado_paciente'], request.json['Diagnostico'], request.json['idHistorial'],
                          request.json['Fecha_consulta'], request.json['idConsulta'], request.json['Licencia_medico'],
                          request.json.get('Pruebas', list()), request.json.get('ICD10s', list()))
        informe.insert_informe()
        return informe, 201


@api.route('/api/pacientes/<string:idPaciente>/informes')
@api.response(404, 'Paciente no encontrada.')
@api.param('idPaciente', 'El identificador de una paciente')
class PacienteInformesCollection(Resource):

    @api.doc('get_paciente_informes')
    @api.marshal_list_with(informeClass)
    def get(self, idPaciente):
        paciente = get_paciente(idPaciente)
        informes = lista_informes()
        result = list()
        for informe in informes:
            if paciente.historial == informe.idHistorial:
                result.append(informe)
        if result is None:
            return "Error", 404
        else:
            return result

    @api.response(201, 'Informe creado correctamente')
    @api.response(400, 'Formato del informe incorrecto')
    @api.expect(informeClass)
    @api.doc('create_informe')
    @api.marshal_with(informeClass, code=201)
    def post(self, idPaciente):
        historial = get_paciente(idPaciente).historial
        if not request.json or not 'Estado_paciente' in request.json or not 'Diagnostico' in request.json \
                or not 'idConsulta' in request.json or not 'Fecha_consulta' in request.json or not 'Licencia_medico' in request.json:
            return "Formato incorrecto", 400
        informe = Informe()
        print(request)
        informe.new_informe(None, request.json['Estado_paciente'], request.json['Diagnostico'], historial,
                          request.json['Fecha_consulta'], request.json['idConsulta'], request.json['Licencia_medico'],
                          request.json.get('Pruebas', list()), request.json.get('ICD10s', list()))
        informe.insert_informe()
        return informe, 201


@api.route('/api/pacientes/<string:idPaciente>/historial')
@api.response(404, 'Paciente no encontrada.')
@api.param('idPaciente', 'El identificador de una paciente')
class PacienteHistorialItem(Resource):

    @api.doc('get_paciente_historial')
    @api.marshal_with(historialClass)
    def get(self, idPaciente):
        paciente = get_paciente(idPaciente)
        historiales = lista_historial()
        result = list()
        paciente_historial = None
        for historial in historiales:
            if paciente.historial == historial.idHistorial:
                paciente_historial = historial
                break
        if result is None:
            return "Error", 404
        else:
            return paciente_historial


'''Dame todas las pruebas de un paciente'''
@api.route('/api/pacientes/<string:idPaciente>/pruebas')
class PacientePruebasCollection(Resource):

    @api.response(404, 'Paciente no encontrada.')
    @api.param('idPaciente', 'El identificador de una paciente')
    @api.doc('get_paciente_pruebas')
    @api.marshal_list_with(pruebaClass)
    def get(self, idPaciente):
        paciente = get_paciente(idPaciente)
        informes = lista_informes()
        result_idPruebas = list()
        for informe in informes:
            if paciente.historial == informe.idHistorial:
                result_idPruebas.extend(informe.Pruebas)
        pruebas = lista_pruebas()
        result_pruebas = list()
        for prueba in pruebas:
            if prueba.idPrueba in result_idPruebas:
                result_pruebas.append(prueba)
        if result_pruebas is None:
            return "Error", 404
        else:
            return result_pruebas


@api.route('/api/informes')
class InformeCollection(Resource):

    @api.doc('lista_informes')
    @api.response(400, 'Lista vacia')
    @api.marshal_list_with(informeClass)
    def get(self):
        informes = lista_informes()
        if len(informes) > 0:
            return informes
        else:
            return "Formato incorrecto", 400


@api.route('/api/informes/<string:idInforme>')
class InformeItem(Resource):

    @api.response(404, 'Informe no encontrado.')
    @api.param('idInforme', 'El identificador de un informe')
    @api.doc('get_informe')
    @api.marshal_with(informeClass)
    def get(self, idInforme):
        informe = get_informe(idInforme)
        if informe is None:
            return "Error", 404
        else:
            return informe

    @api.response(204, 'Informe eliminado correctamente')
    @api.doc('eliminar_informe')
    def delete(self, idInforme):
        informe = get_informe(idInforme)
        if informe is None:
            return "Error", 404
        informe.delete_informe()
        return None, 204


@api.route('/api/informes/<string:idInforme>/ICD10')
class InformeICD10Collection(Resource):

    @api.response(404, 'Informe no encontrado.')
    @api.param('idInforme', 'El identificador de un informe')
    @api.doc('get_informe_icd10')
    @api.marshal_list_with(ICD10Class)
    def get(self, idInforme):
        informe = get_informe(idInforme)
        icd10s = lista_ICD10()
        result = list()
        for icd10 in icd10s:
            if informe.idInforme in icd10.informes:
                result.append(icd10)
        if result is None:
            return "Error", 404
        else:
            return result

    @api.response(201, 'ICD10 anyadido correctamente')
    @api.response(400, 'Formato del ICD10 incorrecto')
    @api.expect(ICD10Class)
    @api.doc('add_icd10')
    @api.marshal_list_with(ICD10Class, code=201)
    def post(self, idInforme):
        if not request.json or not 'Codigo' in request.json:
            return "Formato incorrecto", 400
        informe = get_informe(idInforme)
        print(idInforme)
        print(informe.idInforme)
        informe.insert_icd10(request.json['Codigo'])
        icd10s = lista_ICD10()
        result = list()
        for icd10 in icd10s:
            if idInforme in icd10.informes:
                result.append(icd10)
        if result is None:
            return "Error", 404
        else:
            return result, 201


'''Dame todas las pruebas de un informe'''
@api.route('/api/informes/<string:idInforme>/pruebas')
class InformesPruebasCollection(Resource):

    @api.response(404, 'Pruebas no encontradas.')
    @api.param('idInforme', 'El identificador de un informe')
    @api.doc('get_informe_pruebas')
    @api.marshal_list_with(pruebaClass)
    def get(self, idInforme):
        pruebas = lista_pruebas()
        result = list()
        for prueba in pruebas:
            pprint(vars(prueba))
            print("idInforme " + idInforme)
            if idInforme in prueba.idInforme:
                result.append(prueba)
        if result is None:
            return "Error", 404
        else:
            return result

    @api.response(201, 'Prueba creado correctamente')
    @api.response(400, 'Formato de la prueba incorrecto')
    @api.expect(pruebaClass)
    @api.doc('create_prueba')
    @api.marshal_with(pruebaClass, code=201)
    def post(self, idInforme):
        if not request.json or not 'Observaciones' in request.json\
                or not 'Tipo' in request.json or not 'Nombre' in request.json:
            return "Formato incorrecto", 400
        prueba = Prueba()
        prueba.new_prueba(None, request.json['Observaciones'],
                          None, request.json['Tipo'],
                          idInforme, request.json['Nombre'])
        pprint(prueba)
        prueba.insert_prueba()
        return prueba, 201

@api.route('/api/historiales')
class HistorialesCollection(Resource):

    @api.doc('lista_historiales')
    @api.response(400, 'Lista vacia')
    @api.marshal_list_with(historialClass)
    def get(self):
        historiales = lista_historial()
        if len(historiales) > 0:
            print(str(len(historiales)))
            return historiales
        else:
            return "Formato incorrecto", 400

@api.route('/api/historiales/<string:idHistorial>')
class HistorialItem(Resource):

    @api.response(404, 'Historial no encontrado.')
    @api.param('idHistorial', 'El identificador de un historial')
    @api.doc('get_historial')
    @api.marshal_with(historialClass)
    def get(self, idHistorial):
        historial = get_historial(idHistorial)
        if historial is None:
            return "Error", 404
        else:
            return historial


@api.route('/api/medicos')
class MedicoCollection(Resource):

    @api.doc('lista_medicos')
    @api.response(400, 'Lista vacia')
    @api.marshal_list_with(medicoClass)
    def get(self):
        medicos = lista_medicos()
        print(str(len(medicos)))
        if len(medicos) > 0:
            return medicos
        else:
            return "Formato incorrecto", 400


@api.route('/api/medicos/<string:Licencia>')
class MedicoItem(Resource):

    @api.response(404, 'Medico no encontrado.')
    @api.param('id', 'El identificador de un medico')
    @api.doc('get_medico')
    @api.marshal_with(medicoClass)
    def get(self, Licencia):
        medico = get_medico(Licencia)
        if medico is None:
            return "Error", 404
        else:
            pprint(vars(medico))
            return medico

@api.route('/api/pruebas')
class PruebasCollection(Resource):

    @api.doc('lista_pruebas')
    @api.response(400, 'Lista vacia')
    @api.marshal_list_with(pruebaClass)
    def get(self):
        pruebas = lista_pruebas()
        '''print(str(len(pruebas)))'''
        if len(pruebas) > 0:
            return pruebas
        else:
            return "Formato incorrecto", 400

@api.route('/api/pruebas/<string:idPrueba>')
class PruebaItem(Resource):

    @api.response(404, 'Prueba no encontrada.')
    @api.param('id', 'El identificador de una prueba')
    @api.doc('get_prueba')
    @api.marshal_with(pruebaClass)
    def get(self, idPrueba):
        prueba = get_prueba(idPrueba)
        if prueba is None:
            return "Error", 404
        else:
            return prueba

@api.route('/api/ICD10')
class ICD10Collection(Resource):

    @api.doc('lista_ICD10')
    @api.response(400, 'Lista vacia')
    @api.marshal_list_with(ICD10Class)
    def get(self):
        icd10s = lista_ICD10()
        print(str(len(icd10s)))
        if len(icd10s) > 0:
            return icd10s
        else:
            return "Formato incorrecto", 400

    @api.response(201, 'ICD10 anyadido correctamente')
    @api.response(400, 'Formato del ICD10 incorrecto')
    @api.expect(ICD10Class)
    @api.doc('add_icd10_new')
    @api.marshal_list_with(ICD10Class, code=201)
    def post(self):
        if not request.json or not 'Codigo' in request.json or not 'Nombre':
            return "Formato incorrecto", 400
        icd = create_ICD10(request.json['Codigo'], request.json['Nombre'])
        if icd is None:
            return "Error", 404
        else:
            return icd, 201


@api.route('/api/ICD10/<string:Codigo>')
class ICD10Item(Resource):

    @api.response(404, 'ICD10 no encontrado.')
    @api.param('id', 'El identificador de un ICD10')
    @api.doc('get_ICD10')
    @api.marshal_with(ICD10Class)
    def get(self, Codigo):
        icd10 = get_ICD10(Codigo)
        if icd10 is None:
            return "Error", 404
        else:
            pprint(vars(icd10))
            return icd10

@api.route('/api/ICD10/all')
class ICD10All(Resource):

    @api.response(404, 'ICD10 no encontrado.')
    @api.param('id', 'El identificador de un ICD10')
    @api.doc('get_ICD10_all')
    def get(self):
        informes = lista_informes()
        result = list()
        icd10s = lista_ICD10()
        for informe in informes:
            result.extend(informe.ICD10s)
        print(str(result))
        if result is None:
            return "Error", 404
        else:
            return result


@api.route('/api/usuarios')
class UsuarioCollection(Resource):
    @api.doc('lista_usuarios')
    @api.response(400, 'Lista vacia')
    @api.marshal_list_with(UsuarioClass)
    def get(self):
        usuarios = lista_usuarios()
        if len(usuarios) > 0:
            return usuarios
        else:
            return "Formato incorrecto", 400
