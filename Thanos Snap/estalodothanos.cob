IDENTIFICATION DIVISION.                                   
PROGRAM-ID. EXT7.                                           
DATA DIVISION.         
WORKING-STORAGE SECTION.

*> preparando a seed

01 WS-FIRST-TIME PIC 9(1) VALUE 0.
01 WS-RND-SEED-X PIC X(8).
01 WS-RND-SEED-9 REDEFINES WS-RND-SEED-X PIC 9(8).
01 WS-RND-DBL COMP-2.
01 MIN-NUMBER PIC 99 VALUE 1.                             
01 MAX-NUMBER PIC 99 VALUE 2.                             
01 RANDOM-NUMBER PIC 99.    
LINKAGE SECTION.
01 LS-MAX PIC X COMP-X.
01 LS-RESULT PIC X COMP-X.


PROCEDURE DIVISION.

*>Criando a seed pra recomeçar toda vez

if ws-first-time = 0
              move 32768 to ws-rnd-seed-9
              perform until ws-rnd-seed-9 < 32768
                 accept ws-rnd-seed-x from time
                 move function reverse(ws-rnd-seed-x) to ws-rnd-seed-x
                 compute ws-rnd-seed-9 = ws-rnd-seed-9 / 3060
              end-perform
              compute ws-rnd-dbl = function random(ws-rnd-seed-9)
              move 1 to ws-first-time
           end-if.

*>Loop

     PERFORM 50 TIMES                                       
         COMPUTE RANDOM-NUMBER = FUNCTION RANDOM *         
                            (MAX-NUMBER - MIN-NUMBER + 1) +
                             MIN-NUMBER                     
     END-PERFORM.  

*> If e else

     IF RANDOM-NUMBER = 1 THEN
        DISPLAY 'You were spared by Thanos.'
    ELSE
        DISPLAY 'You were slain by Thanos, for the good of the Universe.'
     END-IF
     
STOP RUN.      