CREATE VIEW diccionariomodelos AS
    SELECT 
        modelos.modelo_id,
        modelos.linea_de_produccion,
        modelos.nombre_modelo,
        marcas.nombre_marca,
        tipo_vehiculos.tipo_nombre,
        clasificaciones.nombre_clasificacion,
        carrocerias.nombre_carroceria
    FROM
        modelos
            LEFT JOIN
        marcas ON modelos.marca_id = marcas.marca_id
            LEFT JOIN
        tipo_vehiculos ON modelos.tipo_id = tipo_vehiculos.tipo_id
            LEFT JOIN
        clasificaciones ON modelos.clasificacion_id = clasificaciones.clasificacion_id
            LEFT JOIN
        carrocerias ON modelos.carroceria_id = carrocerias.carroceria_id;