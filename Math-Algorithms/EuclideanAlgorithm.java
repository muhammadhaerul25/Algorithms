import java.util.Scanner;

class EuclideanAlgorithm {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		System.out.println();
		int m = scan.nextInt();
		int n = scan.nextInt();

		int m1 = 0;
		int n1 = 0;

		while (n!= 0) {

			if (m > 0 && n > 0) {
				int q = m/n;
				int r = m - n*q;

				m1 = m;
				n1 = n;

				m = n;
				n = r;

				System.out.println(m1 + " = " + n1 + "(" + q + ") + " + r);
			}

			else {
				int q = m/n - 1;
				int r = m - n*q;

				if (r >= n) {
					q = m/n;
					r = m - n*q;
				}

				m1 = m;
				n1 = n;

				m = n;
				n = r;

				System.out.println(m1 + " = " + n1 + "(" + q + ") + " + r);

			}
			
		}

		if (n1 < 0) {
			n1 = n1*(-1);
		}

		System.out.println("\nGCD = " + n1);
	}
}