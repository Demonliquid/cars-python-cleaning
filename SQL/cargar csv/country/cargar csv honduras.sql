SET GLOBAL local_infile = 1;
USE honduras;
LOAD DATA LOCAL INFILE "D:\\Basededatos\\Limpioparaunir\\honduras.csv" INTO TABLE honduras.flotahonduras
FIELDS TERMINATED BY ","
ENCLOSED BY '"'
LINES TERMINATED BY "\n"
IGNORE 1 LINES
(`MERCADO`,
`SEGMENTO.1`,
`MARCA`,
`MODELO`,
`MGEN`,
`MODELO/VERSION`,
`VERSION (SALES DESCRIPTION)`,
`AÑO`,
`MOTOR`,
`CILINDRADA`,
`COMBUSTIBLE`,
`FLOTA 2019`
)
SET	`MERCADO` = nullif(`MERCADO`, ''),
	`SEGMENTO.1` = nullif(`SEGMENTO.1`, ''),
    `MARCA` = nullif(`MARCA`, ''),
    `MODELO` = nullif(`MODELO`, ''),
    `MGEN` = nullif(`MGEN`, ''),
    `MODELO/VERSION` = nullif(`MODELO/VERSION`, ''),
	`VERSION (SALES DESCRIPTION)` = nullif(`VERSION (SALES DESCRIPTION)`, ''),
    `AÑO` = nullif(`AÑO`, ''),
    `MOTOR` = nullif(`MOTOR`, ''),
    `CILINDRADA` = nullif(`CILINDRADA`, ''),
    `COMBUSTIBLE` = nullif(`COMBUSTIBLE`, ''),
    `FLOTA 2019` = nullif(`FLOTA 2019`, '')
    ;
