    SELECT  DSSADMIN.SENT_MAIL_TEST(trunc(sysdate), 
                                    '[TST] Registros para el dia ' || trunc(sysdate) ||
                                      ' = ' || (SELECT COUNT(1) FROM BT_INVENTARIO_WF WHERE ID_DIA = TRUNC(SYSDATE)),
                                    'jbianculli@coto.com.ar',
                                    'Modulo de Inventario'
                                    ) mail
     FROM DUAL
     
    
    