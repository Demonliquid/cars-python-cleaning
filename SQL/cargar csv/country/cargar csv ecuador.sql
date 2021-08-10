SET GLOBAL local_infile = 1;
USE ecuador;
LOAD DATA LOCAL INFILE "D:\\Basededatos\\Limpioparaunir\\ecuador.csv" INTO TABLE ecuador.flotaecuador
FIELDS TERMINATED BY ","
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(
`MARCA`,
`MODELO/VERSION`,
`ORIGEN`,
`AÑO`,
`TIPO`,
`SEGMENTO`,
`SEGMENTO.1`,
`MOTOR`,
`CILINDRADA`,
`COMBUSTIBLE`,
`LOCALIDAD`,
`PROVINCIA`,
`MERCADO`,
`FLOTA 2019`,
`MODELO`,
`VERSION (SALES DESCRIPTION)`,
`MGEN`
)
SET	`MARCA` = nullif(`MARCA`, ''),
	`MODELO/VERSION` = nullif(`MODELO/VERSION`, ''),
    `ORIGEN` = nullif(`ORIGEN`, ''),
    `AÑO` = nullif(`AÑO`, ''),
    `TIPO` = nullif(`TIPO`, ''),
    `SEGMENTO` = nullif(`SEGMENTO`, ''),
    `SEGMENTO.1` = nullif(`SEGMENTO.1`, ''),
    `MOTOR` = nullif(`MOTOR`, ''),
    `CILINDRADA` = nullif(`CILINDRADA`, ''),
    `COMBUSTIBLE` = nullif(`COMBUSTIBLE`, ''),
    `LOCALIDAD` = nullif(`LOCALIDAD`, ''),
    `PROVINCIA` = nullif(`PROVINCIA`, ''),
    `MERCADO` = nullif(`MERCADO`, ''),
    `FLOTA 2019` = nullif(`FLOTA 2019`, ''),
    `MODELO` = nullif(`MODELO`, ''),
    `VERSION (SALES DESCRIPTION)` = nullif(`VERSION (SALES DESCRIPTION)`, ''),
    `MGEN` = nullif(`MGEN`, '')
    ;
