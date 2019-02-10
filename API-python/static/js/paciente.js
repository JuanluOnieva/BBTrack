/*
Permite descargarnos las bases de datos del paciente en concreto
 */


function runbbTrackXML(idPaciente) {

    $.ajax({
      type: "POST",
        url: "/computeXML/paciente/" + idPaciente ,
		  complete: function() {

          var win = window.open('/downloadXML/paciente/' + idPaciente, '_blank');
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
    $("#btnDonwloadXML").click(function(){
        var idPaciente = document.location.pathname.split("/")[3];
        console.log(idPaciente);
		runbbTrackXML(idPaciente)
    });
});

