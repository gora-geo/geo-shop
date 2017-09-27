$(document).ready(function(){                // стандартная обертка jqery которая говорит о том что даннный код будетвыполняться после токго как загрузиться весь html-документ
    var form = $('#form_buying_product');     //мы хотим обратиться к форме поэтому вводим переменную form знак долара означает что мы хотим обратиться к элементу как к элементу jqery,form_buying_product-это id формы в product.html #-означает что мы хотим  выбрать элемент по id
    console.log(form);                      //мы выводим переммменю в console(в браузере надо нажать иследовать элемент там будет console)
    form.on('submit', function(e){        //(ниже будет описываться что будет поисходить при нажати кнопки купить которая имеет тип submit)--тоесть мы к форме должны подключить событие у формы это submit добовляем переменную е
        e.preventDefault();                  // e.preventDefault();-фция чтобы форма не обновлялась а то сторока ниже не выведиться
        console.log('123');           //выводим в console строчку 123
        var nmb = $('#number').val();   //добовляем перемнную nmb $('#number')-вызываем элемент с id=number(элемент-jqery) .val-для получения значения элементов формы
        console.log(nmb);                //выводим в консоль переменной nmb
        var submit_btn = $('#submit_btn');   //вводим переменную submit_btn это будет элемент у которого  id=submit_btn
        var product_id =  submit_btn.data("product_id");   //вводим перемменую product_id которая равна data атрибуту product_id
        var name = submit_btn.data("name");  //вводим перемменую name которая равна data атрибуту name
        var price = submit_btn.data("price");  //вводим перемменую price которая равна data атрибуту price
        console.log(product_id);       //выводим в консоль переменную product_id
        console.log(name);              //выводим в консоль переменную name
        console.log(price);              //выводим в консоль переменную price

        var data = {};    //вводим перемееню(пустой список(или словарь) куда будем отправлять id продукта ,которое добовляет в карзину его количество
        data.product_id = product_id; //записывем с писок data переменую product_id под полкой product_id
        data.nmb = nmb;               //записывем с писок nmb переменую product_id под полкой nmb
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();   //считывет токен с формы form_buying_product(product.html)
        data["csrfmiddlewaretoken"] = csrf_token;  //записыввем в переменную список data под индексом именем

        var url = form.attr("action");   //адрес куда необходимо отрправить пост запрос,это это значениеатрибута формыы  action
        console.log(data);
        $.ajax({                  //обозначени что от сюда идет код ajax
                url: url,         //здесь сипользуеться url который описан 2 строки выше
                type: 'POST',     //используеться тип запроса-запрос с пост обработкой
                data: data,       //используеться data фаил описанный выше
                cache: true,      //используеться кеширование - true(истина) (кэширование некий буфер где храняться данные  для ускоренногоработы  с ним)
                success: function (data) {   // success-это функция которая вызываеться если успешно получен ответ с сервера
                 console.log("OK");         //выводим ок в консоль
                 console.log(data.products_total_nmb);  //выводим в консоль присланое из django(смотри order/views.py)значение products_total_nmb
                 if (data.products_total_nmb){   //условие если она существует
                    $('#basket_total_nmb').text("("+data.products_total_nmb+")"); //в элемент с id=basket_total_nmb(navbar.html)-будем записывать переданное значение
                 }
                 },
                error: function(){        //error-эта функция вызываеться если ответ с сервера получен не успешно
                 console.log("error")     //выводим в консоль error
                }
        })
//
        $('.basket-items ul').append('<li>'+ name+', ' + nmb + 'шт. ' + 'по ' + price + 'руб  ' +
                             '<a class="delete-item" href="" >x</a>' +       //появиться крестик ввиде сылки с классом delete-item
                            '</li>');
        //(то что будет выводиться в ячейку корзины при нажати купить)
        // $('.basket-items ul').-тоеть делаем элемент с классом basket-items элементом jqery(div в navbare) ul(означает что на уровень ниже есть элемент(тоесть в ul входяший div)
        // ul (в элемент с классом basket-items входит элемент ul),append('<li>---</li>')-и добовляем в строку (добавить в ul)---

    });
    function showingBasket(){                       //вводим функцию showingBasket() котороая будет отвечать за отображенияокошкаа всплывающего окошка корзины
        $('.basket-items').removeClass('hidden');   //$('.basket-items')-обращаемся к элементу(в navbar.html) с классом basket-items как к элементу jqery,removeClass('hidden')-означает что если  класса hidden есть он его удалает
    };
    $('.basket-container').mouseover(function(){   //что будет вывполняться с этим элементо(в navbar.html) при наведении мышью(элемент с классом basket-container-корзинана навбаре)
       showingBasket();   //вывзо функции описанрой выше
    });

//    $('.basket-container').mouseout(function(){  //что будет вывполняться с этим элементо при не наведении мышью(элемент с классом basket-container-корзинана навбаре)
//       showingBasket();  ////вывзо функции описанрой выше
//       $('.basket-items').addClass('hidden');    //$('.basket-items')-обращаемся к элементу с классом basket-items как к элементу jqery,addClass('hidden')-означает что добовляет класс hidden(видимость)если его нет
//     });

     $(document).on('click', '.delete-item', function(e){   //описание функции котороя происходит при нажати элемента с классом delete-item это крестик в корзине
         e.preventDefault();

     });


});
