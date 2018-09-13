#include <stdio.h>

int main(){
    FILE *inF;
    FILE *outF;

    inF = fopen("./commentReddit.txt", "r");
    outF = fopen("./ReducedFile.txt", "w");

    char buff[2];

    while(!feof(inF)){
        fgets(buff, 2, (FILE*)inF);
        if((buff[0] >= '0' && buff[0] <= '9') || (buff[0] >= 'A' && buff[0] <= 'Z') || (buff[0] >= 'a' && buff[0] <= 'z') || buff[0] == ' ' || buff[0] == '\n')
            fputc(buff[0], outF);
        else
            fputc(' ', outF);

        printf("%c",buff[0]);
    }
    fclose(inF);
    fclose(outF);
}