import java.util.*;
import java.lang.*;
import java.io.*;

class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        boolean flag = true;
        int num = sc.nextInt();
        for (int i = 1; i < n; i++){
            int tmp = sc.nextInt();
            if(num != tmp){
                flag = false;
                break;
            }
            num = tmp;
        }
        
        if(flag){
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
	}
	
}
