#include<stdio.h>

void main()
{
	
	
	int n,i;
	printf("Enter n: ");
	scanf("%d",&n);
	int arr[n];
	printf("\nEnter the array elements: ");
	for (i=0; i<n; i++)
	{
		scanf("%d",&arr[i]);
	}
	
	/*, arr[10], res[10], i, k=1;	
	printf("Enter the size of the array: ");
	scanf("%d", &n);
	printf("\nEnter the array elements: ");
	for (i=0; i<n; i++)
	{
		scanf("%d",&arr[i]);
	}*/
	res[0] = arr[0];
	for (i=1; i<n; i++)
	{
		if(arr[i-1]%7==0)
		{
			res[k] = arr[i];
			k++;
		}
	}
	printf("\n7up elements are: ");
	for(i=0;i<k;i++)
	{
		printf("%d ",res[i]);
	}

}
