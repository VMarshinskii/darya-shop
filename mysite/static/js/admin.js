$(document).ready(function(){
    alert("ok");
    var path = $(".file-upload").children("a").attr("href");
    $(".file-upload").children("a").attr("href", '/' + path);
    $(".file-upload").children("a").html('<img width="260px" class="adminImageField" src="/' + path + '"/>');
    var content = $(".file-upload").html().replace("На данный момент: ", '');
    $(".file-upload").html(content);
});