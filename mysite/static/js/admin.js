$(document).ready(function(){
    var path = $(".file-upload").children("a").attr("href");
    $(".file-upload").children("a").attr("href", '/' + path);
    $(".file-upload").children("a").html('fsdgfsdfgsdfgsdfgsd');
});