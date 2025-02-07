Q_PALLETS = """
SELECT  
    b.id,       
    B.ORDETRAB ID_OT, 
    B.CNUPALET NRO_PALLET, 
    b.CNUANDEN ANDEN, 
    b.CREFEREN PLU, 
    C.DARTIGDM DESCPLU,
    CANTUNOK UNIDADES_RECIBIDAS, 
    VLOSTOCK ||' (' ||(SELECT quccaman ||' x '||qcapaman FROM F054vlog a where creferen =b.CREFEREN and cvarlogi =VLOSTOCK) ||')' VL_STOCKEADA,
    (
    SELECT CASE CCNIVELE WHEN 1 THEN 'PICO (U)' WHEN 2 THEN 'PICO' ELSE 'COMPLETO' END FROM f054vlog v WHERE v.creferen=b.creferen AND v.cvarlogi=b.vlostock) tipopal,
    B.CANSTOCK CANT_STOCKEADA,to_char(B.FCREAREG, 'dd/mm/yyyy HH24:mi:ss') FEC_REVISION,
    VLPALLET ||' (' ||(SELECT quccaman ||' x '||qcapaman FROM F054vlog a where creferen =b.CREFEREN and cvarlogi =VLPALLET) ||')'  PALLETIZADO,
    VLREVISA  ||' (' ||(SELECT quccaman ||' x '||qcapaman FROM F054vlog a where creferen =b.CREFEREN and cvarlogi =VLREVISA) ||')' VL_BULTO,
    QVLREVIS CANT_BULTOS,
    decode (d.xxlegajo,'',b.cusuario ||' - N/D', d.xxlegajo ||' - '||D.DNOMBREU||' '||d.dapelli1) RECEPCIONISTA, 
    B.CENTRADA,
    B.CPROVEED || ' - ' || (select razonsocial from cdj_proveedor where codigo = B.CPROVEED) Proveedor     
FROM f559otre a 
JOIN f562potr B ON A.ORDETRAB = B.ORDETRAB 
JOIN F002arti_pll C ON b.creferen = c.creferen AND B.CCONSIGN = C.CCONSIGN 
LEFT JOIN F009USUA D ON B.CUSUARIO = D.CUSUARIO 
WHERE idpicabe= 1511958 AND ESACTIVO = 1
"""

###############################################################################################################################################################

Q_RECHAZOS = """
SELECT R.ID id,
    R.ID_CABECERA idCabecera,
    R.PLU plu,
    A.DARTICUL descPlu,
    R.OC oc,
    R.CODIGO_PROVEEDOR codigoProveedor, 
    P.DRAZSOCI descProveedor,
    R.UNIDAD_MEDIDA unidadMedida,
    R.CANTIDAD_ENTREGADA cantidadEntregada,
    R.CANTIDAD_RECHAZADA cantidadRechazada,
    R.OBSERVACIONES observaciones,
    R.ID_MOTIVO_RECHAZO idMotivo,
    M.DESCRIPCION descMotivo,
    R.LEGAJO_INSPECTOR legajoInspector,
    (SELECT NOMBRE FROM ACTIVE_EMPLOYEE WHERE LEGAJO = LPAD(R.LEGAJO_INSPECTOR,8,'0')) inspector, 
    R.VL vl,
    R.CORTE corte
FROM REC_RECHAZO_REF R INNER JOIN F002ARTI A ON R.PLU = A.CREFEREN
INNER JOIN F041PROV P ON R.CODIGO_PROVEEDOR = P.CPROVEED
INNER JOIN REC_MOTIVO_RECHAZO M ON R.ID_MOTIVO_RECHAZO = M.ID

"""
# WHERE ID_CABECERA = #{idCab}
###############################################################################################################################################################

