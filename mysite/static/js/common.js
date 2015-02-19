/**
 * Created by Vladislav on 06.01.2015.
 */

function resize() {
    /*if($(document).width() > 1700) {
        $("#all-content").css({"width":"1600px"});
        $(".header-info .header-info-one").css({"width":"585px"});
    }*/
    if($(document).width() > 1320) {
        $("#all-content").css({"width":"1285px"});
        $(".all-content").css({"width":"1285px"});
        $(".header-info .header-info-one").css({"width":"585px"});
        $("#center-block").css({"width":"700px"});
        $(".main-slider img").css({"width":"683px"});
        $(".main-slider").css({"height":"auto"});
        $(".photoslider-bullets").css({"height":"443px"});

        resize_goods(3, 192);
    }
    else {
        $("#all-content").css({"width": "1000px"});
        $(".all-content").css({"width": "1000px"});
        $(".header-info .header-info-one").css({"width":"400px"});
        $("#center-block").css({"width":"395px"});
        $(".main-slider img").css({"width":"375px"});
        $(".main-slider").css({"height":"244px"});
        $(".photoslider-bullets").css({"height":"244px"});

        resize_goods(2 ,159);
    }
}
function resize_goods(number, width) {
    //number -= ;
    var index = 1;

    $(".goodss .good").removeClass("mar0");
    $(".goodss .good").width(width);

    $(".goodss .good").each(function () {
        if(index%number == 0) {
            $(this).addClass("mar0");
        }
        index++;
    });

    //width: 192px;
    /*width: 159px;*/
}

$(document).ready(function (){
    resize();
});
$(window).resize(function(){
    resize();
});
jQuery(window).load(function(){
    jQuery(".photoslider-bullets").sliderkit({
        auto:true,
        circular:true,
        mousewheel:true,
        shownavitems:5,
        panelfx:"sliding",
        panelfxspeed:2000,
        panelfxeasing:"easeOutExpo" // "easeOutExpo", "easeInOutExpo", etc.
    });
});

$(".CartAdd").live('click', function(){
    var id = $(this).attr("data-id");
    $(".ContentBoxPage").load("/cart/add_in_cart/" + id + "/?cart=1");
});
$(".CartDelete").live('click', function(){
    var id = $(this).attr("data-id");
    $(".ContentBoxPage").load("/cart/del_in_cart/" + id + "/");
});
$(".CartItemDelete").live('click', function(){
    var id = $(this).attr("data-id");
    $(".ContentBoxPage").load("/cart/remove_in_cart/" + id + "/");
});

$(document).ready(function (){
    $(".good-c a").click(function(){
        var id = $(this).attr("data-id");
        $.get("/cart/add_in_cart/" + id + "/");
        alert("Товар в корзине");
        return false;
    });
});