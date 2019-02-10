/*
Calgula diagrama con los ICD10 y obtiene la tabla topICD10. Tambien crea tabla donde indica posicion
y cantidad del ICD10 buscado
 */

var table_icd10;
var table_icd10_order;

function getICD10s() {

	$.ajax({
		method: "GET",
		url: "/api/ICD10/all",
		dataType: "json",
		success: function (data) {
            graph_icd10(data);
		},
		error: function(data) {
			alert("Ha habido un error!");

		},
		complete: function() {
			$("[name=\"loading\"]").hide()
        }
	});

}

// Diagrama de quesos ICD10
function graph_icd10(icd10s){
	var count;
	count = countElement(icd10s)
	console.log(count.sort);
	var sortable = [];
	for (var icd10 in count) {
		sortable.push([icd10, count[icd10]]);
	}
	prueba= icd10s;
	sortable = sortable.sort(function(a, b) {
    	return a[1] - b[1];
	});

	table_icd10_order = sortable.reverse();
	table_icd10 = count;
	sortable = sortable.slice(0, 3)
	table_top_icd10(sortable)

	TESTER = document.getElementById('icd10Graph');

	var data = [{
	  values: Object.values(count),
	  labels: Object.keys(count),
	  type: 'pie'
	}];

	var layout = {
		autosize: false,
	  height: document.getElementById('icd10Graph').offsetHeight,
	  width: document.getElementById('icd10Graph').offsetWidth
	};

	Plotly.newPlot(TESTER, data, layout);

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


// Tabla top ICD10
function table_top_icd10(topICD10){

	$('#topICD10').empty();

	$("#topICD10").append("" +
		"<thead class=\"thead-dark\">\n" +
        "                    <tr>\n" +
        "                      <th scope=\"col\">#</th>\n" +
        "                      <th scope=\"col\">ICD10</th>\n" +
        "                      <th scope=\"col\">Cantidad</th>\n" +
        "                    </tr>\n" +
        "                  </thead>\n" +
        "                  <tbody>"
	)


	for(var i in topICD10){
        $("#topICD10").append("" +
			"<tr><td>" + (parseInt(i) + 1) + "</td><td>" + topICD10[i][0] + "</td><td>" + topICD10[i][1] + "</td></tr>" +
			"</tbody>" +
			"</table>"
		);
	}

	$("#topICD10").append("</tbody>\n")


}

$("[name=\"loading\"]").show()
getICD10s();



$(document).ready(function() {
    $("#btn1").click(function(){
		var code = $('#search').val()
		doWork(code)
    });
});


// Tabla del ICD10 buscado
function doWork(code){
	var index;
	var position;
	var icd10_keys = Object.keys(table_icd10)
	console.log(icd10_keys)
	index = icd10_keys.indexOf(code)
	console.log(code)

	for(var i in table_icd10_order) {
        if (table_icd10_order[i][0] == code) {
            position = i;
            break;
        }
    }

	if(index == -1){
		alert("No existe dicho ICD10")
	}else{

			$('#searchICD10').empty();

			$("#searchICD10").append("" +
				"<thead class=\"thead-dark\">\n" +
				"                    <tr>\n" +
				"                      <th scope=\"col\">#</th>\n" +
				"                      <th scope=\"col\">ICD10</th>\n" +
				"                      <th scope=\"col\">Cantidad</th>\n" +
				"                    </tr>\n" +
				"                  </thead>\n" +
				"                  <tbody>"
			)

				$("#searchICD10").append("" +
					"<tr><td>" + (parseInt(position) + 1) + "</td><td>" + code + "</td><td>" + table_icd10[icd10_keys[index]] + "</td></tr>" +
					"</tbody>" +
					"</table>"
				);

	}
}




