/*
Calgula diagrama con los ICD agrupandolos y obtiene la tabla topICD10. Tambien crea tabla donde indica posicion
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
            graph_icd10_group(data);
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

function countElement(array){
	var  count = {};
	console.log(array)
	if(array != undefined)
		array.forEach(function(i) { count[i] = (count[i]||0) + 1;});
	console.log(count)
	return count;
}

// Diagrama de quesos ICD10
function graph_icd10_group(icd10s){
	var count = {};
	var icd10s_group = [];
	for(var i in icd10s){
		icd10s_group.push(icd10s[i].split(".")[0])
	}
	count = countElement(icd10s_group)
	console.log(count.sort);
	var sortable = [];
	for (var icd10 in count) {
		sortable.push([icd10, count[icd10]]);
	}
	sortable = sortable.sort(function(a, b) {
    	return a[1] - b[1];
	});

	table_icd10_order = sortable.reverse();
	table_icd10 = count;
	sortable = sortable.slice(0, 3)
	table_top_icd10_group(sortable)

	TESTER = document.getElementById('icd10Graph2');

	var data = [{
	  values: Object.values(count),
	  labels: Object.keys(count),
	  type: 'pie'
	}];

	var layout = {
		autosize: false,
	  height: document.getElementById('icd10Graph2').offsetHeight,
	  width: document.getElementById('icd10Graph2').offsetWidth
	};

	Plotly.newPlot(TESTER, data, layout);

	console.log( Plotly.BUILD );
}

// Tabla top ICD10
function table_top_icd10_group(topICD10){

	$('#topICD102').empty();

	$("#topICD102").append("" +
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
        $("#topICD102").append("" +
			"<tr><td>" + (parseInt(i) + 1) + "</td><td>" + topICD10[i][0] + "</td><td>" + topICD10[i][1] + "</td></tr>" +
			"</tbody>" +
			"</table>"
		);
	}

	$("#topICD102").append("</tbody>\n")


}

$("[name='nav-link']").addClass("disabled");
$("[name=\"loading\"]").show();
//document.getElementsByName("loading") .className = "loading-visible";
getICD10s();


$(document).ready(function() {
    $("#btn1").click(function(){
		var code = $('#search').val()
		doWork(code)
    });
});

// Tabla ICD10 buscado
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

