import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[201];
        for (int i = 0; i < n; i++)
            a[sc.nextInt() + 100]++;
        System.out.print(a[sc.nextInt() + 100]);
    }
}
