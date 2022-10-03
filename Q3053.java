import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int r = sc.nextInt();
        double pi = 3.14159265359;
        
        System.out.println(pi * r * r);
        System.out.println(r * r * 2);
        
        sc.close();
    }
}
