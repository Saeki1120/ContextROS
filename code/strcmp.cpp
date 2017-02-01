#include <stdio.h>
#include <string.h>
#include <string>
/*
int get_layer_num(char *l_name){
	if (strcmp("indoor", l_name) == 0){
		return 0;
	} else if (strcmp("outdoor", l_name) == 0){
		return 1;
	}
    return -1;
}
*/
int get_layer_num(std::string layer_name){
if (layer_name == "indoor") {return 0;}
else if (layer_name == "outdoor") {return 1;}
else if (layer_name == "middoor") {return 2;}
return -1;
}


int get_layer_num2(std::string l_name){
    char l[10];
    if (strcmp("indoor", l) == 0){
        return 0;
    } else if (strcmp("outdoor", l) == 0){
        return 1;
    }
    return -1;
}

int main(void)
{
    char str[] = "ABC";
    char str1[] = "ABC";
    char str2[] = "ABD";
    char str3[] = "B";
    char str4[] = "AAAA";
    char str5[] = "indoor";
    char str6[] = "outdoor";
    int l_num1;
    int l_num2=-1;
    int l_num3=-1;
    std::string st = "middoor";

    printf("strcmp(%s, %s) = %d\n", str, str1, strcmp(str, str1));
    printf("strcmp(%s, %s) = %d\n", str, str2, strcmp(str, str2));
    printf("strcmp(%s, %s) = %d\n", str, str3, strcmp(str, str3));
    printf("strcmp(%s, %s) = %d\n", str, str4, strcmp(str, str4));


    l_num1 = get_layer_num(st);
    //l_num2 = get_layer_num(str6);
    //l_num3 = get_layer_num(str);

    printf("%d, %d, %d\n", l_num1, l_num2, l_num3);
    return 0;
}
