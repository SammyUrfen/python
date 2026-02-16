import java.util.*;
import java.math.*;

public class E_Pashmak_and_Garden{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int x1 = input.nextInt();
        int y1 = input.nextInt();
        int x2 = input.nextInt();
        int y2 = input.nextInt();
        
        int dist_x = Math.abs(x1 - x2);
        int dist_y = Math.abs(y1 - y2);
        if (x1 == x2){
            System.out.println((x1+dist_y)+" "+y1+" "+(x2+dist_y)+" "+y2);
        }
        else if (y1 == y2){
            System.out.println(x1+" "+(y1+dist_x)+" "+x2+" "+(y2+dist_x));      
        }
        else if (dist_x == dist_y){
            if (y1 < y2 && x1<x2){
                System.out.println(x1+" "+(y1+dist_x)+" "+x2+" "+(y2-dist_x));
            }
            if (y1 < y2 && x1>x2){
                System.out.println((x1-dist_y)+" "+y1+" "+(x2+dist_y)+" "+y2);
            }
            if (y1 > y2 && x1<x2){
                System.out.println(x1+" "+(y1-dist_x)+" "+x2+" "+(y2+dist_x));
            }
            if (y1 > y2 && x1>x2){
                System.out.println((x1-dist_y)+" "+y1+" "+(x2+dist_y)+" "+y2);
            }
        }
        else{
            System.out.println(-1);
        }
    }
}