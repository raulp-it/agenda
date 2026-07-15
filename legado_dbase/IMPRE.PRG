**MENU IMPRESION**
DO WHILE .T.
  CLEAR
  @1,1 TO 22,78 DOUBLE
  @4,30 SAY 'IMPRESION DE CLIENTES'
  @3,27 TO 5,51
  @21,2 SAY 'INGRESE EL CODIGO DESDE = (0 PARA SALIR)'
  STORE 0 TO cod_des, cod_has
  @8,20 SAY 'CODIGO DESDE:'GET COD_DES PICTURE '9999'
  READ
  IF COD_DES = 0
       EXIT
  ENDIF
  SEEK cod_des
  IF EOF()
       @15,15 SAY 'CODIGO DE CLIENTE INEXISTENTE...'
       @23,23
       WAIT 'PULSE UNA TECLA PARA CONTINUAR.'
       @23,0
       LOOP
  ENDIF
@21,2 SAY 'Ingrese codigo hasta = 0 para Terminar'
@8,50 say 'Codigo hasta: 'GET cod_has PICTURE '99999'
READ
IF cod_has < cod_des
    LOOP
ENDIF
@10,30 SAY 'Imprimiendo...'
SET DEVICE TO PRINT
@3,3 SAY 'Cod'
@3,7 SAY 'Apellido'
@3,24 SAY 'Nombre'
@3,41 SAY 'Direccion'
@3,59 SAY 'Cod. Post.'
@3,72 SAY 'Saldo'
STORE 5 TO linea
DO WHILE cod >= cod_des .AND. cod <= cod_has
    @linea,2 SAY cod
    @linea,7 SAY apel
    @linea,24 SAY nom
    @linea,41 SAY dir
    @linea,63 SAY c_p
    @linea,70 SAY saldo
    STORE linea + 1 TO linea
    SKIP
    IF linea = 60
        @3,3 SAY 'Cod'
        @3,7 SAY 'Apellido'
        @3,24 SAY 'Direccion'
        @3,59 SAY 'Cod.Postal'
        @3,72 SAY 'Saldo'
        STORE 5 TO linea
        LOOP
    ENDIF
ENNDO
SET DEVICE TO SCREEN
EJECT
ENDO
RETURN
        