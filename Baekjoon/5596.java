import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = 0; 
        int b = 0; 
        int n;
        for (int i = 0; i < 4; i++){
            n = sc.nextInt();
            a += n;
        }
        for (int i = 0; i < 4; i++){
            n = sc.nextInt();
            b += n;
        }
        System.out.println(Math.max(a, b));
    }
}
