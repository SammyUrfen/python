import java.util.*;
import java.math.*;

public class G_The_number_of_positions{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int a = input.nextInt();
        int b = input.nextInt();

        if (a+b<n){
            System.out.println(b+1);
        }
        else{
            System.out.println(n-a);
        }
    }
}