Q_RETRABAJOS = """
SELECT
    f787.centrada oc, 
    f787.calbaran remito,
    (SELECT descmovi FROM f785movi WHERE cempresa = f787.cempresa AND calmacen = f787.calmacen AND codimovi = f787.ctiptrab) descripcionRetrabajo,
    f787.qcantida cantidad, 
    f787.cproclie codProveedor, 
    (SELECT drazsoci FROM f041prov WHERE cempresa = f787.cempresa AND cconsign = f787.cconsign AND cproveed = f787.cproclie)  proveedor,
    TO_CHAR(f787.fentrada,'DD/MM/YYYY') fechaEntrada, 
    f787.remito remitoGdm, 
    f787.costo, 
    DECODE(f787.fechproc,'0','S/PROCESAR',f787.fechproc) fechaProcesamientoGdm
FROM  f787lfac f787, f068calb f068
WHERE f787.cempresa = '1'
AND   f787.calmacen = '93'
AND   f068.cempresa = f787.cempresa
AND   f068.calmacen = f787.calmacen
AND   f068.centrada = f787.centrada
AND   f068.calbaran = f787.calbaran
AND   f068.dproclie = f787.cproclie
AND   f068.ccnsgent = f787.cconsign
AND (F787.CALBARAN, F787.CENTRADA) IN (SELECT REMITO_PROVEEDOR, ORDEN_DE_COMPRA FROM WFADMIN.VW_REMITOS_COTO_PROVEEDOR a WHERE NRO_PI =  1511958)
union
SELECT
    f787.centrada oc, 
    f787.calbaran remito,
    (SELECT descmovi FROM f785movi WHERE cempresa = f787.cempresa AND calmacen = f787.calmacen AND codimovi = f787.ctiptrab) descripcion_retrabajo,
    f787.qcantida cantidad, 
    f787.cproclie cod_proveedor, 
    (SELECT drazsoci FROM f041prov WHERE cempresa = f787.cempresa AND cconsign = f787.cconsign AND cproveed = f787.cproclie)  proveedor,
    TO_CHAR(f787.fentrada,'DD/MM/YYYY') fecha, 
    f787.remito remito_gdm, 
    f787.costo, 
    DECODE(f787.fechproc,'0','S/PROCESAR',f787.fechproc) fecha_procesamiento_gdm
FROM  f787lfac f787, f068calb_hist f068
WHERE f787.cempresa = '1'
AND   f787.calmacen = '93'
AND   f068.cempresa = f787.cempresa
AND   f068.calmacen = f787.calmacen
AND   f068.centrada = f787.centrada
AND   f068.calbaran = f787.calbaran
AND   f068.dproclie = f787.cproclie
AND   f068.ccnsgent = f787.cconsign
AND (F787.CALBARAN, F787.CENTRADA) IN (SELECT REMITO_PROVEEDOR, ORDEN_DE_COMPRA FROM WFADMIN.VW_REMITOS_COTO_PROVEEDOR a WHERE NRO_PI =  1511958)
"""
###############################################################################################################################################################

Q_REMITOS = """
SELECT SUBSTR(lpad(a.ordetrab,12,'0'),0,4)||'-'||SUBSTR(lpad(a.ordetrab,12,'0'),5,12) remito_coto, 
    E.CPROVEED ||' - '||E.DRAZSOCI proveedor, F.DESCRIPCION tipoMercaderia,
    B.NUM_ORDEN oc, SUBSTR(C.REMITO,0,4)||'-'||SUBSTR(C.REMITO,5,12) remito_proveedor, 
    C.LINEAS cantidad_lineas, C.BULTOS cantidad_bultos 
FROM f559otre a, rec_pi_orden_compra b, rec_orden_remito c, F052menc d, F041PROV E 
LEFT JOIN rec_desc_proveedor F ON  F.CODIGO_WF = E.CPROVEED 
WHERE A.IDPICABE = B.ID_CABECERA 
AND B.ID = C.ID_ORDEN_COMPRA 
AND A.CEMPRESA = D.CEMPRESA 
AND A.CALMACEN = D.CCENTDIS 
AND B.NUM_ORDEN = D.CENTRADA 
AND D.CPROCLIE = E.CPROVEED 
AND D.CEMPRESA = E.CEMPRESA 
AND A.IDPICABE = 1511958
order by E.CPROVEED ||' - '||E.DRAZSOCI, B.NUM_ORDEN, C.BULTOS
"""

###############################################################################################################################################################

Q_MATERIALES = """
SELECT 
    B.CCODIGOM CODIGO,
    c.ddescoma MATERIAL, 
    B.QESTIMAD CANT_ESTIMADA, 
    B.QRECIBID CANT_RECIBIDA, 
    NVL(d.cdescrip,'ACEPTADO') motivo, 
    b.idnoacep idMotivo, 
    b.f_modif_mot fechaRech,
    b.cantidrf cantidrf 
    FROM F566mapa b JOIN f621coma  c ON  B.CCODIGOM = C.CCODIGOM LEFT JOIN f597mrma d ON B.IDNOACEP = d.idmotivo  
    WHERE b.idpaf562 = :idPallet 
"""

