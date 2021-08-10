SET GLOBAL local_infile = 1;
USE pruebaperu;
LOAD DATA LOCAL INFILE "D:\\Basededatos\\schema\\bases\\peru\\flotaperu.csv" INTO TABLE pruebaperu.vehiculos
FIELDS TERMINATED BY ","
ENCLOSED BY '"'
LINES TERMINATED BY "\n"
IGNORE 1 LINES
(`vehiculo_id`,
`cantidad`,
`texto_original`,
`modelo_id`,
`version`,
`origen`,
`ano_fabricacion`,
`cantidad`
)
SET	`vehiculo_id` = nullif(`vehiculo_id`, ''),
	`cantidad` = nullif(`cantidad`, ''),
    `texto_original` = nullif(`texto_original`, ''),
    `modelo_id` = nullif(`modelo_id`, ''),
    `version` = nullif(`version`, ''),
    `origen` = nullif(`origen`, ''),
    `ano_fabricacion` = nullif(`ano_fabricacion`, ''),
    `cantidad` = nullif(`cantidad`, '')
    ;
