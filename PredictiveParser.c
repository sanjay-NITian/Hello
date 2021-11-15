/*
The grammar in this program is:
E -> i / E*E / E+E / (E) / E^E
i for identifier.
E is the start symbol.
*/
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
char *input;
int i=0;
char lasthandle[6],stack[50],handles[][5]={")E(","E*E","E+E","i","E^E"};
//(E) becomes )E( when pushed to stack
int top=0,l;
char prec[9][9]={
 /*stack + - * / ^ i ( ) $ */
 /* + */ '>', '>','<','<','<','<','<','>','>',
 /* - */ '>', '>','<','<','<','<','<','>','>',
 /* * */ '>', '>','>','>','<','<','<','>','>',
 /* / */ '>', '>','>','>','<','<','<','>','>',
 /* ^ */ '>', '>','>','>','<','<','<','>','>',
 /* i */ '>', '>','>','>','>','e','e','>','>',
 /* ( */ '<', '<','<','<','<','<','<','>','e',
 /* ) */ '>', '>','>','>','>','e','e','>','>',
 /* $ */ '<', '<','<','<','<','<','<','<','>',
 };
int getindex(char c)
{
switch(c)
 {
 case '+':return 0;
 case '-':return 1;
 case '*':return 2;
 case '/':return 3;
 case '^':return 4;
 case 'i':return 5;
 case '(':return 6;
 case ')':return 7;
 case '$':return 8;
 }
}