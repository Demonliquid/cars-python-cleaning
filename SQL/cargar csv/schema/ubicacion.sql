SET GLOBAL local_infile = 1;
USE vehiculosdemotor;
LOAD DATA LOCAL INFILE "D:\\Basededatos\\Unificada\\Ubicacion.csv" INTO TABLE vehiculosdemotor.ubicacion
FIELDS TERMINATED BY ";"
ENCLOSED BY '"'
LINES TERMINATED BY "\n"
IGNORE 1 LINES
(
`CONTINENTE`,
`PAIS`,
`PROVINCIA`,
`CIUDAD`,
`CODIGO_POSTAL`
)
SET	`CONTINENTE` = nullif(`CONTINENTE`, ''),
    `PAIS` = nullif(`PAIS`, ''),
    `PROVINCIA` = nullif(`PROVINCIA`, ''),
    `CIUDAD` = nullif(`CIUDAD`, ''),
    `CODIGO_POSTAL` = nullif(`CODIGO_POSTAL`, '')
;
