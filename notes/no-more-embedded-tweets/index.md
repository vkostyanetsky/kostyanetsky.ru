﻿Не успел я [выпилить](/notes/no-more-google-fonts/) из блога Google Fonts, как пришлось отправить вдогонку встроенные твиты.

Как это работало раньше? Хотел сослаться на твит — просто вставлял на него ссылку. Скрипт сборки заменял её на HTML-блок, который находил скрипт Твиттера и заменял на текст твита (и всякими полезными ссылками). Вот в этом [коммите](https://github.com/vkostyanetsky/BlogBuilder/commit/c21ef8a7bec10672406e6be57b8e734ba3ac01c5) в целом видно, как это работало.

Как это работает теперь? Ну да, никак. Твиттер в России заблокирован, так что его скрипты работают только со включенным VPN.

![Штош](well.jpg)

Пришлось поскринить все твиты, на которые я когда-то ссылался, и добавить их в заметки в виде картинок со ссылками. Кому нужен оригинал, тот найдёт способ перейти в Твиттер, а остальные, по крайней мере, могут прочитать текст.

Пара слов про техническую сторону. Скринить каждый твит вручную мне было лень, поэтому я полез в сеть, обдумывая, как автоматизировать процесс. Сначала попадались только сервисы, готовые решить проблему за какие-то жалкие десять долларов (спасибо, как-нибудь в следующий раз), но потом я набрёл на идеальный [инструмент](https://github.com/privatenumber/snap-tweet): консольный скрипт для Node.js.

Ничего лишнего. Чистый функционал. Ты ему — твит. Он тебе — картинку:

> npx snap-tweet https://twitter.com/PossumEveryHour/status/1506148678461014016

И всё. Захотелось занести автору денег.

Подумал, не прикрутить ли snap-tweet к скрипту сборки (чтобы было, как раньше: вставляешь ссылку на твит, а дальше оно само генерит картинку и кладёт куда надо). Решил, нафиг. Грубое попирание KISS, да и вообще... В мире и так хватает энтропии. Особенно, блин, сейчас.