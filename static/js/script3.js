
$(document).on('mouseover','.basket-container',function(){
    $('.basket-items').removeClass('hidden');
});
$(document).on('mouseout','.basket-items',function(){
    $('.basket-items').addClass('hidden');
});



//$(document).ready(function(){
////        function showingBasket(){                       //вводим функцию showingBasket() котороая будет отвечать за отображенияокошкаа всплывающего окошка корзины
////        $('.basket-items').removeClass('hidden');   //$('.basket-items')-обращаемся к элементу(в navbar.html) с классом basket-items как к элементу jqery,removeClass('hidden')-означает что если  класса hidden есть он его удалает
////    };
//    $('.basket-container').mouseover(function(){   //что будет вывполняться с этим элементо(в navbar.html) при наведении мышью(элемент с классом basket-container-корзинана навбаре)
//      $('.basket-items').removeClass('hidden');
//    });
//
//    $('.basket-items').mouseout(function(){  //что будет вывполняться с этим элементо при не наведении мышью(элемент с классом basket-container-корзинана навбаре)
//      /// showingBasket();  ////вывзо функции описанрой выше
//       $('.basket-items').addClass('hidden');    //$('.basket-items')-обращаемся к элементу с классом basket-items как к элементу jqery,addClass('hidden')-означает что добовляет класс hidden(видимость)если его нет
//     });
//});

//    $('.basket-items').hide();
////     $('.basket-container').hover(function(){
////         $('.basket-items').show();
//////     },function(){
//////             $('.basket-items').hide();
////         }
////     );
//    $('.basket-container').mouseover(function(){
//         $(this).show();
//     });
//    $('.basket-items').mouseover(function(){
//         $(this).show();
//     });

//      $('.basket-items').mouseout(function(){
//
//
//             $('.basket-items').show(1000);


//      });
//    $('.basket-items').mouseout(function(){
//
//             $(this).hide(1000);
//
//
////      });
//     });

