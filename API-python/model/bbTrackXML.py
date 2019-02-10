import subprocess
import glob
import os
import sys

def bbTrackXMLjar(arg):
    old_path = os.getcwd()
    print(old_path)
    os.chdir(old_path + "/static/download")
    os.system('rm -rf ' + arg)
    if arg == "bbTrack":
        os.system('rm bbTrack.xml')
    os.system('rm ' + arg + '.zip')
    process = subprocess.call(['java', '-jar', 'bbTrackXML.jar', 'root', 'bbtrack123', arg])
    #process = subprocess.call(['java', '-jar', 'bbTrackXML.jar', 'root', 'secret', arg])
    print(arg)
    style_file = " XSD-XSL/style.css"
    #os.system("rm -rf " + arg)
    if arg == "bbTrack":
        os.system("mkdir " + arg)
        os.system("cp bbTrack.xml " + arg)
        os.system("cp XSD-XSL/XSDGeneral.xsd " + arg)
        os.system("cp XSD-XSL/style.css " + arg)
        os.system("cp XSD-XSL/XSLHome.xsl " + arg)
        os.system("cp XSD-XSL/XSDPaciente.xsd Pacientes")
        os.system("cp XSD-XSL/style.css Pacientes" + arg)
        os.system("cp XSD-XSL/XSLPaciente.xsl Pacientes")
        os.system("cp XSD-XSL/XSDMedico.xsd Medicos")
        os.system("cp XSD-XSL/style.css Medicos" + arg)
        os.system("cp XSD-XSL/XSLMedico.xsl Medicos")
        os.system("mv Pacientes " + arg)
        os.system("mv Medicos " + arg)
        os.system('zip -r ' + arg + '{.zip,}')
    if arg == "Medicos" or arg == "Pacientes":
       # os.system('zip -r ' + arg + '{.zip,}')
       xsd_file = " XSD-XSL/XSD" + arg[:-1] + ".xsd"
       xsl_file = " XSD-XSL/XSL" + arg[:-1] + ".xsl"
       print("cp" + xsd_file + " " + arg)
       os.system("cp" + xsd_file + " " + arg)
       os.system("cp" + xsl_file + " " + arg)
       os.system("cp" + style_file + " " + arg)
       #os.system("zip " + arg + " " + arg + xsd_file + xsl_file + )
       os.system('zip -r ' + arg + '{.zip,}')
    #os.system("rm -rf " + arg)
    os.chdir(old_path)


def bbTrackXMLjar_paciente(idPaciente):
    old_path = os.getcwd()
    print(old_path)
    os.chdir(old_path + "/static/download")
    os.system('rm -rf ' + idPaciente)
    process = subprocess.call(['java', '-jar', 'bbTrackXML.jar', 'root', 'bbtrack123', "Pacientes", idPaciente])
    print(idPaciente)
    style_file = " XSD-XSL/style.css"
    xsd_file = " XSD-XSL/XSDPaciente.xsd"
    xsl_file = " XSD-XSL/XSLPaciente.xsl"
    os.system("mv Paciente " + idPaciente)
    os.system("cp" + xsd_file + " " + idPaciente)
    os.system("cp" + xsl_file + " " + idPaciente)
    os.system("cp" + style_file + " " + idPaciente)
    os.system('zip -r ' + idPaciente + '{.zip,}')
    os.chdir(old_path)
