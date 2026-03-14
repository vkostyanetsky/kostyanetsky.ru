---
title: Сделай это педантично
description: Как сравнить две булевые переменные?
created: 2023-03-21 20:26:43
tags:
- 1c
- work
- code-smell
---

Ежедневная пальма первенства в номинации «самый философский код» уходит автору этого элегантного способа проверить, что две булевые переменные не равны друг другу:

    If DataStructure.Property("AmountVATIn")
        And ((DataStructure.AmountVATIn And NOT SearchPriceIncludesVAT)
        OR (NOT DataStructure.AmountVATIn And SearchPriceIncludesVAT)) Then    
        Price = RecalculateAmountOnVATFlagsChange(Price, DataStructure.AmountVATIn, TabSectionLine.VATRate);
    EndIf;

Думаю дописать сюда что-нибудь вроде «And Not (DataStructure.AmountVATIn = SearchPriceIncludesVAT)», чтобы придать происходящему тонкую нотку безумия.