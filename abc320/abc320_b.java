import java.util.*;
import java.lang.*;
import java.io.*;

class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		int sLen = s.length();
		int maxN = 0;
		for (int i = 0; i < sLen; i++){
		    for (int j = i; j < sLen+1; j++){
		        
		        String tmp = s.substring(i,j);
		        StringBuilder sb = new StringBuilder();
		        sb.append(tmp);
		        sb.reverse();
		        if(tmp.equals(sb.toString())){
		            if(maxN < tmp.length()){
		                maxN = tmp.length();
		            }
		        }
		        
		    } 
		}
		
		System.out.println(maxN);

	}
}
