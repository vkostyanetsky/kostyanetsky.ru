﻿Задержки вида PageIOLatch (я про них сегодня [писал](/notes/pageiolatch)) легко встретить в любых системах, в том числе небольших. С задержками PageLatch дела обстоят наоборот — их трудно заметить, пока пользователей меньше нескольких тысяч.

Дело в том, что они возникают, когда страница находится в оперативной памяти и её пытаются изменить несколько пользователей. Пока один пользователь не завершит модификацию — прочие должны ждать. Время ожидания обычно ничтожно, однако если конкурирующих за страницу пользователей много — оно становится заметным.

Возможных причин две.

## Горячее место в индексе

Такой расклад иногда называют хотспотом. Он возникает, когда мы массово пытаемся писать что-то на последнюю страницу индекса; в первую очередь речь идёт об индексе с монотонно возрастающим ключом — например, любые индексы по полям ссылочного типа (начиная с последних версий 8.2, платформа выдает последовательные GUID — это снижает фрагментацию диска и делает ключ индекса монотонно возрастающим).

Что такое «индекс с монотонно возрастающим ключом»? Для платформы 1С это, например, индексы регистров по периоду. Конечно, они растут не вполне монотонно — однако тут скорее важно, что данные мы всегда будем писать в конец. Сюда же относятся индексы по номеру документа и индексы по коду справочника — в обеих случаях мы выдаем некий новый номер, который пишется в конец индекса.

Решается проблема хотспота только архитектурно — нужно добиться того, чтобы данные записывались в разные места индекса, а не только в конец.

## Системные страницы tempdb

Когда мы создаём или удаляем таблицу в базе данных, в ней обновляется ряд служебных страниц — IAM (Index Allocation Map), PFS (Page Free Space), GAM (Global Allocation Map), SGAM (Shared Global Allocation Map) и другие.

Почему это важно для tempdb? Для платформы 1С это база, в которой регулярно создается **огромное** количество таблиц. Служебные страницы при этом обновляются настолько часто, что при этом возникают задержки семейства PageLatch.

Вообще-то MS SQL Server умеет оптимизировать обновления системных страниц для tempdb, благодаря чему это делается реже, но иногда даже этого не достаточно. Особенно если в tempdb создаются таблицы с индексами — а это очень частый кейс для приложений на 1С.

У проблемы есть несколько возможных решений. Первый — если СУБД старше 2016-й, можно отключить смешанные экстенты через флаг трассировки 1118. При этом исчезнет необходимость сразу в двух служебных страницах — GAM и SGAM. Соответственно, ожиданий на их обновлении не будет. Экстент — это восемь страниц данных, т.е. 64 килобайта; если он содержит страницы одной таблицы — это нормированный экстент, если нескольких — смешанный.

Второй подход — разбивать tempdb (с 2016-й версии СУБД она, кстати, по умолчанию разбивается на восемь файлов). Дело в том, что служебные страницы ведутся в разрезе файлов; если их будет несколько — ожидания на обновлениях служебных страниц будут ниже.

Третий вариант — уменьшать количество временных таблиц с целью снизить нагрузку на tempdb. То есть переписывать наиболее частотные запросы так, чтобы они работали приемлемо быстро без временных таблиц.