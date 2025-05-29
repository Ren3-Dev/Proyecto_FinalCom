%{
#include "parser.tab.h"
#include <stdio.h>
%}

DIGITO      [0-9]
LETRA       [a-zA-Z]
ID          {LETRA}({LETRA}|{DIGITO})*
NUMERO      {DIGITO}+

%%

"MAIN"              return MAIN;
"DEC"               return DEC;
"INPUT"             return INPUT;
"OUTPUT"            return OUTPUT;
"IF"                return IF;
"ELSE"              return ELSE;

"=="                return IGUAL;
"<>"                return DIFERENTE;
"<="                return MENORIGUAL;
">="                return MAYORIGUAL;
"<"                 return MENOR;
">"                 return MAYOR;

"&&"                return AND;
"||"                return OR;

"="                 return ASIGNACION;
";"                 return PUNTOCOMA;
","                 return COMA;
"("                 return PARIZQ;
")"                 return PARDER;
"{"                 return LLAVEIZQ;
"}"                 return LLAVEDER;

"+"                 return SUMA;
"-"                 return RESTA;
"*"                 return MULT;
"/"                 return DIV;

{ID}                { yylval.str = strdup(yytext); return ID; }
{NUMERO}            { yylval.str = strdup(yytext); return NUMERO; }

"/*"([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*"*"+"/"   ; // comentario bloque

[ \t\r\n]+          ; // ignorar espacios

.                   printf("Caracter no reconocido: %s\n", yytext);

%%

int yywrap() {
    return 1;
}



