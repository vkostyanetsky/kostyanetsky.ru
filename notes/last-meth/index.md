Роюсь в коде внешней компоненты 1С, опубликованный разработчиками платформы как пример у себя на сайте. Из хорошего: ну, она компилируется и, если немного допилить — действительно работает. 

В остальном хватает bruh moments: например, проект не открывается в современной Visual Studio (нужно указывать CMake вручную). Код довольно небрежный, документации нет, комментариев и оформления по большому счёту тоже. Разработчику без опыта в С++ может быть непросто вкатиться.

Позабавила реализация поиска метода компоненты:

    long CAddInNative::FindMethod(const WCHAR_T* wsMethodName)
    { 
        long plMethodNum = -1;
        wchar_t* name = 0;

        ::convFromShortWchar(&name, wsMethodName);

        plMethodNum = findName(g_MethodNames, name, eMethLast);

        if (plMethodNum == -1)
            plMethodNum = findName(g_MethodNamesRu, name, eMethLast);

        delete[] name;

        return plMethodNum;
    }

Со строк выше на нас смотрит необъяснимая любовь автора кода к сокращениям: вот что ему мешало назвать переменную с индексом последнего метода "eMethodLast", а не "eMethLast"? В конце концов, у нас уже есть "wsMethodName" и "plMethodNum". 

Возможно, это такая пасхалка с отсылкой на Breaking Bad. Тогда, конечно, уверенный лайк :)