/*
Post de un informe nuevo
 */

idUsuario = localStorage.getItem("idUsuario");;
$("#inputIdMedico" ).val(idUsuario)
$("#inputIdMedico").prop("readonly", true);

$("#inputFechaConsulta" ).val(new Date().toJSON().slice(0,10).substr(2))
$("#inputFechaConsulta").prop("readonly", true);

var utc = new Date().toJSON().slice(0,10)

var paciente_;
var informe_;

// Get que permite rellenar los campos del formulario
function getPaciente(idPaciente) {

	$.ajax({
		method: "GET",
		url: "../../api/pacientes/" + idPaciente,
		dataType: "json",
		success: function (data) {
			paciente_ = data
			console.log(data);
			doWork(data)
		},
		error: function(data) {
			alert("Ha habido un error!");

		}
	});

}

//Creacion de un nuevo informe
function postInforme(idPaciente) {

	$.ajax({
		method: "POST",
		url: "../../api/pacientes/" + idPaciente + "/informes",
		dataType: "json",
		contentType: "application/json",
		data:  JSON.stringify({
			"Estado_paciente": $("#selectEstado").val(),
			"Diagnostico": $("#textDiagnostico").val(),
			"Fecha_consulta": $("#inputFechaConsulta").val(),
			"idConsulta": $("#selectIdConsulta ").val(),
			"Licencia_medico" : $("#inputIdMedico").val()
		}),
		success: function (data) {
			console.log(data);
			informe_ = data;
			if (data.idInforme != undefined) {
                alert("Informe subido correctamente" + data.idInforme)
                location.href = "/html/informe/formulario/" + data.idInforme;
            }
		},
		error: function(data) {
			alert("Ha habido un error!");

		}
	});

}

// Funcion para rellenar los campos
function doWork(paciente){
	$("#inputNombre" ).val(paciente["Nombre"] + " " + paciente["Apellidos"])
	$("#inputNombre").prop("readonly", true);
	$("#inputIdHistorial" ).val("H-" + paciente["idPaciente"])
	$("#inputIdHistorial").prop("readonly", true);
}

$(document).ready(function() {
    $("#btnRellenar").click(function(){
		getPaciente($("#selectIdPaciente option:selected" ).text())
    });
});

$(document).ready(function() {
    $("#btnSubmit").click(function(){
    	if($("#selectIdConsulta ").val()=="None")
    		alert("Por favor, elija la consulta")
		else
			postInforme(paciente_["idPaciente"])
    });
});
