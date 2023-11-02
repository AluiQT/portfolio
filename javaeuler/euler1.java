class Untitled {
	public static void main(String[] args) {
		int i = 0;
		int sum = 0;
		while (i < 1000) {
			if (i % 3 == 0 || i % 5 == 0) {
				sum = sum + i;
			}
		i++;
		}
		System.out.println(sum);
	}		
}