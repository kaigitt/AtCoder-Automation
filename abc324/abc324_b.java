import java.util.*;
import java.lang.*;
import java.io.*;

class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        boolean flag = false;
        for (long i = 0; i < 60; i++){
            for (long j = 0; j < 60; j++){
                if(n == myPow(2, i) * myPow(3, j)){
                    flag = true;
                    break;
                }
            } 
        }
        
        if(flag){
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
        
	}
	
	public static long myPow(long a, long n) {
        // a^nを計算
        long ans = 1l;
        long tmp = a;

        // わかりやすくfor文の中ですべて処理
        for (;;) {
            // すべての桁を見終わったら終了
            if (n < 1l) {
                break;
            }

            // 最下位bitが1かどうかの判定
            if (n % 2l == 1l) {
                ans *= tmp;
            }

            // tmpの更新
            tmp *= tmp;

            // nのbitを一つずらす
            n = n >> 1;
        }
        return ans;
    }
}
