import java.util.Scanner;
public class Main {
	public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
		int n = Integer.parseInt(sc.nextLine());
		
		StringBuilder sb = new StringBuilder();
		while(n-- > 0) {
			sb.append("SciComLove").append("\n");
		}
		System.out.print(sb);
	}
}
