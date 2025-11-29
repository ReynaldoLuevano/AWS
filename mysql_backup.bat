@echo off
REM Configuración de la base de datos
set DB_HOST=localhost
set DB_USER=admin
set DB_PASSWORD=password123
set DB_NAME=myapp

REM Configuración del backup
set BACKUP_DIR=C:\backups\mysql
set DATE=%date:~-4,4%%date:~-10,2%%date:~-7,2%_%time:~0,2%%time:~3,2%%time:~6,2%
set BACKUP_FILE=cliente_backup_%DATE%.sql

REM Crear directorio de backup
if not exist "%BACKUP_DIR%" mkdir "%BACKUP_DIR%"

REM Generar backup
mysqldump -h %DB_HOST% -u %DB_USER% -p%DB_PASSWORD% --single-transaction --routines --triggers %DB_NAME% clientes > "%BACKUP_DIR%\%BACKUP_FILE%"

echo Backup completado: %BACKUP_DIR%\%BACKUP_FILE%