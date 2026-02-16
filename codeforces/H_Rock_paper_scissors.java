import java.util.*;

public class H_Rock_paper_scissors {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String F = sc.nextLine();
        String M = sc.nextLine();
        String S = sc.nextLine();

        if (F.equals("paper") && M.equals("rock") && S.equals("rock")) {
            System.out.println("F");
            }
        else if (F.equals("scissors") && M.equals("paper") && S.equals("paper")){
            System.out.println("F");
            }
        else if (F.equals("rock") && M.equals("scissors") && S.equals("scissors")){
            System.out.println("F");
            } 
        else if (F.equals("rock") && M.equals("paper") && S.equals("rock") ){
            System.out.println("M");
            }  
        else if (F.equals("paper") && M.equals("scissors") && S.equals("paper")){
            System.out.println("M");
            }    
        else if (F.equals("scissors") && M.equals("rock") && S.equals("scissors")){
            System.out.println("M");
        }             
        else if (F.equals("rock") && M.equals("rock") && S.equals("paper")){
            System.out.println("S");
        }
        else if (F.equals("scissors") && M.equals("scissors") && S.equals("rock")){
            System.out.println("S");
        }
        else if (F.equals("paper") && M.equals("paper") && S.equals("scissors")){
            System.out.println("S");
        }
        else {
            System.out.println("?");
        }
    }
}