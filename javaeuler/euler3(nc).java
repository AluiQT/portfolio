/** The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
**/

class Untitled {
	public static void main(String[] args) {
		long n = 600851475143L;
		long largestPrimeFactor = 0;
		
		while (n % 2 == 0) {
			largestPrimeFactor = 2;
			n /= 2;
		}
		for (long i = 3; i <= Math.sqrt(n); i += 2) {
			while (n % i == 0) {
				largestPrimeFactor = i;
				n /= i;
			}
		}
		if (n > 1) {
			largestPrimeFactor = n;
		}
		
		System.out.println(largestPrimeFactor);
	}
}