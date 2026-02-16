import java.util.*;

public class D_The_Time{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        String time = input.nextLine();
        int passed = input.nextInt();
        String[] clock = time.split(":", 2);

        int hour = Integer.parseInt(clock[0]);
        int min = Integer.parseInt(clock[1]);
        min += passed;
        if (min >= 60){
            hour += (min/60);
            min -= 60*(min/60);
        }
        if (hour >= 24){
            hour -= 24*(hour/24);
        }

        String hora = Integer.toString(hour);
        String mino = Integer.toString(min);

        if (hour == 0){
            hora = String.format("%02d", hour);
        }
        else if (hour < 10){
            hora = String.format("%02d", hour);
        }
        if (min == 0){
            mino = String.format("%02d", min);
        }
        else if (min < 10){
            mino = String.format("%02d", min);
        }
        System.out.println(hora+":"+mino);
    }
}