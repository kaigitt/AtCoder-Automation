import java.util.*;
import java.lang.*;
import java.io.*;

class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		long n = sc.nextInt();
		long m = sc.nextInt();
		long totalN = 1;
		for (int i = 0; i < m; i++){
		    totalN = totalN * n;
		} 
		long totalM = 1;
		for (int i = 0; i < n; i++){
		    totalM = totalM * m;
		} 
		System.out.println(totalN + totalM);
	}
}
