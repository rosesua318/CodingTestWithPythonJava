import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a = 0;
        int b = 0; 
        int sum = 0;

        for(int i = 1; i <= n; i++) {
            a = sc.nextInt();
            b = sc.nextInt();
            sum = a + b;
            System.out.println("Case #" + i +": " + a + " + " + b + " = " + sum);
        }
        
        sc.close();
    }
}
