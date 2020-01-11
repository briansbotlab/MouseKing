$("#id_keyword").bind('input propertychange', function() {
      var keyword = $(this).val();

      $.ajax({
        url: '/index/search/',
        data: {
          'keyword': keyword
        },
        type: 'GET',
        dataType: 'json',
        success: function (data) {
          $("#mouses").html("<thead><tr><th>UID</th><th>Currency</th></tr></thead><tbody>")

          if (data == ''){
            $("#mouses").append("<tr><td colspan="+'2'+" class="+'text-center bg-warning'+">No Data.</td></tr>");
          }else{
            $.each(data,function(index,item){
                       $("#mouses").append(
                        "<tr><td>" + item.pk + "</td>" +
                            "<td>" + item.fields.currency + "</td></tr>"
                       );
                    })
          }
          $("#mouses").append("</tbody>");


        },
        error:function(xhr){
          alert("發生錯誤: " + xhr.status + " " + xhr.statusText);
        }
      });
    });
