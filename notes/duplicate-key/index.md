﻿На Инфостарте вышла любопытная [статья](https://infostart.ru/public/1010017/) про ошибку СУБД «cannot insert duplicate key». Одна из возможных причин сбоя — использование уникального идентификатора объекта для сопоставления при обмене с другими информационными базами (то есть, без служебного регистра, сопоставляющего объекты базы данных с идентификаторами объектов внешней базы).

Такой жести, чтобы уникальные идентификаторы совпали в разных базах для одной и той же таблицы, у меня в практике пока не было. Однако от подхода «единого идентификатора» я отрекся окончательно после того, как делал обмен между [FirstBIT ERP](https://firstbit.ae/products/erp-dubai/financial_management/) и [GROTEM / Agent](http://superagent.ru/products/grotem_agent)</a>.

Архитектура пилотного решения была такая: данные из FirstBIT ERP выгружались сперва в служебную ИБ 1С, написанную разработчиками GROTEM'а, а уже оттуда — в основную базу данных сервера мобильных приложений.

Сопоставление было сделано очень просто — через идентификаторы объектов. Например, один и тот же документ в обеих базах имел один и тот же идентфикатор. Но были и более сложные схемы: например, контрагент FirstBIT ERP на стороне GROTEM'а превращался в три объекта: собственно контрагента, торговую точку и документ взаиморасчетов.

![WAIT WHAT](https://media.giphy.com/media/zkSFsZpQMZuG4/giphy.gif)

Да, в документ взаиморасчетов. И все три объекта имели один и тот же идентфикатор — идентификатор контрагента FirstBIT ERP. В общем, не то чтобы это было очень изящным решением, но для платформы такой расклад вполне адекватен и мы решили, что проблем быть не должно.

Однако обмен работать отказался.

Беглый анализ показал, что данные успешно выгружаются в промежуточную базу данных и проходят все возможные проверки на целостность и полноту, а не работает только финальный шаг — выгрузка в базу данных сервера мобильных приложений.

В итоге выяснилось, что:

1. В этой самой базе есть таблица, где хранятся все интересующие нас объекты. Документы, элементы справочников, вот это всё.
2. Эта таблица имеет уникальный индекс по GUID объекта.

В этом месте интрига закончилась. Ну да, первый же выгруженный контрагент создавал целых три сущности с одним и тем же GUID, которые прекрасно лежали в своих таблицах на стороне 1С, но не могли быть записаны в одну общую таблицу базы данных приложения.

![I will not use GUIDs to map objects!](i-will-not-use-guids.gif)