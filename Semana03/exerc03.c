#include <stdio.h>
#include <stdlib.h>

void hanoi(int n,char ori,char dest,char aux){
	
	//Se tiver só um disco, mova ele
	if(n==1){
		printf("\nMova o disco 1 do eixo %c para o eixo %c",ori ,dest);
		return;
	}
	//Para mover o disco n-1 de A para B, usando C de auxiliar/
	hanoi(n-1,ori,aux,dest);
	//Para mover os outros discos de A para C
	printf("\nMova o disco %d do eixo %c para o eixo %c",n,ori,dest);
	//Para mover os n-1 discos de B para C usando A como auxiliar/
	hanoi(n-1,aux,dest,ori);
}

int main(){
	int n;
	printf("Digite a quantidade de discos : ");
	scanf("%d",&n);
	printf("Para resolver a torre de Hanoi faça :\n\n");
	hanoi(n,'A','C','B');
	printf("\n");
	return 0;
}
