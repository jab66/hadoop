select 
    f080.cEMPRESA id_empresa, 
    f080.calmacen id_almacen, 
    0 id_zona, 
    0 id_pasillo, 
    f080.czonaexp id_ubicacion,  
    f081.crefepla id_producto, 
    f081.cvarlpla variable_logistica,
    f080.cnupalet id_pallet, 
    CASE
        WHEN f081.cvarlpla between 'A' and 'Z' then
            SUM(f081.qcantida * f054.qcantdep)
        WHEN f081.cvarlpla between '1' and '9' then
            SUM(f081.qcantida)
    END bultos,
    SUM(f081.qpesobru) kilos,
    SUM(f081.qcantida * f209.qcoeconv) unidades,
    NULL fecha_vencimiento, 
    NULL id_dia_ingreso_pallet, 
    f002.cconsign id_consignatario,
    case when nvl(estado,0) = 0 then 0 else id end id_motivo_bloqueo,
    case when nvl(estado,0) = 0 then 0 else 1 end  pallet_bloqueado      
FROM f080cpsa f080
left join f081lpsa f081 on f080.cempresa = f081.cempresa AND f080.calmacen = f081.calmacen AND f080.cnupalet = f081.cnupalet
left join f002arti f002 on f081.cempresa = f002.cempresa AND f081.crefepla = f002.creferen 
left join f054vlog f054 on f081.cempresa = f054.cempresa AND f081.crefepla = f054.creferen AND f081.cvarlpla = f054.cvarlogi
left join f209conv f209 on f081.cempresa = f209.cempresa AND f081.crefepla = f209.creferen AND f081.cvarlpla = f209.cvarlogi
left join WFADMIN.MOTIVOS_BLOQUEO bloq on f080.cnupalet = BLOQ.CNUPALET
WHERE 
    f209.cvarlodp = '0'
AND f080.csitpals <> 'FI'
GROUP BY f080.cEMPRESA, f080.calmacen, f080.cnupalet, f081.crefepla,
 f081.cvarlpla, f002.cinducon, f080.czonaexp, f002.cconsign,
    BLOQ.ESTADO, bloq.id
    