﻿Хочу поделиться парой классных текстов о современном софте. Они не особенно свежие (первый-то уж точно), но наверняка ведь кто-то пропустил:

- [Моё разочарование в софте](https://tonsky.me/blog/disenchantment/ru/) Никиты Тонского
- [В софте всё восхитительно, но все недовольны](https://habr.com/ru/company/jugru/blog/493178/) Евгения Трифонова

К чему я это вспомнил? На прошлой неделе участвовал в хакатоне среди программистов нашей компании. Узнал кучу клевых штук, а по итогам даже занял первое место (вместе с ещё двумя участниками, у которых получились очень похожие решения).

(если вы — тоже сотрудник «Первого БИТа», то [итоги](https://newportal.1cbit.ru/news/3066979/) хакатона лежат на портале; там же — [отзыв](https://newportal.1cbit.ru/news/3066980/) другого победителя, Димы Лещенко)

В процессе нужно было развернуть и настроить целую гору софта: EDT, RabbitMQ, Docker, GitLab, JIRA, SonarQube и ещё вагон инструментов поменьше и попроще. Ладно, к RabbitMQ у меня претензий нет: легкий и быстрый, но вот остальное... Про хороший аппетит EDT я знал и раньше, а вот прожорливость GitLab и JIRA по-настоящему удивила.

Да, в моём случае всё запускалось в докере; да, конфигурация не была оптимальной (например, было развернуто несколько серверов PostgreSQL вместо одного); да, докер был для Windows, а его реализация под эту платформу — тема для едких шуток у всех сисадминов, с которыми я знаком. Но потратить 12 гигабайт ОЗУ прямо со старта?! Про процессор вообще молчу — нагрузка была такая, будто компьютер просчитывал ядерный взрыв в реальном времени.

Короче, лучшей иллюстрации к тезисам Никиты подобрать трудно: софт выше слопал море ресурсов и невозмутимо попросил ещё, даже не приступив к какой-то понятной задаче. Впрочем, в то же время это отличная иллюстрация к тексту Евгения: я, на секундочку, одной-единственной командой развернул несколько операционных систем со сложными серверами внутри. И потратил на это несоизмеримо меньше времени чем, скажем, пришлось бы потратить несколько лет назад.

У меня нет ответа. Думаю, ни у кого нет. Это такой вечный холивар внутри профессии: какую сторону не займи, на деле все равно балансируешь между двумя крайностями — с одной стороны, надо писать хороший, быстрый код, с другой — надо не свалиться в преждевременную оптимизацию. Первое в итоге дает чистое удовольствие от хорошо сделанной работы: вспоминаешь, что ты, черт побери, неплох! Второе — просто позволяет не нажить бед с башкой в поисках идеального алгоритма сортировки пузырьком :-)