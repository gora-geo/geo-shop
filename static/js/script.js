$(document).ready(function(){                // стандартная обертка jqery которая говорит о том что даннный код будетвыполняться после токго как загрузиться весь html-документ
    var form = $('#form_buying_product');     //мы хотим обратиться к форме поэтому вводим переменную form знак долара означает что мы хотим обратиться к элементу как к элементу jqery,form_buying_product-это id формы в product.html #-означает что мы хотим  выбрать элемент по id
    console.log(form);                      //мы выводим переммменю в console(в браузере надо нажать иследовать элемент там будет console)
    function basketUpdating(product_id, nmb, is_delete){   //создаем функцию basketUpdating product_id, nmb, is_delete-Имена параметров для создаваемой функции
         var data = {};    //вводим перемееню(пустой список(или словарь) куда будем отправлять id продукта ,которое добовляет в карзину его количество
         data.product_id = product_id; //записывем с писок data переменую product_id под полкой product_id
         data.nmb = nmb;               //записывем с писок nmb переменую product_id под полкой nmb
         var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();   //считывет токен с формы form_buying_product(product.html)
         data["csrfmiddlewaretoken"] = csrf_token;  //записыввем в переменную список data под индексом именем

         if (is_delete){                //если есть такойвходящий параметр is_delete
            data["is_delete"] = true;     //записывем в переменную data по ключу is_delete значение true

         }

         var url = form.attr("action");   //адрес куда необходимо отрправить пост запрос,это это значениеатрибута формыы  action

         console.log(data)        //вывод в консоль переменной data
         $.ajax({                  //обозначени что от сюда идет код ajax
                url: url,         //здесь сипользуеться url который описан 2 строки выше
                type: 'POST',     //используеться тип запроса-запрос с пост обработкой
                data: data,       //используеться data фаил описанный выше
                cache: true,      //используеться кеширование - true(истина) (кэширование некий буфер где храняться данные  для ускоренногоработы  с ним)
                success: function (data) {   // success-это функция которая вызываеться если успешно получен ответ с сервера
                 console.log("OK");         //выводим ок в консоль

                 console.log(data.products_total_nmb);  //выводим в консоль присланое из django(смотри order/views.py)значение products_total_nmb
                 if (data.products_total_nmb || data.products_total_nmb == 0){   //условие если она существует
                    $('#basket_total_nmb').text("("+data.products_total_nmb+")"); //в элемент с id=basket_total_nmb(navbar.html)-будем записывать переданное значение
                      console.log(data.products);      //вывод в консоль значения значения переменой(словаря)data по ключу products
                      $('.basket-items ul').html(""); //выводим в консоль браузера содержимое первого элемента с классом basket-items и входящих внего ul
                                                        // $('.basket-items ul').-тоеть делаем элемент с классом basket-items элементом jqery(div в navbare) ul(означает что на уровень ниже есть элемент(тоесть в ul входяший div)

                      $.each(data.products, function(k, v){
                                              //.each - это метод, который применяется к набору элементов для организации цикла по ним
                                              //data.products-массив(объект)
                                              //// function(k, v)-действия, которые будут выполняться для каждого элемента массива
                                             //k - это текущий индекс элемента массива (число)
                                             //v - это значение текущего элемента массива
                        $('.basket-items ul').append('<li style="list-style-type: none">'
                            + v.name+', ' + v.nmb + 'шт. ' + 'по ' + v.price_per_item + 'руб.  ' +'  '+
                            '<a class="delete-item" href="" data-product_id="'+v.id+'">x</a>'+'  '+
                            '</li>');
                               //(то что будет выводиться в ячейку корзины при нажати купить)
                               // $('.basket-items ul').-тоеть делаем элемент с классом basket-items элементом jqery(div в navbare) ul(означает что на уровень ниже есть элемент(тоесть в ul входяший div)
                               // ul (в элемент с классом basket-items входит элемент ul),append('<li>---</li>')-и добовляем в строку (добавить в ul)---

                      });
                 }
                 },
                error: function(){        //error-эта функция вызываеться если ответ с сервера получен не успешно
                 console.log("error")     //выводим в консоль error
                }
         })
    }
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
        basketUpdating(product_id, nmb, is_delete=false)   //выполнение функции basketUpdating(описаной выше) с переменными введеными несколко строк выше
        console.log(price);              //выводим в консоль переменную price
       // location.reload();//перезагрузить страницу чтобы открывалась корзина

           });



