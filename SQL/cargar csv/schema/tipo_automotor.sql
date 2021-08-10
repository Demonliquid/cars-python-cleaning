SET GLOBAL local_infile = 1;
USE pruebaperu;
LOAD DATA LOCAL INFILE "D:\\Basededatos\\schema\\vehicle_types.csv" INTO TABLE pruebaperu.tipo_vehiculos
FIELDS TERMINATED BY ";"
ENCLOSED BY '"'
LINES TERMINATED BY "\r\n"
IGNORE 1 LINES
(`tipo_nombre`,
`tipo_id`
)
SET	`tipo_nombre` = nullif(`tipo_nombre`, ''),
	`tipo_id` = nullif(`tipo_id`, '')
    ;
