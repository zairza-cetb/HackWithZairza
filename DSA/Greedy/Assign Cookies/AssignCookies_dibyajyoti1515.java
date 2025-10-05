/*
 * Author: Dibyajyoti Parida
 * 
 * Problem: Assign Cookies (LeetCode #455)
 * 
 * Approach:
 * 1. Sort both greedFactor and cookieSize arrays.
 * 2. Use two pointers: one for greedFactor (children), one for cookieSize (cookies).
 * 3. If a cookie can satisfy a child, assign it and move both pointers.
 * 4. Otherwise, move the cookie pointer forward to find a larger cookie.
 * 5. Return the number of satisfied children.
 * 
 * Time Complexity: O(n log n) – due to sorting
 * Space Complexity: O(1)
 */

import java.util.*;

public class AssignCookies_dibyajyoti1515 {
    public static int findContentChildren(int[] greedFactor, int[] cookieSize) {
        Arrays.sort(greedFactor);
        Arrays.sort(cookieSize);
        
        int i = 0, j = 0;
        while (i < greedFactor.length && j < cookieSize.length) {
            if (cookieSize[j] >= greedFactor[i]) {
                i++; // child satisfied
            }
            j++; // move to next cookie
        }
        return i;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of children: ");  // Input for greedFactor
        int n = sc.nextInt();
        int[] greedFactor = new int[n];
        System.out.println("Enter greed factors:");
        for (int i = 0; i < n; i++) {
            greedFactor[i] = sc.nextInt();
        }

        System.out.print("Enter number of cookies: ");  // Input for cookieSize 
        int m = sc.nextInt();
        int[] cookieSize = new int[m];
        System.out.println("Enter cookie sizes:");
        for (int i = 0; i < m; i++) {
            cookieSize[i] = sc.nextInt();
        }

        int result = findContentChildren(greedFactor, cookieSize);
        System.out.println("Number of content children: " + result);
    }
}
