$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
       e.preventDefault();
       var searchText = $('#search-box').val();
       $.ajax({
           url: '/products?search_filter=' + searchText,
           type: 'GET',
           success: function (resp) {
               var newHtml = resp.data.map(d => {
                   return `<div class="product">
                                <a href="/products/${d.id}">
                                    <img class="product-img" src="${d.firstImage}">
                                    <h4>${d.name}</h4>
                                    <h4>${d.price}$</h4>
                                </a>
                            </div>`
               });
               $('.products').html(newHtml.join(''));
               $('#search-box').val('');
           },
           error: function (xhr, status, error) {
                console.error(error);
           }
       });
    });
});

$(document).ready(function() {
    $("#myfilter").change(function(e){
        e.preventDefault();
        console.log($("#myfilter").val());
        $.ajax({
            url: '/products?sort_filter=' + $("#myfilter").val(),
            type: 'GET',
            success: function (resp) {
                console.log(resp);
                var newHtml = resp.bla.map(d => {
                    return `<div class="product">
                                <a href="/products/${d.id}">
                                    <img class="product-img" src="${d.firstImage}">
                                    <h4>${d.name}</h4>
                                    <h4>${d.price}$</h4>
                                </a>
                            </div>`
                });
                $('.products').html(newHtml.join(''));
            },
            error: function (xhr, status, error) {
            console.error(error);
            }
        });
    });
});

$(function(){
  $(".close").click(function(){
     $("#myAlert").alert('close');
  });
});

$.ajax({
type: "GET",
dataType: "json",
url:"/products",
success: function(data)
{
    alert("i got data now i will parse it as i want to display it");
},

});