//
//    function showingBasket(){                       //вводим функцию showingBasket() котороая будет отвечать за отображенияокошкаа всплывающего окошка корзины
//        $('.basket-items').removeClass('hidden');   //$('.basket-items')-обращаемся к элементу(в navbar.html) с классом basket-items как к элементу jqery,removeClass('hidden')-означает что если  класса hidden есть он его удалает
//    };
//    $('.basket-container').mouseover(function(){   //что будет вывполняться с этим элементо(в navbar.html) при наведении мышью(элемент с классом basket-container-корзинана навбаре)
//       showingBasket();   //вывзо функции описанрой выше
//    });
//
//    $('.basket-container').mouseout(function(){  //что будет вывполняться с этим элементо при не наведении мышью(элемент с классом basket-container-корзинана навбаре)
//       showingBasket();  ////вывзо функции описанрой выше
//       $('.basket-items').addClass('hidden');    //$('.basket-items')-обращаемся к элементу с классом basket-items как к элементу jqery,addClass('hidden')-означает что добовляет класс hidden(видимость)если его нет
//     });

     $(document).on('click', '.delete-item', function(e){   //описание функции котороя происходит при нажати элемента с классом delete-item это крестик в корзине
         e.preventDefault();                     // e.preventDefault();-фция чтобы форма не обновлялась а то сторока ниже не выведиться
         product_id = $(this).data("product_id")    //вводим переменную  $(this).data("product_id") -обращение к data атрибуту по  значению product_id как к элеаменту jqery
         nmb = 0;    //введем перемменую nmb присвоим значение  0
         basketUpdating(product_id, nmb, is_delete=true)   //вывполнение функции basketUpdating(обновление корзины)
         //location.reload();//перезагрузить страницу чтобы открывалась корзина
     });
         function calculatingBasketAmount(){            //начинаем описание фу-ции    calculatingBasketAmount(колькулятор корзины сумма)
//              console.log("calculatingBasketAmount");   //вывод в консоль слова calculatingBasketAmount
              var total_order_amount=0;            //вводим переменную total_order_amount(общая сума заказов) пиисваиваем значение ноль
              $('.total-product-in-basket-amount').each(function(){   //$('.total-product-in-basket-amount')-обращаемся к элементу(в checkout.html) с классом total-product-in-basket-amount как к элементу jqery,.each-то универсальная функция jQuery с помощью которой можно осуществить перебор элементов массива или объекта.в даном случае это функция описанная ниже
//               console.log($(this).text());
              total_order_amount =total_order_amount+parseFloat($(this).text());  //parseFloat($(this).text())--берем элемент $('.total-product-in-basket-amount') переводим его в текст а его в чесло
              });

    console.log(total_order_amount);   //вывод в консоль переменной total_order_amount(общей суммы заказа)
    $('#total_order_amount').text(total_order_amount.toFixed(2));    //$('#total_order_amount')-берем элемент из checkout.html элемент с id=total_order_amount,.text(total_order_amount.toFixed(2));  -задаем содержимое элемента равное значению элемента total_order_amount с 2 знаками после запятой
         };

//    console.log("123");                                           //вывод в консоль значения 123
    $(document).on('change','.product-in-basket-nmb',function(){      //описание функции котороя происходит при нажати стрелочки элемента с классом product-in-basket-nmb это инпут со трелочками для увеличения количества напротив  каждого наименования товара
        var current_nmb=$(this).val();      //вводим переменную current_nmb(текушее значение) -это значение элемента с классом product-in-basket-nmb,.val()-без параметров метод не принимает аргументов
        console.log(current_nmb);          //выводим в консоль переменную current_nmb(текущее значение)
        var current_tr=$(this).closest('tr');    //ввоодим переменную current_tr(текущий тег tr) ,-значение которое принимает первый тег <tr> выше(вверх) по html-документу(дом -дереву)
        var current_price=parseFloat(current_tr.find('.product-price').text()).toFixed(2);   //вводим переменную current_price(текущая цена),parseFloat(current_tr.find('.product-price').text()).toFixed(2);-запускает поиск внутри переменной current_tr по классу product-price,далее полученные данные выдает ввиде текста,а текст преобразуеться в в число с 2 знаками после запятой
        console.log(current_price);      //вывод в консоль перемееной current_price(текущая цена)
        var total_amount=parseFloat(current_nmb*current_price).toFixed(2);   //вводим переменную total_amount(общая суммма),которая равна числовому значению умножения 2 пере енных ,ввиди числа с 2 знаками после запятой
        console.log(total_amount);    //вывод в консоль переменной total_amount(общая сумма)
        current_tr.find('.total-product-in-basket-amount').text(total_amount);   //поиск в переменной current_tr(текущий тег tr) элемента с клсасом total-product-in-basket-amount,.text(total_amount)-найденный элемент залаем содержимое равное переменной total_amount(общая суммма)
        calculatingBasketAmount();   //вывполнение функции  calculatingBasketAmount(); описангой выще
      //  location.reload();//перезагрузить страницу чтобы открывалась корзина
    });
    calculatingBasketAmount();    //вывполнение функции  calculatingBasketAmount(); описангой выще





});
