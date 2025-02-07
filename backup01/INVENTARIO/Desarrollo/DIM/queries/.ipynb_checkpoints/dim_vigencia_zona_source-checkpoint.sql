SELECT distinct nvl(estado,-1) id_vigencia_zona,
    case when estado = 'NVG' THEN 'No Vigente'
         when estado = 'VIG' THEN 'Vigente'
         else 'No Configurada' end desc_vigencia_zona
    FROM F001ZOAL
 order by 1 desc
 
