#include <stdio.h>
#include <math.h>
#define PI 3.14159265

typedef struct {
  float real,imag;
} complexo;

typedef struct {
  float modulo,ang;
} polar;

complexo somacompl(complexo a,complexo b)
{
	complexo resulsoma;
	resulsoma.real = a.real + b.real;
	resulsoma.imag = a.imag + b.imag ;
	
	return(resulsoma);
}
complexo subtraicompl(complexo a,complexo b)
{
	complexo resulsubtr;
	resulsubtr.real = a.real - b.real;
	resulsubtr.imag = a.imag - b.imag;
	
	return(resulsubtr);
}
complexo multcompl(complexo a,complexo b)
{
	complexo resulmult;
	resulmult.real = a.real*b.real - a.imag*b.imag;
	resulmult.imag = a.real*b.imag + a.imag*b.real;
	
	return(resulmult);
}
complexo divcompl(complexo a,complexo b)
{
	complexo resuldiv;
	resuldiv.real = (a.real*b.real + a.imag*b.imag)/(b.real*b.real + b.imag*b.imag);
	resuldiv.imag =  (a.imag*b.real-a.real*b.imag)/(b.real*b.real + b.imag*b.imag);
	
	return(resuldiv);
}
polar polcompl(complexo a)
{
	polar resulpol;
	resulpol.modulo = sqrtf((a.real*a.real)+(a.imag*a.imag));
	resulpol.ang = (atan2f(a.real,a.imag))*(180/PI);
	return(resulpol);
}

int main() {
  
  int ope = 0, ind;
  complexo a,b,resulsoma,resulsubtr,resulmult,resuldiv,resulret;
  polar resulpol;

  printf("Digite a parte real e imaginaria do primeiro numero: ");
  scanf("%f %f", &a.real, &a.imag);

  printf("Digite a parte real e imaginaria do segundo numero: ");
  scanf("%f %f", &b.real, &b.imag);

  printf("Digite o numero correspondente à operação a ser realizada:\n");
  printf(" (1)Soma\n (2)Subtração\n (3)Multiplicação\n (4)Divisão\n (5)Forma Polar\n (6)Forma Retangular\n");
  scanf("%d", &ope);

if(ope == 1){
resulsoma = somacompl(a,b);
printf( "O resultado da soma é: Re(%f) Im(%f)\n", resulsoma.real, resulsoma.imag);
}
else if(ope == 2){
resulsubtr = subtraicompl(a,b);
printf( "O resultado da subtração é: Re(%f) Im(%f)\n", resulsubtr.real, resulsubtr.imag);
}
else if(ope == 3){
resulmult = multcompl(a,b);
printf( "O resultado da subtração é: Re(%f) Im(%f)\n", resulmult.real, resulmult.imag);
}
else if(ope == 4){
resuldiv = divcompl(a,b);
printf( "O resultado da subtração é: Re(%f) Im(%f)\n", resuldiv.real, resuldiv.imag);
}
else if(ope == 5){
 printf("Qual numero complexo você deseja passar para forma polar, (1) ou (2)? ");
 scanf("%d", &ind);
  if(ind == 1||2){
	 if(ind == 1){	
		resulpol = polcompl(a);
			}
	else if(ind == 2){
		resulpol = polcompl(b);
			} 
printf( "A forma polar desse numero complexo é: %f(cos%.2f + sen%.2f)\n", resulpol.modulo, resulpol.ang, resulpol.ang);
		}
	else{
	printf("Indice invalido!");
		}
}
else if(ope == 6){
 printf("Qual numero complexo você deseja passar para forma retangular, (1) ou (2)? ");
 scanf("%d", &ind);
  if(ind == 1||2){
	 if(ind == 1){	
		resulret = a;
			}
	else if(ind == 2){
		resulret = b;
			} 
if(resulret.imag >= 0){
printf( "A forma retangular desse numero complexo é: %f + %fi \n", resulret.real, resulret.imag);
}
else{
printf( "A forma retangular desse numero complexo é: %f %fi \n", resulret.real, resulret.imag);
}
}
		
	else{
	printf("Indice invalido!");
		}
}
}

