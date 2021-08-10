SET GLOBAL local_infile = 1;
USE pruebaperu;
LOAD DATA LOCAL INFILE "D:\\Basededatos\\schema\\brands.csv" INTO TABLE pruebaperu.marcas
FIELDS TERMINATED BY ";"
ENCLOSED BY '"'
LINES TERMINATED BY "\r\n"
IGNORE 1 LINES
(`nombre_marca`,
`marca_id`
)
SET	`nombre_marca` = nullif(`nombre_marca`, ''),
	`marca_id` = nullif(`marca_id`, '')
    ;
