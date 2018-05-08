#include<stdio.h>

int main(){
	int ulang;
	int array_gaji[1000];
	int i=0;
	int a;
	
	do{
	//system("pause");
	int gaji,a;
	
	printf("ketentuan\n");
	for (a=0; a<5; a++){
		printf("gaji: ");
		scanf("%d", &array_gaji[a]);
	}
	
	printf("ingin ulang?");
	scanf("%d",&ulang);
	system("cls");
	}
	while (ulang==1);
	system("cls");
	for (a=0; a<5; a++){
		print(" gaji yang sudah ada: %d", array_gaji[a]);
	}
	printf("danke");
	return 0;
}
