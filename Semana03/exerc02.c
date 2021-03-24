#include <stdio.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <stdlib.h>

#define TamBUFF 65536
#define MODO_CRIACAO S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH


int main(int argc, char *argv[]) {


    int fd1, fd2;
    char buffer[TamBUFF];
    int bytes_lidos;

    if(argc != 3){

      fprintf(stderr,"Uso: %s <arquivo> <novo-arquivo>\n",argv[0]);
      exit(-1);
    }

    if((fd1 = open(argv[1],O_RDONLY, S_IREAD))==-1){
        fprintf(stderr,"Erro: %s\n",strerror(errno));
        exit(-1);
    }
    if((fd2 = open(argv[2],O_WRONLY | O_TRUNC | O_CREAT, MODO_CRIACAO))==-1){
        fprintf(stderr,"Erro: %s\n",strerror(errno));
        exit(-1);
    }

    while((bytes_lidos=read(fd1,buffer,TamBUFF))!=0) 
         write(fd2,buffer,bytes_lidos);

    close(fd1);
    close(fd2);
    return(0);

} 
