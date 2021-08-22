#include <stdio.h>
int n,d,i,dig,new=0,digit,n1=0,max=-1,n2,di;

void main()
{
	
	printf("Enter N: ");
	scanf("%d",&n);
	printf("\nEnter D: ");
	scanf("%d",&d);
	while (n>0)
	{
		dig = n%10;
		new = (new*10) + dig;
		n=n/10;
	}
	printf("\n%d",new);
	while (new>0)
	{
		digit = new%10;
		if(digit==d)
		{
			new = new/10;
			max = new%10;
			while(new>0)
			{
				
				new = new/10;
				digit = new%10;
				if(max<digit)
				{
					max = digit;
				}
				
			}
			break;
		}
		new=new/10;
	}
	if (max==-1)
		printf("\nDigit is not present in the number!\n");
	else
		printf("\nOutput: %d", max);
}
