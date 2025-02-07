select 
        trunc(sysdate) id_dia,
       a.cempresa id_empresa,  
       a.calmacen id_almacen,  
       a.czonalma id_zona,  
       a.cpasillo id_pasillo, 
       a.chuecopa id_ubicacion,
       xtipsubi id_tipo_ubicacion,
       1 id_tipo_zona, 
       b.xtipubic id_tipo_rack,
       a.xsitubic id_estado_ubicacion,
       d.descripc desc_estado_ubicacion,
       h.cdivisio id_division_asignada, 
       f.cconsign id_consignatario,
       a.qpalaltu*a.qpalprof capacidad_ubicacion,
       a.CODINUTI ID_CODIGO_INUTILIZACION,   
       F670.FLAGINVET INVENTARIABLE,
       nvl(G.TIPO_ZONA,'0') id_tipo_acopio
       
from F005UBIA a

inner join f605rufl b on a.czonalma = b.czonalma and a.cpasillo = b.cpasillo and a.chuecopa = b.chuecopa
inner join f680mtub c on b.xtipubic = c.xtipubic
inner join F681MEUB d on d.xsitubic = a.xsitubic
left join f001zoal g on g.czonalma = a.czonalma and g.cempresa = a.cempresa
left join F720DIZO h on h.cempresa = g.cempresa and h.calmacen = g.calmacen and h.czonalma = g.czonalma
left join f802divi i on i.cempresa = h.cempresa and i.cdivisio = h.cdivisio
left join F007UBAR e on a.czonalma = e.czonalma and a.cpasillo = e.cpasillo and a.chuecopa = e.chuecopa
left join f002arti f on f.creferen = e.creferen
left join F670MMIH f670 on f670.CODINUTI = A.CODINUTI

WHERE a.xsitubic||a.CODINUTI <> 'I3'
  and a.cempresa = '1' 
  and a.calmacen = '93'