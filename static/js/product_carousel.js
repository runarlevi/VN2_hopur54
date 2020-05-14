$(window).load(function() {
    $(".carousel .item").each(function() {
        let i = $(this).next();
        i.length || (i = $(this).siblings(":first"));
          i.children(":first-child").clone().appendTo($(this));

        for (let n = 0; n < 4; n++)(i = i.next()).length ||
          (i = $(this).siblings(":first"));
          i.children(":first-child").clone().appendTo($(this))
    })
});