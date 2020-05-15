$(document).ready(function() {
    $('#search-box').keypress(function(e) {
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

$(function(){
  $(".close").click(function(){
     $("#myAlert").alert('close');
  });
});


/*
    Carousel
*/
$('#carousel-example').on('slide.bs.carousel', function (e) {
    /*
        CC 2.0 License Iatek LLC 2018 - Attribution required
    */
    var $e = $(e.relatedTarget);
    var idx = $e.index();
    var itemsPerSlide = 5;
    var totalItems = $('.carousel-item').length;

    if (idx >= totalItems-(itemsPerSlide-1)) {
        var it = itemsPerSlide - (totalItems - idx);
        for (var i=0; i<it; i++) {
            // append slides to end
            if (e.direction==="left") {
                $('.carousel-item').eq(i).appendTo('.carousel-inner');
            }
            else {
                $('.carousel-item').eq(0).appendTo('.carousel-inner');
            }
        }
    }
});