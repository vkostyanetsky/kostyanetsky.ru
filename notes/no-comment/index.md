﻿Сам не заметил, как бросил привычку педантично комментировать каждый метод, с которым приходится работать. Наверняка у этой практики есть какое-нибудь умное название, но мне нет дела, если честно. Я имею в виду стиль, когда описание добавляют к каждому осмысленному блоку кода:

https://gist.github.com/vkostyanetsky/afae4dee09d639f34156d6c02b29c2a5

Смысл тут простой: когда копаешься в каком-нибудь дремучем легаси и бегаешь туда-сюда между хаотично раскиданными процедурами на три экрана каждая — логику каждой из них держать в голове довольно трудно. Первая же чашка кофе всё смоет. Поэтому такие заметки на полях здорово ускоряют ориентацию на местности, и чем больше времени проходит между подходами к коду — тем заметнее эффект.

Однако в какой-то момент стало понятно, что это ноу-хау — просто костыль, подпирающий откровенно хреновый дизайн кода. Попалась тебе длинная процедура или функция — вздохни, сядь и нарежь толстяка на методы поменьше. Сэкономишь и время, и нервы, и в коде разберешься быстрее, и Сонар порадуешь.