﻿> Важная особенность: метод ВызватьПаузу недоступен в клиент-серверном вызове; при вызове с клиента серверного метода, в котором вызывается ВызватьПаузу, будет сгенерировано исключение «Нельзя вызвать метод ВызватьПаузу в клиент-серверном вызове».
>
> [Метод ВызватьПаузу](https://wonderland.v8.1c.ru/blog/metod-vyzvatpauzu/)

Странное ограничение, если честно. С одной стороны, адекватный разработчик и так не будет в клиент-серверном вызове делать искусственную паузу, с другой — кому чешется, всё равно её там сделает (через проверку времени в цикле, например). Стоило ради security by obscurity огород городить?
  
В лучшем случае какой-нибудь джун схватит это исключение, подумает "похоже, я что-то не так делаю" и двинется в правильном направлении. Однако закладывать в платформу ограничение ради этого кейса — как из пушки по воробьям палить. Давайте ещё лимит по количеству прикрутим — мол, не больше 1000 пауз на сеанс, а то вдруг пользователи подумают, что программа работает слишком медленно :-)