import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int k = sc.nextInt(); 
		int[] a;
		for (int i = 0; i < k; i++) {
			int n = sc.nextInt();
			a = new int[n];
			int s = 0;
			for(int j = 0; j < n; j++) {
				int point = sc.nextInt();
				a[j] = point;
				s += point;
			}
			double avg = (double)s / n;
			double count = 0;
			for (int j = 0; j < n; j++) {
				if(a[j] > avg) {
					count++;
				}
			}
			System.out.printf("%.3f%%\n", count / n * 100);
		}
	}
}
