#include <stdio.h>


void main()
{
	int n,i,dig,k,sum,temp,j;
	printf("Enter N: ");
	scanf("%d", &n);
	int arr[n][2];
	printf("\nEnter array elements: ");
	for (i=0; i<n; i++)
	{
		sum=0;
		scanf("%d", &arr[i][0]);
		k = arr[i][0];
		while(k>0)
		{
			dig = k%10;
			sum = sum + dig;
			k = k/10;
		}
		arr[i][1] = sum;
	}
	for(i=0; i<n; i++)
	{
		for(j=i+1; j<n; j++)
		{
			if (arr[i][1] == arr[j][1])
			{
				
			}
			else if(arr[i][1] > arr[j][1])
			{
				temp = arr[i][1];
				arr[i][1] = arr[j][1];
				arr[j][1] = temp;
			
				temp = arr[i][0];
				arr[i][0] = arr[j][0];
				arr[j][0] = temp;
			}
			
		}
	}
	printf("\nOutput is: ");
	for(i=0;i<n;i++)
	{
		printf("%d ", arr[i][0]);
	}
}

/*
void main()
{
	int n,i,dig,k,sum,temp,j;
	printf("Enter N: ");
	scanf("%d", &n);
	int arr[n];
	printf("\nEnter array elements: ");
	scanf("%d", &k);
	sum=0;
	while(k>0)
	{
		dig = k%10;
		sum = sum + dig;
		k = k/10;
	}
	min = sum;
	for (i=0;
	for (i=1; i<n; i++)
	{
		scanf("%d", &k);
		sum=0;
		while(k>0)
		{
			dig = k%10;
			sum = sum + dig;
			k = k/10;
		}
		if(min>sum)
		{
			min = sum;
		}
	}
	arr[i]=k;
	
}*/
