#include <stdio.h>

#include <math.h>

int main(void) {

printf(" STUDENT RECORD SYSTEM \n");

//attendance

printf("enter details to check eligibility: \n");

float a,b;

printf("Enter the total number of classes held \n ");

scanf("%d",&a);

printf("Enter the number of classes attended. \n");

scanf("%d",&b);

if((b/a) *100 <60) {

printf("Your attendance is less than 60%\n”);

}

else {

printf("You are eligible for giving the examinations
\n");

}

//marks

int
marks,physics_marks,chem_marks,maths_marks,to
tal_marks;

printf("Enter your physics marks \n");

printf("Enter your chemistry marks \n");

printf("Enter your mathematics marks \n");

scanf(“%d %d
%d”,&physics_marks,&chem_marks,&maths_marks
);

total_marks=phyics_marks+chem_marks+maths_
marks;
printf("Your total marks are %d",total_marks);

if(total_marks>=30){

printf("You have passed the exam \n");

}

else {

printf("You have falied the exam...reappear for
test”);

}
//fee

int tution_fee,bus_fee,hostel_fee,total_fee;

printf("Enter tution fee \n");

printf("Enter bus fee \n");

printf("Enter hostel fee \n");

scanf("%d %d
%d",&tution_fee,&bus_fee,&hostel_fee);

total_fee=tition_fee+hostel_fee+bus_fee;

printf("Total fee paid is %d \n",total_fee);

if(total_fee>=50000){

printf("Your fee is paid");

}

else {

printf("please pay your fee immediately”);

}

return 0;

}

