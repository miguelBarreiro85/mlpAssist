
$(document).ready(function(){

    window.row_assistencia = function(){
        console.log("Puta k pariu");
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });




    $("#form_pessoas_novo").click(( event ) => {
        alert( "Handler for .submit() called." );
        event.preventDefault();
      });

     $("#row_assistencia").click((event)=>{
        console.log("haha");
    });

     $("#form_pessoas_procurar").click(( event ) => {
        dados = $("#form_pessoas").serializeArray();
        url = window.location.hostname+":"+window.location.port+"/pesquisa_pessoa";
        $.post("/assistencias/pesquisa_pessoa", dados, (data)=>{
             console.log(JSON.stringify(data));
            $("#DivBody").html("");
                var html = '<table class="table" id="tabela_assistencias"><thead>';
                html += '<th>produto</th>';
                html += '<th>cliente</th>';
                html += '<th>topico</th>';
                html += '<th>descricao</th>';
                html += '<th>valor</th>';
                html += '<th>pago</th>';
                html += "</thead>";
                html += "<tbody>";
                for (i = 0; i < data.length; i++) {
                    html += '<tr>';
                    html += '<td>' + data[i]["produto"] + '</td>';
                    html += '<td >' + data[i]["cliente"] + '</td>';
                    html += '<td>' + data[i]["topico"] + '</td>';
                    html += '<td>' + data[i]["descricao"] + '</td>';
                    html += '<td>' + data[i]["valor"] + '</td>';
                    html += '<td>' + data[i]["pago"] + '</td>';
                    html += "</tr>";
                }
                html += "</tbody>";
                html += "</table>";
                $("#DivBody").append(html);
        });
        event.preventDefault();
      });

});
