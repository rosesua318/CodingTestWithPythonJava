import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int a = 5;

    for(int i = 1; i < n; i++) {
      a = (a + (i + 2) * 3 - 2) % 45678;
    }

    System.out.println(a);
    sc.close();
  }
}