###############################################################################################################################################################

Q_PALLETS_HIST = """
SELECT 
    TO_CHAR(a.fcreareg,'DD/MM/YYYY HH24:MI:SS') fecha, 
    a.cdescrip movimiento, 
    a.qcantida cantidad, 
    a.creferen PLU, 
    a.czonaori||a.cubiorig ubicacion_origen, a.czonades||a.cubidest ubicacion_destino, 
    a.copecrea usuario, 
    AE.NOMBRE nombre 
FROM 
    f132hist_hist a 
    left join wf_active_employee ae on lpad(a.copecrea,8,'0') = AE.LEGAJO
WHERE 
    cempresa='1' and calmacen = '93' 
AND cnupalet = 1520098
AND fcreareg >= TO_DATE(SYSDATE-30,'DD/MM/YYYY HH24:MI:SS')

UNION
SELECT 
    TO_CHAR(b.fcreareg,'DD/MM/YYYY HH24:MI:SS') fecha, 
    b.cdescrip movimiento, 
    b.qcantida cantidad, 
    b.creferen PLU, 
    b.czonaori||b.cubiorig ubicacion_origen, 
    b.czonades||b.cubidest ubicacion_destino, 
    b.copecrea usuario, 
    AE2.NOMBRE 

FROM f132hist b  
LEFT JOIN wf_active_employee ae2 ON lpad(b.copecrea,8,'0') = AE2.LEGAJO
WHERE cempresa='1' and calmacen = '93'
AND cnupalet = 1520098
AND fcreareg >= TO_DATE(SYSDATE-30,'DD/MM/YYYY HH24:MI:SS')
ORDER BY 1
"""

Q_FLUJO = """
SELECT 
    ID_tipopi,
    CAB.ID PI,
    TIP.DESCRIPCION PI_DESC, 
    MOV.ID_ESTADO,
    EST.DESCRIPCION ESTADO, 
    MOV.STAMP FECHA, 
    ROW_NUMBER() OVER (PARTITION BY CAB.ID ORDER BY MOV.STAMP) AS ORDEN
FROM pi_movimiento MOV
INNER JOIN pi_cabecera CAB ON CAB.ID=ID_CABECERA
INNER JOIN pi_tipo TIP ON TIP.ID =ID_tipopi
INNER JOIN cdj_estado EST ON EST.ID=MOV.ID_ESTADO
WHERE TRUNC(MOV.stamp) > TO_DATE('01/01/2024','dd/mm/yyyy')
AND ID_tipopi IN (2,3)
ORDER BY CAB.ID,MOV.STAMP

"""




Q_AGENDA_PI = """
SELECT 
    AGENDA.*,
    PI_TURNO.ID_PI

FROM 

(SELECT 
    CEMPRESA AS EMPRESA,
    CALMACEN AS ALMACEN,
    CDIVISIO AS DIVISION,
    CNUTURNO AS TURNO,
    NDIAAGEN AS FECHA_TURNO_ASIGNADO,
    NHORAGEN AS HORA_TURNO_ASIGNADO,
    HENTRSEG AS HORA_ENTRADA,
    HENTDARS AS HORA_DARSENA,
    HSALISEG AS HORA_SALIDA,
    XTIPODOC AS TIPO_DOCUMENTO_CHOFER,
    DOCUCHOF AS DOCUMENTO_CHOFER,
    NPATENTE AS PATENTE_CAMION,
    ANDENENT AS ANDEN_ENTRADA,
    QCANTPAL AS CANTIDAD_PALLETS,
    QCANTBUL AS CANTIDAD_BULTOS,
    QCANTREF AS CANTIDAD_DE_QUE

FROM a010agen
) AGENDA
LEFT JOIN 
(
SELECT
    ID_PI,
    ID_DIVISION AS DIVISION,
    NUMERO_TURNO AS TURNO,
    FECHA_TURNO AS FECHA_TURNO_ASIGNADO
FROM PI_INTAGENDA
) PI_TURNO

ON AGENDA.TURNO = PI_TURNO.TURNO
AND AGENDA.FECHA_TURNO_ASIGNADO = PI_TURNO.FECHA_TURNO_ASIGNADO
WHERE PI_TURNO.ID_PI = 1407774

"""