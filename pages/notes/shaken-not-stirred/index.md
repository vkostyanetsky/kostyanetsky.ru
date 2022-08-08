Затрем немного про организацию кода. Если вам нужно где-то описать множество объектов с общими свойствами — подумайте, не стоит ли подробить описание на отдельные методы, каждый из которых будет описывать один конкретный объект?

Посмотрим на пример — метод, который описывает табличные части документов, пригодные для какой-то задачи. Что-то вроде:

    SupportedTypes["Document.SupplierPricesEntering"]   = "Prices";
    SupportedTypes["Document.OpeningBalancesEntering"]  = "CustomerAccounts,VendorAccounts";
    SupportedTypes["Document.Requisition"]              = "InventoryAndServices";

Вроде всё в порядке, так? Описания есть, табличные части перечислены, посплитить их по запятой — считай, бесплатно.

Однако документов в методе описано много. Рано или поздно какому-нибудь коллеге (или вам самим) понадобится добавить ещё одну табличную часть для документа, который уже описан в методе. Его что-то отвлечет, он забудет поискать существующую строку и получится что-то вроде:

    SupportedTypes["Document.SupplierPricesEntering"]   = "Prices";
    SupportedTypes["Document.OpeningBalancesEntering"]  = "CustomerAccounts,VendorAccounts";
    SupportedTypes["Document.Requisition"]              = "InventoryAndServices";

    <...>

    SupportedTypes["Document.OpeningBalancesEntering"]  = "PayrollDeductions";

В результате пара табличных частей выпадет из описания, и хорошо, если связанный функционал покрыт тестами.

Вывод? Ну, можно написать метод-хелпер, который будет принимать на вход тип документа и имя **одной** табличной части. Хелпер будет заполнять соответствие SupportedTypes и следить за тем, чтобы уже добавленные в него данные не были потеряны.

А если совсем по фен-шую, лучше поступить так, как я написал в начале заметки: разделить метод на отдельные вспомогательные методы, каждый из которых будет описывать только табличные части по одному документу. Что-то вроде:

    Procedure AddOpeningBalancesEnteringDocument(SupportedTypes)

        TabularSections = New Array;

        TabularSections.Add("CustomerAccounts");
        TabularSections.Add("VendorAccounts");
        TabularSections.Add("PayrollDeductions");

        SupportedTypes["Document.Requisition"] = StrImplode(TabularSections, ",");

    EndProcedure

Так и описание документа никто случайно не сотрет, и Сонар будет доволен. А вот случае реализации хелпера он, скорее всего, примется ругаться на повторяющиеся литералы с именами табличных частей.