/*
Añade ICD10 (existente en la base de datos o bien por busqueda de nuevos terminos) y pruebas a un Informe
 */

idUsuario = localStorage.getItem("idUsuario");;
idInforme = document.URL.split('/').pop()

function hideLoader() {
    $('#loading').hide();
}

$(window).ready(hideLoader);

setTimeout(hideLoader, 20 * 1000);

var get_icd10;
getICD10();

// Añade un codigo ICD10 del correspondiente selectBox
function postICD10() {

	$.ajax({
		method: "POST",
		url: "/api/informes/" + idInforme + "/ICD10",
		dataType: "json",
		contentType: "application/json",
		data:  JSON.stringify({
			"Codigo": $("#selectICD10").val()
		}),
		success: function (data) {
			console.log(data);
			location.href = "../../informe/formulario/" + idInforme;

		},
		error: function(data) {
			alert("Ha habido un error!");

		}
	});

}

// Añade un codigo ICD10 al informe
function postICD10_API(icd10) {

	$.ajax({
		method: "POST",
		url: "/api/informes/" + idInforme + "/ICD10",
		dataType: "json",
		contentType: "application/json",
		data:  JSON.stringify({
			"Codigo": icd10
		}),
		success: function (data) {
			console.log(data);
			location.href = "../../informe/formulario/" + idInforme;

		},
		error: function(data) {
			alert("Ha habido un error!");

		}
	});

}

// Llamada API para añadir un ICD10 a nuestra base de datos
function postICD10_ADD(Codigo, Nombre) {

	$.ajax({
		method: "POST",
		url: "/api/ICD10",
		dataType: "json",
		contentType: "application/json",
		data:  JSON.stringify({ "Codigo": Codigo, "Nombre" : Nombre}),
		success: function (data) {
			console.log(data);
			d = data
			postICD10_API([Codigo]);
		},
		error: function(data) {
			alert("Ha habido un error!" + Codigo);

		}
	});

}

// Llamada API para obtener todos los ICD10
function getICD10() {

	$.ajax({
		method: "GET",
		url: "/api/ICD10",
		dataType: "json",
		contentType: "application/json",
		success: function (data) {
			console.log(data);
			get_icd10 = data
		},
		error: function(data) {
			alert("Ha habido un error!");

		}
	});

}

// Añade ICD10 al informe correspondiente al selecBox
$(document).ready(function() {
    $("#btnAddICD10").click(function(){
		postICD10();
    });
});


// Añade ICD a informe correspondiente a la busqueda
$(document).ready(function() {
    $("#btnAddICD10api").click(function(){

	var suggest_icd10 = [];
	$("#results input:checked").each(function() {
		code = $(this).val();
		var dummy = [];
		var count = 0;
		for(var i in get_icd10){
    		if(get_icd10[i].Codigo == code){
				console.log(get_icd10[i].Nombre)
				dummy.push(code);
				break;
    		}
    		count = count + 1;
		}
		if (get_icd10.length == count){
			for(var j in icd10_api) {
            if (icd10_api[j][0] == code) {
                postICD10_ADD(icd10_api[j][0], icd10_api[j][1])
                break;
            }
        	}
		}else{
			postICD10_API(dummy);
		}
	});
	console.log("ultimo")
    });
});




var icd10_api = [];

// Llamada API para busqueda de termino
function getICD10_API(terms) {

	$.ajax({
		method: "GET",
		url: "https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?sf=code,name&terms=" + terms,
		dataType: "json",
		success: function (data) {
			console.log(data[3]);
			icd10_api = data[3]
			doWork(data[3]);
		},
		error: function(data) {
			alert("Ha habido un error!");

		}
	});

}


// Crea la tabla de la busqueda
function doWork(data){
	all_icd10 = [];
  	if (data.length > 0){

  		$('#results').empty();

        $("#results").append("" +
            "<table class='table table-sm'>" +
            "<thead>" +
            "<tr><th></th><th scope='col'>Codigo</th><th scope='col'>Nombre</th></tr>" +
            "</thead>" +
			"</table>" +
			"<table class='table' id='miTabla'>" +
			"<tbody id='miTablaBody'>"
        );
        for (var i in data) {
        	all_icd10.push(data[i][0]);
            $("#miTablaBody").append("" +
                "<tr><td><input type=\"checkbox\" value = " + data[i][0] +"></td><td><a href=" + ("https://icdcodelookup.com/icd-10/codes/" + data[i][0]) + " target='_blank'>" + data[i][0] + "</a></td><td>" + data[i][1] + "</td></tr>"
            );
        }

        $("#results").after("" +
            "</tbody>" +
            "</table>"
        );
    }
}

$(document).ready(function() {
    $("#btnSugerir").click(function(){
		var terms = $('#inputTerm').val()
		getICD10_API(transform(terms))
    });
});


// Transforma la busqueda con OR y AND
function transform(terms){
	terms = terms.split(" ")
		if (terms.length == 1) {
            console.log(terms);
            return terms;
        }else{
			var index = terms.indexOf("");
			if (index > -1) {
  				terms.splice(index, 1);
			}
    		var result ="";
    		var i = 0;
    		while(i < terms.length){
    			result = result + terms[i];
				if(i < terms.length-1) {
                    result = result + "%20";
                    if (terms[i + 1].toUpperCase() == "AND"){
                        i = i + 1;
                    	result = result + "AND";
                	}else if(terms[i+1].toUpperCase() == "OR") {
                        i = i + 1;
                        result = result + "OR";
                    }else
						result = result + "OR";
					result = result + "%20";
				}
				i = i +1 ;
			}
			console.log(result);
			return result;
		}
}


// Crea una nueva prueba
function postPrueba(prueba) {

	$.ajax({
		method: "POST",
		url: "/api/informes/" + idInforme + "/pruebas",
		dataType: "json",
		contentType: "application/json",
		data:  JSON.stringify({
			"Nombre": prueba.Nombre,
			"Tipo": prueba.Tipo,
			"Observaciones": prueba.Observaciones
		}),
		success: function (data) {
			console.log(data);
			location.href = "../../informe/formulario/" + idInforme;

		},
		error: function(data) {
			alert("Ha habido un error!");

		}
	});

}

// Llamada a postPrueba con los datos y comprobacion de que los datos esten correctos
$(document).ready(function() {
    $("#btnAddPrueba").click(function(){
    	var prueba = {};
    	prueba['Nombre'] = $("#inputNombrePrueba").val()
    	prueba['Tipo'] = $("#selectTipoPrueba").val()
    	prueba['Observaciones'] = $("#inputObservacionesPrueba").val()
		console.log(prueba)
		if (prueba.Nombre == undefined || prueba.Nombre == "")
			alert("Datos incorrectos");
		else if(prueba.Observaciones == undefined || prueba.Observaciones == "")
			alert("Datos incorrectos");
		else if(prueba.Tipo == undefined || prueba.Tipo == "None")
			alert("Datos incorrectos");
		else
			postPrueba(prueba);
    });
});