CREATE VIEW `combinaciones` AS
SELECT `MERCADO`, `SEGMENTO.1`, `MARCA`,`MODELO`,`MODELO/VERSION`,`AÑO`,`CANTIDAD` from chile.combinacioneschile
UNION ALL SELECT `MERCADO`, `SEGMENTO.1`, `MARCA`,`MODELO`,`MODELO/VERSION`,`AÑO`,`CANTIDAD` from costarica.combinacionescostarica
UNION ALL SELECT `MERCADO`, `SEGMENTO.1`, `MARCA`,`MODELO`,`MODELO/VERSION`,`AÑO`,`CANTIDAD` from ecuador.combinacionesecuador
UNION ALL SELECT `MERCADO`, `SEGMENTO.1`, `MARCA`,`MODELO`,`MODELO/VERSION`,`AÑO`,`CANTIDAD` from elsalvador.combinacioneselsalvador
UNION ALL SELECT `MERCADO`, `SEGMENTO.1`, `MARCA`,`MODELO`,`MODELO/VERSION`,`AÑO`,`CANTIDAD` from guatemala.combinacionesguatemala
UNION ALL SELECT `MERCADO`, `SEGMENTO.1`, `MARCA`,`MODELO`,`MODELO/VERSION`,`AÑO`,`CANTIDAD` from honduras.combinacioneshonduras
UNION ALL SELECT `MERCADO`, `SEGMENTO.1`, `MARCA`,`MODELO`,`MODELO/VERSION`,`AÑO`,`CANTIDAD` from panama.combinacionespanama
UNION ALL SELECT `MERCADO`, `SEGMENTO.1`, `MARCA`,`MODELO`,`MODELO/VERSION`,`AÑO`,`CANTIDAD` from paraguay.combinacionesparaguay;