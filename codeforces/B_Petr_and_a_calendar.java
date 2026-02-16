import java.util.*;

public class B_Petr_and_a_calendar{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int m = input.nextInt();
        int d = input.nextInt();

        if (m==4 || m==6 || m==9 || m==11){
            if (d==7){
                System.out.println(6);
            }
            else{
                System.out.println(5);
            }
        }
        else if (m==2){
            if (d==1){
                System.out.println(4);
            }
            else{
                System.out.println(5);
            }
        }
        else{
            if (d==7 || d==6){
                System.out.println(6);
            }
            else{
                System.out.println(5);
            }
        }
    }
}