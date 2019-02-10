/*
Crea diagrama de quesos y busca quien es la prox paciente en dar a luz
 */

// emplea spin mientras carga la pag
window.onload = function(){ document.getElementById("loading-page").style.display = "none" }


function getPacientes() {

	$.ajax({
		method: "GET",
		url: "/api/pacientes",
		dataType: "json",
		success: function (data) {
            get_next_pregnant(data);
		},
		error: function(data) {
			alert("Ha habido un error!");
		},
		complete: function() {
			$("[name=\"loading\"]").hide();
			$("[name='nav-link']").removeClass("disabled");

        }
	});

}

var next_pregnant;
var embarazadas = {};
var age = [];
result = {};
var count;


// Genera grafico de la edad y calcula quien es la prox en dar a luz
function get_next_pregnant(pacientes){
	var today = new Date();
	for(var i in pacientes){
		pacientes[i]['Age'] = _calculateAge(pacientes[i]['Fecha_nacimiento'])
		age.push(pacientes[i]['Age'])
		var fpp = new Date(pacientes[i]['FPP'])
		if(pacientes[i]['Embarazada']=="1" && today<fpp){
			embarazadas[pacientes[i]['idPaciente']] = new Date(pacientes[i]['FPP'])

		}
	}

	// Create items array
	var items = Object.keys(embarazadas).map(function(key) {
	  return [key, embarazadas[key]];
	});

	// Sort the array based on the second element
	items.sort(function(first, second) {
	  return second[1] - first[1];
	});

	id_new_pregnant = items[items.length-1][0];
	for(var i in pacientes){
		if(pacientes[i]['idPaciente']==id_new_pregnant){
			next_pregnant = pacientes[i];
			break;
		}
	}

	var today = new Date();
	var oneDay = 24*60*60*1000; // hours*minutes*seconds*milliseconds
	var diffDays = Math.round(Math.abs((items[items.length-1][1].getTime() - today.getTime())/(oneDay)));

	var full_name = next_pregnant['Nombre'] + " " + next_pregnant['Apellidos'];
	$('#nextPregnant').text(full_name)
	$('#nextPregnantFecha').text("Faltan " + diffDays + " días!")

	var list = age
	// considering ranges `1-4, 5-8, 9-12, 13-16, 17-20, 21-24`
	for (i = Math.min.apply(Math, age); i < Math.max.apply(Math, age); i+= 5) {
	  result[String(i)+"-"+String(i+5)] = (list.filter(function(d){
		return ((i+5 > d) && d >= i);  // check if the number between lower and upper bound
	  }));
	}

	console.log(result);

	count =result;
	for(var i in count){
		count[i] = count[i].length
	}

	TESTER = document.getElementById('ageGraph');

	var data = [{
	  values: Object.values(count),
	  labels: Object.keys(count),
	  type: 'pie'
	}];

	var layout = {
		autosize: true,
	  height: document.getElementById('bodyGraph').offsetHeight*0.9,
	  width: document.getElementById('bodyGraph').offsetWidth*0.9,
		 margin: {
			l: 10,
			r: 10,
			b: 10,
			t: 10,
			pad: 4
		  }
	};

	Plotly.newPlot(TESTER, data, layout);
}

getPacientes()


var update = {
	autosize: true,
  height: document.getElementById('bodyGraph').offsetHeight*0.9,
  width: document.getElementById('bodyGraph').offsetWidth*0.9,
	 margin: {
		l: 10,
		r: 10,
		b: 10,
		t: 10,
		pad: 4
	  }
};

Plotly.relayout('graph', update);



function _calculateAge(birthday) { // birthday is a date
    birthday = new Date(birthday)
	var ageDifMs = Date.now() - birthday.getTime();
    var ageDate = new Date(ageDifMs); // miliseconds from epoch
    return Math.abs(ageDate.getUTCFullYear() - 1970);
}

