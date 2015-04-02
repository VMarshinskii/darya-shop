$(document).ready(function(){
    var path = $(".file-upload").children("a").attr("href");
    $(".file-upload").children("a").attr("href", '/' + path);
    $(".file-upload").children("a").html('<img width="260px" class="adminImageField" src="/' + path + '"/>');
    var content = $(".file-upload").html().replace("На данный момент: ", '');
    $(".file-upload").html(content);

    var order_str = $("#id_products").val();
    alert(order_list(order_str));
});


//fvpe8pai.jpg;Пальто Green Frash зеленое;1140;4;4560;1

var order_list = function(order_str){
    var result = "<table>";
    var products = order_str.split("==");
    for (var i = 1; i < products.length -1; i++){
        if(products[i] !== '') {
            var product = products[i].split(";");
            result += '<tr>';
            result += '<td><img width="50" src="' + product[0] + '"/></td>';
            result += '<td><a href="/catalog/product/' + product[5] + '">' + product[1] + '<a/></td>';
            result += '<td>' + product[2] + '</td>';
            result += '<td>' + product[3] + '</td>';
            result += '<td>' + product[4] + '</td>';
            result += '</tr>';
        }
    }
    result += '</tr>';
    return result;
};