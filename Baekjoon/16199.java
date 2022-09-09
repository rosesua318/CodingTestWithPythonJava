import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(); 
        int b = sc.nextInt();
        int c = sc.nextInt();
        int x = sc.nextInt();
        int y = sc.nextInt();
        int z = sc.nextInt();
        
        int n1 = 0;
        
        if (b < y) {
            n1 = x - a;
        } else if (b == y && c <= z) {
            n1 = x - a;
        } else {
            n1 = x - a - 1;
        }
        int n2 = x - a + 1;
        int n3 = x - a;
    
        System.out.println(n1);
        System.out.println(n2);
        System.out.println(n3);
    }
}
