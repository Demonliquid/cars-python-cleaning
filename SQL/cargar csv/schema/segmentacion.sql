SET GLOBAL local_infile = 1;
USE pruebaperu;
LOAD DATA LOCAL INFILE "D:\\Basededatos\\schema\\classif.csv" INTO TABLE pruebaperu.clasificaciones
FIELDS TERMINATED BY ";"
ENCLOSED BY '"'
LINES TERMINATED BY "\r\n"
IGNORE 1 LINES
(`nombre_clasificacion`,
`clasificacion_id`
)
SET	`nombre_clasificacion` = nullif(`nombre_clasificacion`, ''),
	`clasificacion_id` = nullif(`clasificacion_id`, '')
    ;
