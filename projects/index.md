На этой странице собраны некоторые проекты, в которых я участвовал и о которых нашлось время написать.с

Сортировка — по времени, от новых к старым.

## Клиентский портал

<span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">FirstBit ERP</span> <span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">1С:Предприятие</span> <span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">1С:Шина</span> <span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">RabbitMQ</span> <span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">FastAPI</span> <span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">Python</span> <span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">React.js</span> <span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">Typescript</span>

Заказчик пишет софт и продает на него подписки. Нужно было сделать веб-сайт, на котором его клиенты смогут работать с подписками без помощи менеджеров заказчика. Например:

- увидеть данные этих подписок (купленный продукт, срок действия);
- оплатить истекающие подписки с помощью банковской карты;
- скачать выставленные компанией счета и накладные.

[Подробности](/projects/customer-portal/)

## Веб-интерфейс базы 1С для поставщиков

<span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">FirstBit ERP</span> <span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">1С:Предприятие</span> <span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">Flask</span> <span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">Python</span> <span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">React.js</span> <span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">Typescript</span>

Нашим заказчиком был владелец торговой компании. Часть её деятельности — проценка: сотрудники компании связывались с поставщиками, определяя, у какого из них выгоднее разместить заказы клиентов с точки зрения цен, сроков доставки и других условий.

От нас требовалось сделать так, чтобы они могли просто отправлять поставщикам ссылки на веб-интерфейс, где можно было бы вводить цены и отвечать на дополнительные вопросы.

Веб-интерфейс платформы использовать было нельзя из соображений экономии лицензий. Поэтому я написал веб-приложение на React.js, которое работает с базой 1С:Предприятия через специально разработанный для этого REST-интерфейс.

Упрощенную версию проекта можно [посмотреть](https://github.com/vkostyanetsky/RFQ) на GitHub'е.

## Сбор курсов валют с сайта ЦБ ОАЭ

<span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">FirstBit ERP</span> <span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">1С:Предприятие</span> <span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">Flask</span> <span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">Python</span> <span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">MongoDB</span> <span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">NoSQL</span> 

Мы хотели дать пользователям FirstBit ERP возможность автоматически получать курсы дирхама по отношению к другим валютам, которые публикует сайт ЦБ ОАЭ.

Код парсинга сайта можно было добавить в саму конфигурацию, однако эта идея выглядела проблемной сразу с нескольких точек зрения: удобного механизма для получения курсов на сайте ЦБ нет, сам сайт работает нестабильно, а при необходимости изменить логику парсинга её придется менять во множестве баз данных.

Поэтому я написал консольное приложение на пайтоне, которые регулярно загружает публикуемые курсы валют в свою базу данных и отдает через REST-сервис. Мы развернули это приложение на своей площадке, а в FirstBit ERP я добавил только регулярные обращения к сервису.

Код серверной части проекта можно [посмотреть](https://github.com/vkostyanetsky/UAExchangeRates) на GitHub'е.

## История данных в FirstBit ERP

<span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">FirstBit ERP</span> <span class="f6 link br3 ph3 pv1 mb2 dib blue bg-lightest-blue">1С:Предприятие</span>

В конфигурации FirstBit ERP я заменил подсистему версионирования БСП на встроенный в платформу [механизм](https://wonderland.v8.1c.ru/blog/istoriya-dannykh/), решающий ту же задачу. В проект вошли:

1. Алгоритм миграции истории изменений из регистров сведений во встроенное хранилище платформы.
2. Обработка, с помощью которой можно включать и выключать историю для объектов и их реквизитов. Раннюю версию можно [посмотреть](https://github.com/vkostyanetsky/AuditLogSettings) на GitHub'е.
3. Обработка, способная выводить в одном списке изменения по разным объектам за указанный период. 
4. Анализ объектов конфигурации (был нужен, чтобы выключить историю данных для объектов, которые нет смысла версионировать — неразделенные объекты 1сFresh, служебные справочники и так далее).
5. Доработка алгоритма выгрузки информационной базы в XML-файлы и загрузки из них (с тем, чтобы при выгрузке история так же выгружалась в XML-файлы, а при загрузке — подгружалась из них).