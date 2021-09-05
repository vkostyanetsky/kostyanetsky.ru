Для чего может пригодиться дата запуска MS SQL Server? Например, мы разбираем задержки в работе СУБД и хотим определить, в течении какого периода времени наполнялась DMV-шка [sys.dm_os_wait_stats](https://docs.microsoft.com/ru-ru/sql/relational-databases/system-dynamic-management-views/sys-dm-os-wait-stats-transact-sql). Её данные (как и любой другой DMV, впрочем) хранятся в оперативной памяти как раз с момента запуска СУБД.

Дату запуска сервера можно получить из  DMV-шки [sys.dm_os_sys_info](https://docs.microsoft.com/ru-ru/sql/relational-databases/system-dynamic-management-views/sys-dm-os-sys-info-transact-sql):

    SELECT sqlserver_start_time FROM sys.dm_os_sys_info

Есть и другой способ, связанный с tempdb. Эта база данных создаётся при запуске сервера, и дата её создания вполне может считаться датой запуска сервера. Значение можно вытащить из [sys.databases](https://docs.microsoft.com/ru-ru/sql/relational-databases/system-catalog-views/sys-databases-transact-sql):

    SELECT create_date FROM sys.databases WHERE name = 'tempdb'

Нюанс: дату запуска сервера как точку начала сбора данных DMV-шек нужно рассматривать с осторожностью. Накопленная статистика могла быть очищена вручную — например, вот так:

    DBCC SQLPERF('sys.dm_os_wait_stats', CLEAR)