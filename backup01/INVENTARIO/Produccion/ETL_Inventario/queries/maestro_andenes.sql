SELECT 

trunc(sysdate) id_dia,
a.cempresa id_empresa, 
a.calmacen id_almacen, 
0 id_zona, 
0 id_pasillo, 
a.cnuanden id_ubicacion,

CASE 
    WHEN a.ctipoand = 'P' THEN 2
    WHEN a.ctipoand = 'A' THEN 3
    WHEN a.ctipoand = 'I' THEN 4
    WHEN a.ctipoand = 'K' THEN 5
    WHEN a.ctipoand = 'C' THEN 6
END id_tipo_zona,

CASE 
    WHEN a.ctipoand = 'P' THEN 'PULMON'
    WHEN a.ctipoand = 'I' THEN 'INUTILIZADO'
    WHEN a.ctipoand = 'K' THEN 'PUNTERA DE RACK'
    WHEN a.ctipoand = 'A' THEN 'ANDEN'
    WHEN a.ctipoand = 'C' THEN 'CONTROL'
END desc_tipo_zona,

a.cdivisio id_division_asignada, 
'T' id_tipo_ubicacion, 

(SELECT wfadmin.estado_anden(a.cnuanden, a.cempresa, a.calmacen ) FROM DUAL) id_estado_ubicacion,
CASE 
WHEN
  (SELECT wfadmin.estado_anden(a.cnuanden, a.cempresa, a.calmacen ) FROM DUAL) = 'I' THEN 'Inutilizada'
WHEN
(SELECT wfadmin.estado_anden(a.cnuanden, a.cempresa, a.calmacen ) FROM DUAL) = 'L' THEN 'Libre'
WHEN
(SELECT wfadmin.estado_anden(a.cnuanden, a.cempresa, a.calmacen ) FROM DUAL) = 'O' THEN 'Ocupada'
END desc_estado_ubicacion,
'Z' id_tipo_rack
FROM f638mand a
LEFT JOIN f802divi b ON b.cempresa = a.cempresa AND b.cdivisio = a.cdivisio