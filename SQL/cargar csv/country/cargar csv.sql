SET GLOBAL local_infile = 1;
USE pruebaperu;
LOAD DATA LOCAL INFILE "D:\\Basededatos\\schema\\bases\\flotaperu.csv" INTO TABLE pruebaperu.vehiculos
FIELDS TERMINATED BY ";"
ENCLOSED BY '"'
LINES TERMINATED BY "\n"
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
`MODELO`
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
    `MODELO` = nullif(`MODELO`, '')
    ;
