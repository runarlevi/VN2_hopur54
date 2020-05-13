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

$(function(){
  $(".close").click(function(){
     $("#myAlert").alert('close');
  });
});