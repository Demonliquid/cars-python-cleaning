-- Backup to CSV for manipulation with python/openrefine


USE argentina;


-- cod_prom columnas y contenido
SELECT `COLUMN_NAME` 
FROM `INFORMATION_SCHEMA`.`COLUMNS` 
WHERE `TABLE_SCHEMA`='argentina' 
AND `TABLE_NAME`='cod_prom'
INTO OUTFILE 'D:\\Basededatos\\Limpioparaunir\\Argentina\\cod_prom_columns.csv'
FIELDS ENCLOSED BY '"' 
TERMINATED BY ';' 
ESCAPED BY '"' 
LINES TERMINATED BY '\r\n';

SELECT *
FROM argentina.cod_prom
INTO OUTFILE 'D:\\Basededatos\\Limpioparaunir\\Argentina\\cod_prom.csv'
FIELDS ENCLOSED BY '"' 
TERMINATED BY ';' 
ESCAPED BY '"' 
LINES TERMINATED BY '\r\n';


-- flota columnas y contenido
SELECT `COLUMN_NAME` 
FROM `INFORMATION_SCHEMA`.`COLUMNS` 
WHERE `TABLE_SCHEMA`='argentina' 
AND `TABLE_NAME`='flota'
INTO OUTFILE 'D:\\Basededatos\\Limpioparaunir\\Argentina\\flota_columns.csv'
FIELDS ENCLOSED BY '"' 
TERMINATED BY ';' 
ESCAPED BY '"' 
LINES TERMINATED BY '\r\n';

SELECT *
FROM argentina.flota
INTO OUTFILE 'D:\\Basededatos\\Limpioparaunir\\Argentina\\flota.csv'
FIELDS ENCLOSED BY '"' 
TERMINATED BY ';' 
ESCAPED BY '"' 
LINES TERMINATED BY '\r\n';

-- historicos columnas y contenido
SELECT `COLUMN_NAME` 
FROM `INFORMATION_SCHEMA`.`COLUMNS` 
WHERE `TABLE_SCHEMA`='argentina' 
AND `TABLE_NAME`='historicos'
INTO OUTFILE 'D:\\Basededatos\\Limpioparaunir\\Argentina\\historicos_columns.csv'
FIELDS ENCLOSED BY '"' 
TERMINATED BY ';' 
ESCAPED BY '"' 
LINES TERMINATED BY '\r\n';

SELECT *
FROM argentina.flota
INTO OUTFILE 'D:\\Basededatos\\Limpioparaunir\\Argentina\\historicos.csv'
FIELDS ENCLOSED BY '"' 
TERMINATED BY ';' 
ESCAPED BY '"' 
LINES TERMINATED BY '\r\n';