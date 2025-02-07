select 
    f078.cempresa id_empresa,  
    f078.calmacen id_almacen, 
    0 id_zona, 
    0 id_pasillo, 
    f078.czonpule id_ubicacion,
    f079.creferen id_producto, 
    f079.cvarlogi variable_logistica,
    f078.cnupalet id_pallet, 
    case
        when f079.cvarlogi between 'A' and 'Z' then
            sum(f079.qenpalet * f054.qcantdep)
        when f079.cvarlogi between '1' and '9' then
            sum(f079.qenpalet)
    end bultos,
    sum(f079.qpesobru) kilos,
    sum(f079.qenpalet * f209.qcoeconv) unidades, 
    NULL fecha_vencimiento, 
    NULL id_dia_ingreso_pallet, 
    f002.cconsign id_consignatario,
    case when nvl(estado,0) = 0 then 0 else id end id_motivo_bloqueo,
    case when nvl(estado,0) = 0 then 0 else 1 end  pallet_bloqueado    
from f078cpen f078
left join f079lpen f079 on f078.cempresa = f079.cempresa and f078.calmacen = f079.calmacen and f078.cnupalet = f079.cnupalet
left join f002arti f002 on f079.cempresa = f002.cempresa and f079.creferen = f002.creferen
left join f054vlog f054 on f079.cempresa = f054.cempresa and f079.creferen = f054.creferen and f079.cvarlogi = f054.cvarlogi
left join f209conv f209 on f079.cempresa = f209.cempresa and f079.creferen = f209.creferen and f079.cvarlogi = f209.cvarlogi
left join WFADMIN.MOTIVOS_BLOQUEO bloq on f078.cnupalet = BLOQ.CNUPALET
where 
     f209.cvarlodp = '0'
and f079.csitlpal in ('PL','PG') 
group by f078.cempresa,f078.cnupalet, f079.creferen, f079.cvarlogi, f002.cinducon, f078.calmacen, f078.czonpule,
f002.cconsign,
    BLOQ.ESTADO, bloq.id
