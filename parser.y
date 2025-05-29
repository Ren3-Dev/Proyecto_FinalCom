%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int tempCount = 0;
int labelCount = 0;

char* newTemp() {
    char* t = malloc(10);
    sprintf(t, "t%d", tempCount++);
    return t;
}

char* newLabel() {
    char* l = malloc(10);
    sprintf(l, "l%d", labelCount++);
    return l;
}

void yyerror(const char* s) {
    fprintf(stderr, "Error: %s\n", s);
}
extern int yylex();
%}

%union {
    char* str;
}

%token <str> ID NUMERO
%token MAIN DEC INPUT OUTPUT IF ELSE
%token IGUAL DIFERENTE MENORIGUAL MAYORIGUAL MENOR MAYOR
%token AND OR
%token ASIGNACION PUNTOCOMA COMA PARIZQ PARDER LLAVEIZQ LLAVEDER
%token SUMA RESTA MULT DIV

%type <str> expresion termino factor lista_ids condicion comparacion

%start programa

%%

programa:
    MAIN LLAVEIZQ bloque LLAVEDER
;

bloque:
    sentencia
  | bloque sentencia
;

sentencia:
    DEC lista_ids PUNTOCOMA
  | INPUT ID PUNTOCOMA    { printf("call input;\npop %s;\n", $2); }
  | OUTPUT ID PUNTOCOMA   { printf("push %s;\ncall output;\n", $2); }
  | ID ASIGNACION expresion PUNTOCOMA { printf("%s = %s;\n", $1, $3); }
  | IF PARIZQ condicion PARDER LLAVEIZQ bloque LLAVEDER
    ELSE LLAVEIZQ bloque LLAVEDER {
        char* l1 = newLabel();
        char* l2 = newLabel();
        printf("ifZ %s goto %s;\n", $3, l1);
        printf("goto %s;\n", l2);
        printf("%s:\n", l1);
        printf("%s:\n", l2);
    }
;

lista_ids:
    ID                    { printf("// Declaración: %s\n", $1); }
  | ID COMA lista_ids     { printf("// Declaración: %s\n", $1); }
;

expresion:
    expresion SUMA termino {
        char* t = newTemp();
        printf("%s = %s + %s;\n", t, $1, $3);
        $$ = t;
    }
  | expresion RESTA termino {
        char* t = newTemp();
        printf("%s = %s - %s;\n", t, $1, $3);
        $$ = t;
    }
  | termino { $$ = $1; }
;

termino:
    termino MULT factor {
        char* t = newTemp();
        printf("%s = %s * %s;\n", t, $1, $3);
        $$ = t;
    }
  | termino DIV factor {
        char* t = newTemp();
        printf("%s = %s / %s;\n", t, $1, $3);
        $$ = t;
    }
  | factor { $$ = $1; }
;

factor:
    PARIZQ expresion PARDER { $$ = $2; }
  | ID { $$ = $1; }
  | NUMERO { $$ = $1; }
;

condicion:
    comparacion                  { $$ = $1; }
  | condicion AND comparacion    {
        char* t = newTemp();
        printf("%s = %s && %s;\n", t, $1, $3);
        $$ = t;
    }
  | condicion OR comparacion     {
        char* t = newTemp();
        printf("%s = %s || %s;\n", t, $1, $3);
        $$ = t;
    }
;

comparacion:
    expresion IGUAL expresion {
        char* t = newTemp();
        printf("%s = %s == %s;\n", t, $1, $3);
        $$ = t;
    }
  | expresion DIFERENTE expresion {
        char* t = newTemp();
        printf("%s = %s <> %s;\n", t, $1, $3);
        $$ = t;
    }
  | expresion MENOR expresion {
        char* t = newTemp();
        printf("%s = %s < %s;\n", t, $1, $3);
        $$ = t;
    }
  | expresion MAYOR expresion {
        char* t = newTemp();
        printf("%s = %s > %s;\n", t, $1, $3);
        $$ = t;
    }
  | expresion MENORIGUAL expresion {
        char* t = newTemp();
        printf("%s = %s <= %s;\n", t, $1, $3);
        $$ = t;
    }
  | expresion MAYORIGUAL expresion {
        char* t = newTemp();
        printf("%s = %s >= %s;\n", t, $1, $3);
        $$ = t;
    }
;

%%


