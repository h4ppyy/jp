function move(url){
  window.location.href = url;
}

function post_save(){
  var id_title = $('#id_title').val();
  var id_content = $('#id_content').val();
  id_content = id_content.replace(/\r?\n/g, '<br/>');

  $.post( "/regist", {
     csrfmiddlewaretoken: $('#csrf_token').val(),
     title: id_title,
     content: id_content
   })
  .done(function( data ) {
    if (data.result == 200) {
      window.location.href = '/';
    } else {
      alert('error');
    }
  });
}

function post_delete(){
  var post_id = $('#post_id').val();

  $.post( "/delete", {
     csrfmiddlewaretoken: $('#csrf_token').val(),
     post_id: post_id
   })
  .done(function( data ) {
    if (data.result == 200) {
      window.location.href = '/';
    } else {
      alert('error');
    }
  });
}
