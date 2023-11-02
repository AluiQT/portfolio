class Untitled {
	public static void main(String[] args) {
		for(int baka = 2520; ; baka+= 2520) {
			if (isEvenlyDivisible(baka)) {
				System.out.println(baka);
				break;
			}	
		}
	}
	public static boolean isEvenlyDivisible(int num) {
		for(int i = 11; i <= 20; i++) {
			if(num % i != 0) {
				return false;
			}
	    }
		return true;
	}
}