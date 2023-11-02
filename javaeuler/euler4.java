class euler4 {
	public static void main(String[] args) {
		int largestPalindrome = 0;
		for(int i = 100; i < 1000; i++)	{
			for(int j = 100; j < 1000; j++){
				int k = i * j;
				if(isPalindrome(k) && k > largestPalindrome) {
					largestPalindrome = k;
				}
			}
		}
		System.out.println(largestPalindrome);
	}
		static boolean isPalindrome(int num) {
				int originalNum = num;
				int reverse = 0;
				while (num != 0) {
					reverse = reverse * 10 + num % 10;
					num /= 10;
				}
				return originalNum == reverse;
			}
	}
