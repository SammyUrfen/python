import java.util.*;

public class J_Elephant{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int i =0;
        if (n>=5){
            i += n/5;
        }
        if (n%5!=0){
            i++;
        }
        System.out.println(i);
    }
}