SELECT `MERCADO`, COUNT(`MERCADO`) from chile.flotachile
UNION SELECT `MERCADO`, COUNT(`MERCADO`) from costarica.flotacostarica
UNION SELECT `MERCADO`, COUNT(`MERCADO`) from elsalvador.flotaelsalvador
UNION SELECT `MERCADO`, COUNT(`MERCADO`) from guatemala.flotaguatemala
UNION SELECT `MERCADO`, COUNT(`MERCADO`) from honduras.flotahonduras
UNION SELECT `MERCADO`, COUNT(`MERCADO`) from paraguay.flotaparaguay
UNION SELECT `MERCADO`, COUNT(`MERCADO`) from ecuador.flotaecuador
;