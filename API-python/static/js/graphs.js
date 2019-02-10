/*
Obtiene un diagrama de quesos de los ICD de los informes de un paciente
 */

function getICD10(idPaciente) {

	$.ajax({
		method: "GET",
		url: "../../api/pacientes/" + idPaciente + "/informes",
		dataType: "json",
		success: function (data) {
			console.log(data);
			var informes;
			for (var i in data){
				console.log(data[i].ICD10s)
				if(informes == undefined) {
                    informes = data[i].ICD10s;
                }else {
                    informes = informes.concat(data[i].ICD10s)
                }
            }
            console.log(informes)
            doWork(informes);
		},
		error: function(data) {
			alert("Ha habido un error!");

		}
	});

}

function doWork(informes){
	var count;
	count = countElement(informes)

	TESTER = document.getElementById('tester');

	var data = [{
	  values: Object.values(count),
	  labels: Object.keys(count),
	  type: 'pie'
	}];


	var layout = {
	  font: {size: 18}
	};

	Plotly.newPlot(TESTER, data, layout, {responsive: true});

	console.log( Plotly.BUILD );
}


function countElement(array){
	var  count = {};
	console.log(array)
	if(array != undefined)
		array.forEach(function(i) { count[i] = (count[i]||0) + 1;});
	console.log(count)
	return count;
}


getICD10(document.URL.split('/')[5])








