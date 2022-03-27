
#include<iostream>  
#include<cstdio>  
#include<ctime>
using namespace std;
#define M 4
#define N 4
#include <memory.h>  
 
int maxSubArray(int *arr, int len)       //最大子序列和  
{
	int i, sum = arr[0], b = 0;
	for (i = 0; i<len; ++i)
	{
		if (b>0)
			b += arr[i];
		else
			b = arr[i];
		if (b>sum)
			sum = b;
	}
	return sum;
}
int maxSubMatrix(int n, int m, int array[M][N])
{
	int i, j, h, max, sum = -100000;
	int b[100];
	for (i = 0; i < n; i++)
	{
		memset(b, 0, sizeof(b));       //初始化b[]  
		for (j = i; j < n; j++)          //把第i行到第j行相加,对每一次相加求出最大值  
		{
			for (h = 0; h<m; h++)
			{
				b[h] += array[j][h];   //二维数组压缩成一维数组，然后求最大子序列和  
			}
			max = maxSubArray(b, h);
 
			if (max>sum)
				sum = max;
		}
	}
	return sum;
}
int main()
{
	int arr[M][N] = { { -15, -21,5, -12 }, { -7, 21, 20, 12 }, { 21, 0, -1, 13 }, { 10, 20, -10, -18 } };
	cout << "随机二维数组为：" << endl;
	//srand(time(0));
	//for (int i = 0; i < M; i++)
	//{
	//	for (int j = 0; j < N; j++)
	//	{
	//		arr[i][j] = rand() % 50 - 25;
	//		cout << arr[i][j] << " ";
	//	}
	//	cout << endl;
	//}
	
	cout << maxSubMatrix(M, N, arr) << endl;
	system("pause");
	return 0;
}

