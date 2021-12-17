$(function () {
    
    $('#finish').hide();
    var starRating = 0;
   
    $('.photo span').on('mouseenter', function () {
        var index = $(this).index() + 1;
        $(this).prevAll().find('.high').css('z-index', 1);
        $(this).find('.high').css('z-index', 1);
        $(this).nextAll().find('.high').css('z-index', 0);
        $('.starNum').html((index * 2).toFixed(1) + '分');
    });
   
    $('.photo').on('mouseleave', function () {
        $(this).find('.high').css('z-index', 0);
        var count = starRating / 2;
        console.log(count);
        if (count == 5) {
            $('.photo span').find('.high').css('z-index', 1);
        } else {
            $('.photo span').eq(count).prevAll().find('.high').css('z-index', 1);
        }
        $('.starNum').html(starRating.toFixed(1) + '分')
    }),
        
        $('.photo span').on('click', function () {
            var index = $(this).index() + 1;
            $(this).prevAll().find('.high').css('z-index', 1)
            $(this).find('.high').css('z-index', 1);
            starRating = index * 2;
            $('.starNum').html(starRating.toFixed(1) + '分');
            
        });
   
        $('.cancleStar').on('click',function () {
            starRating = 0;
            $('.photo span').find('.high').css('z-index',0);
            $('.starNum').html(starRating.toFixed(1)+'分');
        });

        $('.sureStar').on('click',function () {
            if(starRating===0) {
                alert('最低一颗星！');
            } else {
                var pagid;
           pagid = $(this).attr('data-catid');
           $.get('/datamining/score/', 
                 {'page_id': pagid,
                  'score':starRating.toFixed(1)
                },
                 function(data) {
                 $('#score_count').html(data);
                 $('#score').hide();
                 $('#hi').hide();
                 $('#finish').show();
               })
            $.get('/datamining/score1/', 
                 {'page_id': pagid,
                },
                 function(data) {
                 $('#num_count').html(data);
               })
            }
        })
})
