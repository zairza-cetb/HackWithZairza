/*
 * Author: Dibyajyoti Parida
 * 
 * Problem: Assign Cookies
 * 
 * Approach (Greedy):
 * 1. Sort both greedFactor and cookieSize arrays.
 * 2. Use two pointers to iterate through both arrays.
 * 3. If the current cookie can satisfy the current child, assign it and move to the next child.
 * 4. Otherwise, try a larger cookie.
 * 5. Continue until all cookies or all children are processed.
 * 
 * Time Complexity: O(n log n)
 * Space Complexity: O(1)
 */



import java.util.Arrays;
import java.util.Scanner;

public class AssignCookies_dibyajyoti1515 {

    public static int findContentChildren(int[] greedFactor, int[] cookieSize) {
        Arrays.sort(greedFactor);
        Arrays.sort(cookieSize);

        int i = 0; // pointer for children
        int j = 0; // pointer for cookies

        while (i < greedFactor.length && j < cookieSize.length) {
            if (cookieSize[j] >= greedFactor[i]) {
                i++; // child satisfied
            }
            j++; // move to next cookie
        }
        return i; // number of satisfied children
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of children: ");
        int n = sc.nextInt();
        int[] greedFactor = new int[n];

        System.out.println("Enter greed factors:");
        for (int i = 0; i < n; i++) {
            greedFactor[i] = sc.nextInt();
        }

        System.out.print("Enter number of cookies: ");
        int m = sc.nextInt();
        int[] cookieSize = new int[m];

        System.out.println("Enter cookie sizes:");
        for (int i = 0; i < m; i++) {
            cookieSize[i] = sc.nextInt();
        }

        int result = findContentChildren(greedFactor, cookieSize);
        System.out.println("Maximum number of content children: " + result);
    }
}

