UNION SELECT `MERCADO`, `SEGMENTO.1`, `MARCA`,`MODELO`, `AÑO`, sum(`FLOTA 2019`) as 'CANTIDAD' from costarica.flotacostarica
UNION SELECT `MERCADO`, `SEGMENTO.1`, `MARCA`,`MODELO`, `AÑO`, sum(`FLOTA 2019`) as 'CANTIDAD' from elsalvador.flotaelsalvador
UNION SELECT `MERCADO`, `SEGMENTO.1`, `MARCA`,`MODELO`, `AÑO`, sum(`FLOTA 2019`) as 'CANTIDAD' from guatemala.flotaguatemala
UNION SELECT `MERCADO`, `SEGMENTO.1`, `MARCA`,`MODELO`, `AÑO`, sum(`FLOTA 2019`) as 'CANTIDAD' from honduras.flotahonduras
GROUP BY MERCADO, `SEGMENTO.1`, `MARCA`, `MODELO`, `AÑO`
order by CANTIDAD DESC;
;