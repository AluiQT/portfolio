class Untitled {
	public static void main(String[] args) {
		System.out.println(differenceSum(100));
	}
	public static int sqrNums(int num) {
		int x = 0;
		for (int i = 0; i <= num; i++){
			x += i*i;
		}
	return x;
	}
	public static int sqrSums(int sum) {
		int k = 0;
		int som = 0;
		for (int i = 1; i <= sum; i++) {
			som = som + i;
			k = som;
		}
		return k*k;
	}
	public static int differenceSum(int baka){
		return sqrSums(baka) - sqrNums(baka);
	}
}