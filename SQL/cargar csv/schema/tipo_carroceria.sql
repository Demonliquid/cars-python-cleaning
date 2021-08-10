SET GLOBAL local_infile = 1;
USE pruebaperu;
LOAD DATA LOCAL INFILE "D:\\Basededatos\\schema\\car_body_styles.csv" INTO TABLE pruebaperu.carrocerias
FIELDS TERMINATED BY ";"
ENCLOSED BY '"'
LINES TERMINATED BY "\r\n"
IGNORE 1 LINES
(`nombre_carroceria`,
`carroceria_id`
)
SET	`nombre_carroceria` = nullif(`nombre_carroceria`, ''),
	`carroceria_id` = nullif(`carroceria_id`, '')
    ;
