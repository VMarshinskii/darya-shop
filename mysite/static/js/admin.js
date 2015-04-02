var order_list = function(order_str){
    var result = '<table class="admin_order_list">';
    result += '<tr>';
    result += '<td width="56"></td>';
    result += '<td>Название</td>';
    result += '<td>Цена</td>';
    result += '<td>Кол-во.</td>';
    result += '<td>Сумма</td>';
    result += '</tr>';
    var products = order_str.split("==");
    for (var i = 0; i < products.length -1; i++){
        if(products[i] !== '') {
            var product = products[i].split(";");
            result += '<tr>';
            result += '<td><div class="admin_table_img"><img width="50" src="/static/uploads/' + product[0] + '"/></div></td>';
            result += '<td><a href="/catalog/product/' + product[5] + '">' + product[1] + '<a/></td>';
            result += '<td align="center">' + product[2] + '</td>';
            result += '<td align="center">' + product[3] + '</td>';
            result += '<td align="center">' + product[4] + '</td>';
            result += '</tr>';
        }
    }
    result += '</tr>';
    return result;
};

$(document).ready(function(){
    var path = $(".file-upload").children("a").attr("href");
    if(path){
        $(".file-upload").children("a").attr("href", '/' + path);
        $(".file-upload").children("a").html('<img width="260px" class="adminImageField" src="/' + path + '"/>');
        var content = $(".file-upload").html().replace("На данный момент: ", '');
        $(".file-upload").html(content);
    }
});


$(document).ready(function(){
    var order_str = $("#id_products").val();
    $("#id_products").after(order_list(order_str));
    $("#id_products").remove();
});
