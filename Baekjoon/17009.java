import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] a = new int [6];
        for(int i = 0; i < 6; i++) {
            a[i] = sc.nextInt();
        }           
        int x = a[0] * 3 + a[1] * 2 + a[2]; 
        int y = a[3] * 3 + a[4] * 2 + a[5]; 
        if (x == y) {
            System.out.println("T");    
        } else if (x > y) {
            System.out.println("A");
        } else {
            System.out.println("B");
        }            
    }
}
