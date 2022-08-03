import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] a = new int[31];

		for (int i = 1; i < 29; i++) {
			int n = sc.nextInt();
			a[n] = 1;
		}
		for (int i = 1; i < a.length; i++) {
			if (a[i] != 1)
				System.out.println(i);
		}

		sc.close();
	}
}
