from rdflib import Namespace, Graph
from rdflib.namespace import RDF, FOAF, OWL, RDFS, XSD
from rdflib import URIRef, BNode, Literal
from rdflib import Graph
from Paciente import lista_pacientes, Paciente
from Historial import Historial, get_historial, lista_historial, get_informes
from Informe import Informe, get_informe, lista_informes, get_prueba, get_ICD10
from Prueba import get_prueba as get_prueba_from_prueba
from ICD10 import get_ICD10 as get_ICD10_from_ICD10
import os


def bbTrackRDF():
    os.system("rm static/download/bbTrack.rdf")
    n = Namespace("http://uma.org/EDAID/bbTrack/#")
    #Paciente
    tieneNombre = URIRef(n + "tieneNombre")
    tieneNUSS = URIRef(n+"tieneNUSS")
    tieneFechaNacimiento=URIRef(n + "tieneFechaNacimiento")
    tieneTelefono=URIRef(n + "tieneTelefono")
    tieneEmail=URIRef(n + "tieneEmail")
    estaEmbarazada = URIRef(n + "estaEmbarazada")
    tieneHistorial = URIRef(n + "hasHitorial")

    #Historial
    tieneFechaPrimeraConsulta = URIRef(n + "tieneFechaPrimeraConsulta")
    tieneInformes = URIRef(n + "tieneInformes")

    #Informe
    tieneEstado = URIRef(n + "tieneEstado")
    tieneDiagnostico = URIRef(n + "tieneDiagnostico")
    tieneFechaConsulta = URIRef(n + "tieneFechaConsulta")
    tienePruebas = URIRef(n + "tienePruebas")
    tieneICD10 = URIRef(n + "tieneICD10")

    #Prueba
    tieneNombrePrueba = URIRef(n + "tieneNombrePrueba")
    tieneObservaciones = URIRef(n + "tieneObservaciones")
    tieneTipo = URIRef(n + "tieneTipo")

    #ICD10
    tieneCodigo = URIRef(n + "tieneCodigo")
    tieneDescripcion = URIRef(n + "tieneDescripcion")

    g = Graph()
    pacientes = lista_pacientes()
    informes = lista_informes()

    for paciente in pacientes:
        ## crea clase pacienteObj
        pacienteObj = URIRef(n + paciente.idPaciente)
        Domicilio = Literal(paciente.Domicilio)
        Localidad = Literal(paciente.Localidad)
        g.add((pacienteObj, RDF.type, FOAF.Paciente))
        g.add((pacienteObj, FOAF.Domicilio, Domicilio))
        g.add((pacienteObj, FOAF.Localidad, Localidad))

        ## data prop estaEmbarazada
        g.add((estaEmbarazada, RDF.type, OWL.DataProperty))
        g.add((estaEmbarazada, RDFS.domain, FOAF.Person))
        g.add((estaEmbarazada, RDFS.range, XSD.boolean))
        g.add((pacienteObj, estaEmbarazada, Literal(str(paciente.Embarazada))))
        ##data prop tieneNombre
        g.add((tieneNombre, RDF.type, OWL.DataProperty))
        g.add((tieneNombre, RDFS.domain, FOAF.Person))
        g.add((tieneNombre, RDFS.range, XSD.string))
        g.add((pacienteObj, tieneNombre, Literal(paciente.Nombre + " " + paciente.Apellidos)))
        ##data prop tieneNUSS
        g.add((tieneNUSS, RDF.type, OWL.DataProperty))
        g.add((tieneNUSS, RDFS.domain, FOAF.Person))
        g.add((tieneNUSS, RDFS.range, XSD.string))
        g.add((pacienteObj, tieneNUSS, Literal(paciente.NUSS)))
        ##data prop tieneFechaNacimiento
        g.add((tieneFechaNacimiento, RDF.type, OWL.DataProperty))
        g.add((tieneFechaNacimiento, RDFS.domain, FOAF.Person))
        g.add((tieneFechaNacimiento, RDFS.range, XSD.date))
        g.add((pacienteObj, tieneFechaNacimiento, Literal(paciente.Fecha_nacimiento)))
        ##data prop tieneTelefono
        g.add((tieneTelefono, RDF.type, OWL.DataProperty))
        g.add((tieneTelefono, RDFS.domain, FOAF.Person))
        g.add((tieneTelefono, RDFS.range, XSD.string))
        g.add((pacienteObj, tieneTelefono, Literal(paciente.Telefono)))
        ##data prop tieneEmail
        g.add((tieneEmail, RDF.type, OWL.DataProperty))
        g.add((tieneEmail, RDFS.domain, FOAF.Person))
        g.add((tieneEmail, RDFS.range, XSD.string))
        g.add((pacienteObj, tieneEmail, Literal(paciente.Correo_electronico)))
        # selected_historial = get_historial(pacienteObj.historial)


        if paciente.historial is None:
            continue;
        ## crea clase historial
        historial = get_historial(paciente.historial)
        historialObj = URIRef(n + str(paciente.historial))
        Vacunas = Literal(historial.Vacunas)
        g.add((historialObj, RDF.type, FOAF.Historial))
        g.add((historialObj, FOAF.Vacunas, Vacunas))

        ## data prop tieneFechaPrimeraConsulta
        if historial.Fecha_primera_consulta is not None:
            g.add((tieneFechaPrimeraConsulta, RDF.type, OWL.DataProperty))
            g.add((tieneFechaPrimeraConsulta, RDFS.domain, FOAF.Historial))
            g.add((tieneFechaPrimeraConsulta, RDFS.range, XSD.date))
            print(historial.Fecha_primera_consulta)
            g.add((historialObj, tieneFechaPrimeraConsulta, Literal(historial.Fecha_primera_consulta)))

        ##object property tieneHistorial y añade typo, dominio y rango
        g.add((tieneHistorial, RDF.type, OWL.ObjectProperty))
        g.add((tieneHistorial, RDFS.domain, FOAF.Paciente))
        g.add((tieneHistorial, RDFS.range, FOAF.Historial))
        g.add((pacienteObj, tieneHistorial, historialObj))

        for informe in get_informes(paciente.historial):
            informe = get_informe(informe)
            ## crea clase InformeObj
            informeObj = URIRef(n + informe.idInforme)
            g.add((informeObj, RDF.type, FOAF.Informe))
            ## data prop tieneEstado
            g.add((tieneEstado, RDF.type, OWL.DataProperty))
            g.add((tieneEstado, RDFS.domain, FOAF.Informe))
            g.add((tieneEstado, RDFS.range, XSD.string))
            g.add((informeObj, tieneEstado, Literal(informe.Estado_paciente)))
            ## data prop tieneDiagnostico
            g.add((tieneDiagnostico, RDF.type, OWL.DataProperty))
            g.add((tieneDiagnostico, RDFS.domain, FOAF.Informe))
            g.add((tieneDiagnostico, RDFS.range, XSD.string))
            g.add((informeObj, tieneDiagnostico, Literal(informe.Diagnostico)))
            ## data prop tieneFechaConsulta
            g.add((tieneFechaConsulta, RDF.type, OWL.DataProperty))
            g.add((tieneFechaConsulta, RDFS.domain, FOAF.Informe))
            g.add((tieneFechaConsulta, RDFS.range, XSD.date))
            g.add((informeObj, tieneFechaConsulta, Literal(informe.Fecha_consulta)))
            #object property tieneInformes
            g.add((tieneInformes, RDF.type, OWL.ObjectProperty))
            g.add((tieneInformes, RDFS.domain, FOAF.Historial))
            g.add((tieneInformes, RDFS.range, FOAF.Informe))
            g.add((historialObj, tieneInformes, informeObj))

            ## Las pruebas estan asociadas a un informe
            for prueba in get_prueba(informe.idInforme):
                prueba = get_prueba_from_prueba(prueba)
                ## crea clase PruebaObj
                pruebaObj = URIRef(n + prueba.idPrueba_Externo)
                g.add((pruebaObj, RDF.type, FOAF.Prueba))
                ##Data property tieneNombrePrueba
                g.add((tieneNombrePrueba, RDF.type, OWL.DataProperty))
                g.add((tieneNombrePrueba, RDFS.domain, FOAF.Prueba))
                g.add((tieneNombrePrueba, RDFS.range, XSD.string))
                g.add((pruebaObj, tieneNombrePrueba, Literal(prueba.Nombre)))
                ##Data property tieneObservaciones
                g.add((tieneObservaciones, RDF.type, OWL.DataProperty))
                g.add((tieneObservaciones, RDFS.domain, FOAF.Prueba))
                g.add((tieneObservaciones, RDFS.range, XSD.string))
                g.add((pruebaObj, tieneObservaciones, Literal(prueba.Observaciones)))
                ##Data property tieneTipo
                g.add((tieneTipo, RDF.type, OWL.DataProperty))
                g.add((tieneTipo, RDFS.domain, FOAF.Prueba))
                g.add((tieneTipo, RDFS.range, XSD.string))
                g.add((pruebaObj, tieneTipo, Literal(prueba.Tipo)))
                # object property tienePruebas
                g.add((tienePruebas, RDF.type, OWL.ObjectProperty))
                g.add((tienePruebas, RDFS.domain, FOAF.Informe))
                g.add((tienePruebas, RDFS.range, FOAF.Prueba))
                g.add((informeObj, tienePruebas, pruebaObj))

            ## Los ICD10 estan asociados a un informe
            for ICD10 in get_ICD10(informe.idInforme):
                ICD10 = get_ICD10_from_ICD10(ICD10)
                ## crea clase ICD10Obj
                ICD10Obj = URIRef(n + ICD10.Codigo)
                g.add((ICD10Obj, RDF.type, FOAF.ICD10))
                ##Data property tieneCodigo
                g.add((tieneCodigo, RDF.type, OWL.DataProperty))
                g.add((tieneCodigo, RDFS.domain, FOAF.ICD10))
                g.add((tieneCodigo, RDFS.range, XSD.string))
                g.add((ICD10Obj, tieneCodigo, Literal(ICD10.Codigo)))
                ##Data property tieneDescripcion
                g.add((tieneDescripcion, RDF.type, OWL.DataProperty))
                g.add((tieneDescripcion, RDFS.domain, FOAF.ICD10))
                g.add((tieneDescripcion, RDFS.range, XSD.string))
                g.add((ICD10Obj, tieneDescripcion, Literal(ICD10.Nombre)))
                # object property tienePruebas
                g.add((tieneICD10, RDF.type, OWL.ObjectProperty))
                g.add((tieneICD10, RDFS.domain, FOAF.Informe))
                g.add((tieneICD10, RDFS.range, FOAF.ICD10))
                g.add((informeObj, tieneICD10, ICD10Obj))
                ## seguir con el resto

    g.serialize(destination='static/download/bbTrack.rdf', format='xml')


