﻿Недавно внедрили в нашу конфигурацию встроенный в платформу механизм истории данных вместо морально и функционально устаревшего велосипеда из SSLi. Сейчас как раз дописываю выгрузку историю данных в бэкап и загрузку его обратно: удивительно, но этого пока не умеет ни БСП, ни БТС, ни SSLi (впрочем, от последней я и не ждал).

Как закончу, расскажу подробнее. Пока хочу отметить любопытную опцию, которая пригодилась по ходу дела: встроенные в платформу обработки, которые доступны из меню «Все функции», можно выгрузить в виде обычных epf-файлов! Трюк очень подробно разобрали коллеги на Инфостарте ([вот тут](https://infostart.ru/public/369487/) и [вот тут](https://infostart.ru/public/538300/)). Вкратце магия выглядит вот так:

    КопироватьФайл(
        "v8res://mngbase/StandardDataChangeHistory.epf",
        "Q:/StandardDataChangeHistory.epf"
    );

Полный список стандартных форм и обработок, которые можно вытащить, способ получения этого списка, а также куча споров вокруг и около — по ссылкам выше.

Зачем это пригодится вам — честно, не знаю. Что касается нас, то мы делали интерфейсы для работы с историей данных и было любопытно, как они написаны у самой 1С (спойлер: довольно неряшливо).