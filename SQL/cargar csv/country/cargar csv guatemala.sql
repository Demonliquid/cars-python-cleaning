SET GLOBAL local_infile = 1;
USE guatemala;
LOAD DATA LOCAL INFILE "D:\\Basededatos\\Limpioparaunir\\guatemala.csv" INTO TABLE guatemala.flotaguatemala
FIELDS TERMINATED BY ","
ENCLOSED BY '"'
LINES TERMINATED BY "\n"
IGNORE 1 LINES
(`MERCADO`,
`SEGMENTO.1`,
`MARCA`,
`MGEN`,
`MODELO`,
`MODELO/VERSION`,
`VERSION (SALES DESCRIPTION)`,
`AÑO`,
`MOTOR`,
`FLOTA 2019`,
`PROVINCIA`,
`LOCALIDAD`
)
SET	`MERCADO` = nullif(`MERCADO`, ''),
	`SEGMENTO.1` = nullif(`SEGMENTO.1`, ''),
    `MARCA` = nullif(`MARCA`, ''),
    `MGEN` = nullif(`MGEN`, ''),
    `MODELO` = nullif(`MODELO`, ''),
    `MODELO/VERSION` = nullif(`MODELO/VERSION`, ''),
    `VERSION (SALES DESCRIPTION)` = nullif(`VERSION (SALES DESCRIPTION)`, ''),
    `AÑO` = nullif(`AÑO`, ''),
    `MOTOR` = nullif(`MOTOR`, ''),
    `FLOTA 2019` = nullif(`FLOTA 2019`, ''),
    `PROVINCIA` = nullif(`PROVINCIA`, ''),
    `LOCALIDAD` = nullif(`LOCALIDAD`, '')
    ;