''' bbTrackRDF():
    os.system("rm static/download/bbTrack.rdf")
    n = Namespace("http://uma.org/EDAID/bbTrack/#")
    hasHistorial = URIRef(n + "hasHitorial")
    estaEmbarazada = URIRef(n + "estaEmbarazada")
    firstDate = URIRef(n + "firstDate")
    g = Graph()
    pacientes = lista_pacientes()
    for paciente in pacientes:
        ## crea clase paciente
        obj = URIRef(n + paciente.idPaciente)
        nombre = Literal(paciente.Nombre+" "+paciente.Apellidos)
        fecha_nacimiento = Literal(paciente.Fecha_nacimiento)
        ## crease clase historial
        historial = URIRef(n + str(paciente.historial))
        ## crea object property hasHistorial y añade typo, dominio y rango
        g.add((hasHistorial, RDF.type, OWL.ObjectProperty))
        g.add((hasHistorial, RDFS.domain, FOAF.Person))
        g.add((hasHistorial, RDFS.range, FOAF.Historial))
        g.add((obj, RDF.type, FOAF.Person))
        g.add((obj, FOAF.name, nombre))
        g.add((obj, FOAF.fecha_nacimiento, fecha_nacimiento))
        g.add((obj, hasHistorial, historial))
        g.add((historial, RDF.type, FOAF.Historial))
        g.add((historial, firstDate, Literal("hola")))
        ## data prop estaEmbarazada
        g.add((estaEmbarazada, RDF.type, OWL.DataProperty))
        g.add((estaEmbarazada, RDFS.domain, FOAF.Person))
        g.add((estaEmbarazada, RDFS.range, XSD.boolean))
        g.add((obj, estaEmbarazada, Literal(paciente.Embarazada)))
        #selected_historial = get_historial(paciente.historial)
    g.serialize(destination='static/download/bbTrack.rdf', format='xml')
'''