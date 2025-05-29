Poyecto_FinalCom: lexer.l parser.y main.c
	bison -d parser.y
	flex lexer.l
	gcc parser.tab.c lex.yy.c main.c -o Poyecto_FinalCom

clean:
	rm -f parser.tab.* lex.yy.c Poyecto_FinalCom
