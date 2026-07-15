**MENU LISTADO**
DO WHILE .T.
  CLEAR
  @1,1 TO 22,78 DOUBLE
  @4,30 SAY 'LISTADO DE CLIENTES'
  @3,28 TO 5,50
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
@2,2 CLEAR TO 21,77
@3,3 SAY 'Cod'
@3,7 SAY 'Apellido'
@3,24 SAY 'Nombre'
@3,41 SAY 'Direccion'
@3,59 SAY 'Cod. Post.'
@3,72 SAY 'Saldo'
@4,2 to 4,77
STORE 5 TO linea
DO WHILE cod >= cod_des .AND. cod <= cod_has
    @linea,2 SAY cod
    @linea,7 SAY apel
    @linea,24 SAY nom
    @linea,41 SAY dir
    @linea,63 SAY c_p
    @linea,70 SAY saldo
    linea = linea + 1
    SKIP
    IF linea > 20
        @23,25 SAY 'Pulse una tecla para continuar.'
        WAIT
        @23,0
        STORE 5 TO linea
        @5,2 CLEAR TO 21,77
        LOOP
    ENDIF
    IF EOF() .OR. cod > cod_has
        @23,24 SAY 'Pulse una tecla para finalizar'
        WAIT
        CLEAR
        EXIT
    ENDIF
ENDDO
ENDDO
RETURN