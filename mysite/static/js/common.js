/**
 * Created by Vladislav on 06.01.2015.
 */

function resize() {
    /*if($(document).width() > 1700) {
        $("#all-content").css({"width":"1600px"});
        $(".header-info .header-info-one").css({"width":"585px"});
    }*/
    if($(document).width() > 1340) {
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
        mousewheel:false,
        shownavitems:5,
        panelfx:"sliding",
        panelfxspeed:2000,
        panelfxeasing:"easeOutExpo" // "easeOutExpo", "easeInOutExpo", etc.
    });
});

$(".CartAdd").live('click', function(){
    var id = $(this).attr("data-id");
    $(".ContentBoxPage").load("/cart/add_in_cart/" + id + "/?cart=1");
    setTimeout(function f() {
        $(".cart").load("/cart/cart_top_ajax/");
    }, 500);
});
$(".CartDelete").live('click', function(){
    var id = $(this).attr("data-id");
    $(".ContentBoxPage").load("/cart/del_in_cart/" + id + "/");
    $(".cart").load("/cart/cart_top_ajax/");
});
$(".CartItemDelete").live('click', function(){
    var id = $(this).attr("data-id");
    $(".ContentBoxPage").load("/cart/remove_in_cart/" + id + "/");
    setTimeout(function f() {
        $(".cart").load("/cart/cart_top_ajax/");
    }, 500);
});

$(document).ready(function (){
    $(".good-c a").click(function(){
        var id = $(this).attr("data-id");
        $.get("/cart/add_in_cart/" + id + "/", function(data){
            $(".popupBox").html(data);
            $(".background").css('display', 'block');
            $(".popupBox").css('display', 'block');
        });
        setTimeout(function f() {
            $(".cart").load("/cart/cart_top_ajax/");
        }, 500);
        return false;
    });

    $(".CatalogPriceBox a").click(function(){
        var id = $(this).attr("data-id");
        $.get("/cart/add_in_cart/" + id + "/", function(data){
            $(".popupBox").html(data);
            $(".background").css('display', 'block');
            $(".popupBox").css('display', 'block');
        });
        setTimeout(function f() {
            $(".cart").load("/cart/cart_top_ajax/");
        }, 500);
        return false;
    });

    $(".cart").load("/cart/cart_top_ajax/");
//    $(".OrderBoxAddressAdd").hide();

    $(".popupBoxLoginFormClose").live('click', function(){
        $(".background").css('display', 'none');
        $(".popupBox").css('display', 'none');
    });

    $(".popup_img_box_close").live('click', function(){
        $(".background").css('display', 'none');
        $(".popupBox").css('display', 'none');
    });

    $('.background').hover(
    function(){
        $(".popup_img_box_close").css('opacity', '1');
    },
    function(){
        $(".popup_img_box_close").css('opacity', '0.3');
    });

    $(".background").click(function(){
        $(".background").css('display', 'none');
        $(".popupBox").attr("style", "display: none");
        $(".popupBox").html("");
    });

    $(".login_order").live('click', function(){
        $.get("/login/", function(data){
            $(".popupBox").html(data);
            $(".background").css('display', 'block');
            $(".popupBox").css('display', 'block');
            $("#id_login").mask("+7 (999) 999-9999");
        });
        return false;
    });

    $(".loginSubmit").live('click', function(){
        var link = $(".login_order").attr("data-link");
        $.post("/login/",
            {
                login: $("#id_login").val(),
                password: $("#id_password").val(),
                csrfmiddlewaretoken: $(".popupBox input[name='csrfmiddlewaretoken']").val()
            },
            function(data){
                if(data == "true")
                {
                    if(link == undefined)
                    {
                        window.location.replace("http://85.143.216.11/user/orders/");
                        window.location.href = "http://85.143.216.11/user/orders/";
                    }
                    else
                    {
                        window.location.replace(link);
                        window.location.href = link;
                    }
                }
        });
        return false;
    });

    $("#id_phone").mask("+7 (999) 999-9999");
    $("#id_login").mask("+7 (999) 999-9999");

    $("#id_type_delivery").live('click', function(){
        var price = $(this).attr('data-price');
        $("#OrderBoxConfirmationPriceCurrent span").html(price);
        var price_all = parseInt($("#OrderBoxConfirmationPriceSum span").html(), 10) + parseInt(price, 10);
        $("#OrderBoxConfirmationPriceAll span").html(price_all);
    });


    $(".video_file").each(function(indx, element){
        $(element).append("<span></span>");
        var left = $(element).children("img").position().left + (($(element).children("img").width() - 64) / 2);
        var top = $(element).children("img").position().top + (($(element).children("img").height() - 64) / 2);
        $(element).children("span").css({'top': top, 'left': left});
    });

    $(".video_file").click(function(){
        var url = 'http://85.143.216.11' + $(this).attr("href");
        var str = '<div class="player" id="videoplayer"></div><script type="text/javascript">this.player = new Uppod({m:"video",uid:"videoplayer",file:"'+ url +'",poster:"'+ url +'"});</script>'
        $(".popupBox").html(str);
        $(".background").css('display', 'block');
        $(".popupBox").css('display', 'block');
        $(".popupBox").css({'width':'500px', 'height': '375px', 'margin-left': '-250px', 'margin-top': '-171px', 'padding': '0'});
        return false;
    });


    $(".galeryBoxImg").click(function(){

        var doc_w = $(window).width();
        var doc_h = $(window).height();

        var width = doc_w / 100 * 60;
        var height = doc_h / 100 * 70;

        $(".popupBox").html('<div class="popup_img_box">' + $(this).html() + '</div>');
        $(".background").html('<span class="popup_img_box_close"></span>');
        $(".background").css('display', 'block');
        $(".popupBox").css({'display':'block', 'width': width, 'height': height, 'margin-top': -(height / 2), 'margin-left': -(width / 2), 'box-shadow': 'none', 'background': 'none'});
    });

    $(".goods-img img").each(function(index, element){
        if ($(element).width() > $(element).height())
        {
            alert($(element).width() + " : " + $(element).height());
            $(element).css({'width': 'auto', 'height': '100%'});
        }
    });

});