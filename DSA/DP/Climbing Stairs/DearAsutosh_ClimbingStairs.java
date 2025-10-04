public class DearAsutosh_ClimbingStairs {
        public static int climbStairs(int n) {
            if (n <= 3)
                return n;
            int firstPrev = 3, secPrev = 2, curr = 0;
            for (int i = 3; i < n; i++) {
                curr = firstPrev + secPrev;
                secPrev = firstPrev;
                firstPrev = curr;
            }

            return curr;
        }

    public static void main(String[] args) {
        int n=4;
        System.out.println("There are "+climbStairs(n)+" ways to climb "+n+" stairs.");
    }
}
