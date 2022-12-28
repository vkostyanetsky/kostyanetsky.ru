На днях прикручивал работу с куками к одному из своих скриптов. Пока искал оптимальное решение, наткнулся на совершенно очаровательный (при этом, кстати, 100% рабочий) [совет](https://stackoverflow.com/questions/13030095/how-to-save-requests-python-cookies-to-a-file) со StackOverflow:

> You can get a CookieJar object from the session with session.cookies, and use pickle to store it to a file.

Ну то есть, буквально: держите ваше печенье в банке, а чтобы хранить его — маринуйте. Банку с маринованным печеньем, кстати, потом можно поставить на [полку](https://docs.python.org/3/library/shelve.html).

Вот как после этого не любить пайтон, а?

P.S. Пока писал заметку, разобрало любопытство — почему всё-таки pickle, а нe serialization? Так вот, если вкратце: [таков путь](https://stackoverflow.com/questions/27324986/pickles-why-are-they-called-that/27325007#27325007).