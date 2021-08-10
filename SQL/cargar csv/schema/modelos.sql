SET GLOBAL local_infile = 1;
USE pruebaperu;
LOAD DATA LOCAL INFILE "D:\\Basededatos\\schema\\models.csv" INTO TABLE pruebaperu.modelos
FIELDS TERMINATED BY ";"
ENCLOSED BY '"'
LINES TERMINATED BY "\r\n"
IGNORE 1 LINES
(`modelo_id`,
`marca_id`,
`linea_de_produccion`,
`nombre_modelo`,
`tipo_id`,
`clasificacion_id`,
`carroceria_id`
)
SET	`modelo_id` = nullif(`modelo_id`, ''),
	`marca_id` = nullif(`marca_id`, ''),
    `linea_de_produccion` = nullif(`linea_de_produccion`, ''),
    `nombre_modelo` = nullif(`nombre_modelo`, ''),
    `tipo_id` = nullif(`tipo_id`, ''),
    `clasificacion_id` = nullif(`clasificacion_id`, ''),
    `carroceria_id` = nullif(`carroceria_id`, '')
    ;
