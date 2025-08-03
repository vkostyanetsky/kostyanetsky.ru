Коллега заметил, что на одном из инстансов нашего фреша удаление областей стало идти прямо-таки трагически долго. Полезли в метрики. 

<pre>
DELETE FROM T1
FROM _DataHistoryMetadata T1
WHERE 
    T1._MetadataId = ?
    AND T1._IsActual = 0x00 
    AND NOT (
        T1._MetadataVersionNumber IN (
            SELECT T2._MetadataVersionNumber AS MetadataVersionNumber_
            FROM _DataHistoryVersions T2
            WHERE T2._HistoryDataId IN (
                SELECT DataHistoryLatestVersions1.DataHistoryLatestVersions._HistoryDataId AS HistoryDataId_
                FROM DataHistoryLatestVersions1.DataHistoryLatestVersions T3
                WHERE DataHistoryLatestVersions1.DataHistoryLatestVersions._MetadataId = ?
            )
        )
    )
</pre>

Каждый такой запрос читает порядка двадцати гигабайт данных из таблицы истории данных. Что тут происходит — примерно понятно: платформа пытается удалить историю данных области и кривой запрос к БД приводит к сканированию всей таблицы по всем областям вместо быстрого поиска по индексу. Кто-то на Дмитровском опять поленился.

[![Чему ты удивлён?](why.png)](https://x.com/EffinBirds/status/1945545263407301033)

В общем, теряем от тридцати секунд до полутора минут на действие. Хотелось бы побыстрее. Решение:

<pre>
CREATE NONCLUSTERED INDEX IX_DataHistoryLatestVersions1_MetadataId
  ON dbo._DataHistoryLatestVersions1 (_MetadataId)
  INCLUDE (_HistoryDataId)
  WITH (DROP_EXISTING = OFF, ONLINE = OFF);
 
CREATE NONCLUSTERED INDEX IX_DataHistoryVersions_MetadataVersionNumber
  ON dbo._DataHistoryVersions (_MetadataVersionNumber)
  WITH (DROP_EXISTING = OFF, ONLINE = OFF);
</pre>

Стоимость удаления области ожидаемо просела на ~99%.

Если будете повторять у себя — помните, что:
        
1. Формально такой трюк нарушает лицензионное соглашение, you've been warned и всё такое.
2. Есть риск, что платформа при будущих реструктуризациях будет спотыкаться о новые индексы (особенно при работе по «новой» схеме). Лучше иметь под рукой готовый скрипт, который сможет грохнуть индекс, а потом (после реструктуризации) — вернуть обратно.
