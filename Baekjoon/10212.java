public class Main {
    public static void main(String[] args) throws Exception {
        int a = 1;
        int b = 0;
        int n = b + (int) (Math.random() * ((a - b) + 1));
        String s = "Korea";
        if (n % 2 == 0) {
            s = "Yonsei";
        }
        System.out.print(s);
    }
}
