#!/bin/bash

# Configuración de la base de datos
DB_HOST="localhost"
DB_USER="admin"
DB_PASSWORD="password123"
DB_NAME="myapp"

# Configuración del backup
BACKUP_DIR="/backups/mysql"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="cliente_backup_${DATE}.sql"

# Crear directorio de backup si no existe
mkdir -p $BACKUP_DIR

# Generar backup con datos de cliente
mysqldump -h $DB_HOST -u $DB_USER -p$DB_PASSWORD \
  --single-transaction \
  --routines \
  --triggers \
  --where="1" \
  $DB_NAME clientes > $BACKUP_DIR/$BACKUP_FILE

# Comprimir el backup
gzip $BACKUP_DIR/$BACKUP_FILE

echo "Backup completado: $BACKUP_DIR/${BACKUP_FILE}.gz"