SET GLOBAL local_infile = 1;
USE panama;
LOAD DATA LOCAL INFILE "D:\\Basededatos\\Limpioparaunir\\panamaconcesionaria.csv" INTO TABLE panama.panamaconcesionaria
FIELDS TERMINATED BY ","
ENCLOSED BY '"'
LINES TERMINATED BY "\n"
IGNORE 1 LINES
(`MERCADO`,
`MARCA`,
`MGEN`,
`MODELO`,
`MODELO/VERSION`,
`VERSION (SALES DESCRIPTION)`,
`PROVINCIA`,
`LOCALIDAD`,
`CILINDRADA`,
`CILINDROS`,
`TRACCION`,
`TRANSMISION`,
`FRENOS DISCO DELANTERO`,
`FRENOS DISCO TRASEROS`,
`AÑO`,
`COMBUSTIBLE`,
`MOTOR`,
`NUMERO CHASIS / VIN`,
`NUMERO MOTOR`,
`PATENTE`,
`FLOTA 2019`,
`ORIGEN`
)
SET	`MERCADO` = nullif(`MERCADO`, ''),
	`MARCA` = nullif(`MARCA`, ''),
    `MGEN` = nullif(`MGEN`, ''),
    `MODELO` = nullif(`MODELO`, ''),
    `MODELO/VERSION` = nullif(`MODELO/VERSION`, ''),
    `VERSION (SALES DESCRIPTION)` = nullif(`VERSION (SALES DESCRIPTION)`, ''),
    `PROVINCIA` = nullif(`PROVINCIA`, ''),
    `LOCALIDAD` = nullif(`LOCALIDAD`, ''),
    `CILINDRADA` = nullif(`CILINDRADA`, ''),
    `CILINDROS` = nullif(`CILINDROS`, ''),
    `TRACCION` = nullif(`TRACCION`, ''),
    `TRANSMISION` = nullif(`TRANSMISION`, ''),
    `FRENOS DISCO DELANTERO` = nullif(`FRENOS DISCO DELANTERO`, ''),
    `FRENOS DISCO TRASEROS` = nullif(`FRENOS DISCO TRASEROS`, ''),
    `TRANSMISION` = nullif(`TRANSMISION`, ''),
    `AÑO` = nullif(`AÑO`, ''),
    `COMBUSTIBLE` = nullif(`COMBUSTIBLE`, ''),
	`MOTOR` = nullif(`MOTOR`, ''),
    `NUMERO CHASIS / VIN` = nullif(`NUMERO CHASIS / VIN`, ''),
    `NUMERO MOTOR` = nullif(`NUMERO MOTOR`, ''),
    `PATENTE` = nullif(`PATENTE`, ''),
    `FLOTA 2019` = nullif(`FLOTA 2019`, ''),
    `ORIGEN` = nullif(`ORIGEN`, '')
    ;
