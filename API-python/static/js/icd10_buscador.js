/*
Buscador de términos de ICD10
 */

var all_icd10 = [];

// Llamada API para el buscador
function getICD10_API(terms) {

	$.ajax({
		method: "GET",
		url: "https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?sf=code,name&terms=" + terms,
		dataType: "json",
		success: function (data) {
			console.log(data[3]);
			d = data[3]
			doWork(data[3]);
		},
		error: function(data) {
			alert("Ha habido un error!");

		}
	});

}

function getICD10() {

	$.ajax({
		method: "GET",
		url: "/api/informes",
		dataType: "json",
		success: function (data) {
			console.log("Aquiiii");
			console.log(data);
			var prueba = {};
			for (var i in data){
				console.log(data[i]);
				console.log(data[i].ICD10s);
				var dummy = data[i].ICD10s.concat(prueba[data[i].idHistorial.split("-")[1]])
				prueba[data[i].idHistorial.split("-")[1]] = dummy;
            }
            console.log(prueba)
			console.log(Object.keys(prueba))
            doWork2(prueba);
		},
		error: function(data) {
			alert("Ha habido un error!");

		}
	});

}

// Crea tabla del resultado de la llamada
function doWork(data){
	all_icd10 = [];
  	if (data.length > 0){

  		$('#results').empty();

        $("#results").append("" +
			"<div class=\"row\">" +
				"<div class='col-md-6'>" +
					"<h1>Resultados</h1>" +
				"</div>" +
				"<div class='col-md-6'>" +
					"<button type=\"button\" class=\"btn\" id=\"btn2\">Buscar en mis pacientes</button>\n" +
				"</div>" +
			"</div>" +
			"<div class=\"row\">" +
				"<table class='table'>" +
					"<thead class='thead-dark'>" +
					"<tr><th scope='col'>Codigo</th><th scope='col'>Nombre</th></tr>" +
					"</thead>" +
					"<tbody class=\"thead-light\" id='resultsBody'>" +
					"</tbody>" +
				"</table>" +
			"</div>"
        );
        for (var i in data) {
        	all_icd10.push(data[i][0]);
            $("#resultsBody").append("" +
                "<tr><td><a href=" + ("https://icdcodelookup.com/icd-10/codes/" + data[i][0]) +" target='_blank'>" + data[i][0] + "</a></td><td>" + data[i][1] + "</td></tr>"
            );
        }
		$(document).ready(function() {
			$("#btn2").click(function(){
				getICD10()
			});
		});

    }
}

// Busca los pacientes con algun ICD10 de la busqueda anterior
function doWork2(data){
  	result_icd10 = []
  	result_paciente = []
	for(var i in data){
  		for(var j in data[i]){
  			if(all_icd10.includes(data[i][j])) {
            	result_icd10.push(data[i][j])
				console.log("llego")
            	result_paciente.push(i)
        	}
		}
	}
	if (result_paciente.length > 0){
  		$('#results2').empty();

        $("#results2").append("" +
            "<h1 class='text-center'>Resultados Paciente</h1>" +
            "<table class='table' id='miTabla2'>" +
            "<thead class='thead-dark'>" +
            "<tr><th scope='col'>Paciente</th><th scope='col'>Codigo</th></tr>" +
            "</thead>" +
            "<tbody class=\"thead-light\" id='resultsBody2'>"+
            "</tbody>" +
            "</table>"
        );

        $('#resultsBody2').empty();

        for (var i in result_paciente) {
            $("#resultsBody2").append("" +
                "<tr><td>" + result_paciente[i] + "</td><td><a href=" + ("https://icdcodelookup.com/icd-10/codes/" + result_icd10[i]) + " target='_blank'>" + result_icd10[i] + "</td></tr>"
            );
        }

    }
}

$(document).ready(function() {
    $("#btn1").click(function(){
		var terms = $('#search').val()
		getICD10_API(transform(terms))
    });
});

$(document).ready(function() {
    $("#btn2").click(function(){
		getICD10()
    });
});


// transforma los terminos
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