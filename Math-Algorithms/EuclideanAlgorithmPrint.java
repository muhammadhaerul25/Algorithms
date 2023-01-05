class EuclideanAlgorithmPrint {
    public static void main(String[] args) {
        int m = Integer.parseInt(args[0]);
        int n = Integer.parseInt(args[1]);

        int m1 = 0;
        int n1 = 0;

        while (n != 0) {
            int q = m / n;
            int r = m - n * q;

            m1 = m;
            n1 = n;
            m = n;
            n = r;

            System.out.println(m1 + " = " + n1 + "(" + q + ") + " + r);
        }

        System.out.println("\nGCD = " + Math.abs(n1));
    }
}
