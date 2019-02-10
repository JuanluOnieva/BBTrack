/*
Permite descargarnos las bases de datos
 */


function runbbTrackXML(argument) {
    $.ajax({
      type: "POST",
        url: "../computeXML/" + argument ,
		  complete: function() {

          var win = window.open('/downloadXML/' + argument, '_blank');
            if (win) {
                //Browser has allowed it to be opened
                win.focus();
            } else {
                //Browser has blocked it
                alert('Please allow popups for this website');
            }

       }
    })

}

function runbbTrackRDF() {
    $.ajax({
      type: "POST",
        url: "/computeRDF" ,
		  complete: function() {

          var win = window.open('/downloadRDF', '_blank');
            if (win) {
                //Browser has allowed it to be opened
                win.focus();
            } else {
                //Browser has blocked it
                alert('Please allow popups for this website');
            }

       }
    })

}



$(document).ready(function() {
    $("#btnDownload").click(function(){
        console.log("llego")
		runbbTrackXML("bbTrack")
    });
});


$(document).ready(function() {
    $("#btnDownload2").click(function(){
        console.log("llego")
		runbbTrackXML("Medicos")
    });
});

$(document).ready(function() {
    $("#btnDownload3").click(function(){
        console.log("llego")
		runbbTrackXML("Pacientes")
    });
});

$(document).ready(function() {
    $("#btnDownloadRDF").click(function(){
        console.log("llego")
		runbbTrackRDF()
    });
});
