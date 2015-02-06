$(document).ready(function(){
    var path = $(".file-upload").children("a").attr("href");
    $(".file-upload").children("a").attr("href", '/' + path);
    $(".file-upload").children("a").html('<img width="140px" style="margin:10px 0 10px 0" src="/' + path + '"');
});