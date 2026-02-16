import java.util.*;

public class A_Johny_Likes_Numbers{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        int k = input.nextInt();

        int ans = n+k-(n%k); 
        System.out.println(ans);
    }
}