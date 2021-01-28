res     db  0;
vector  db  02, 04, 05, 01, 02, 06, 07, 09  ;La suma de este vector debe ser 9
fin     db  1;

.inicio
      LDAA  0x00   ;Asignar cero al acumulador A
      LDAB  0xFF   ;Asignar cero al acumulador A
      LDX   #(vector)  ;Este sera el apuntador y se le metera la direccion inicial
.rutina
      XPAR        ;Compara el contenido que apunta X, si c=1 es impar si c = 0 es par
      BLO   3
      JMP   .par     ;Este ira a la rutina
      ADDA  0,X     ;Suma de numero impar y guardo en ACCA
      INX           ;Incrementa el apuntador
      CPX   #(fin)  ;fin del vector
      BEQ   3       ;Si IX == #(fin) entonces .suma
      JMP   .rutina 
      JMP   .suma   ; Va a suma
.par    
      SUBB  0,X   ;Resta de numero par y guardo en ACCB
      INX   ;Incrementa el apuntador
      CPX   #(fin) ;Comparacion con fin de vector
      BEQ   3      ;Si IX == #(fin) entonces .suma
      JMP .rutina ;Si el apuntador no es igual al fin de la rutina z!=0 entonces regreso a .rutina
.suma
      XABA   ; Suma de ACCA + ACCB y se guarda en X
      JMP .inicio  ;Loop infinito
