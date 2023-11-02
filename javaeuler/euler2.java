class euler2 {
	public static void main(String[] args) {
		int i = 1;
		int j = 2;
		int k = 0;
		int sum = 2;
		while (k < 4000000) {
			k = i + j;
			if (k < 4000000 && k % 2 == 0) {
				sum = sum + k;
			}
			i = j;
			j = k;
		}
		System.out.println(sum);
	}
}