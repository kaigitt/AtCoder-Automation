import java.util.*;
import java.lang.*;
import java.io.*;

class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
        Scanner sc = new Scanner(System.in);
        String n = sc.next();
        int preN = Integer.parseInt(n.substring(0,1));
        boolean flag = true;
        for(int i = 1; i < n.length(); i++){
            int curN =  Integer.parseInt(n.substring(i, i+1));
            //System.out.println(curN);
            if(preN <= curN){
                flag = false;
            }
            if(!flag){
                break;
            }
            preN = curN;
        }
        
        if(flag){
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
	}
}
