SET GLOBAL local_infile = 1;
USE chile;
LOAD DATA LOCAL INFILE "D:\\Basededatos\\Limpioparaunir\\chile.csv" INTO TABLE chile.flotachile
FIELDS TERMINATED BY ","
ENCLOSED BY '"'
LINES TERMINATED BY "'\r\n"
IGNORE 1 LINES
(`PATENTE`,
`SEGMENTO.1`,
`MARCA`,
`MODELO/VERSION`,
`AÑO`,
`DATOS PERSONALES`,
`NUMERO MOTOR`,
`MERCADO`,
`FLOTA 2019`,
`MOTOR`,
`MODELO`,
`MGEN`,
`VERSION (SALES DESCRIPTION)`
)
SET	`PATENTE` = nullif(`PATENTE`, ''),
	`SEGMENTO.1` = nullif(`SEGMENTO.1`, ''),
    `MARCA` = nullif(`MARCA`, ''),
    `MODELO/VERSION` = nullif(`MODELO/VERSION`, ''),
    `AÑO` = nullif(`AÑO`, ''),
    `DATOS PERSONALES` = nullif(`DATOS PERSONALES`, ''),
    `NUMERO MOTOR` = nullif(`NUMERO MOTOR`, ''),
    `MERCADO` = nullif(`MERCADO`, ''),
    `FLOTA 2019` = nullif(`FLOTA 2019`, ''),
    `MOTOR` = nullif(`MOTOR`, ''),
    `MODELO` = nullif(`MODELO`, ''),
    `MGEN` = nullif(`MGEN`, ''),
    `VERSION (SALES DESCRIPTION)` = nullif(`VERSION (SALES DESCRIPTION)`, '')
    ;
