/*
 * Author: AdyaArchita
 
 * Problem: Minimum Number of Arrows to Burst Balloons

 * Approach:
 * 1. Use a Greedy approach, which is the most efficient for this problem.
 * 2. Sort the balloons based on their 'end' coordinates (x_end) in ascending order.
 * 3. This greedy choice ensures we always shoot an arrow at the earliest possible end point, maximizing the chance of hitting subsequent overlapping balloons.
 * 4. Initialize arrow count to 1 and set the first arrow's position to the end of the first balloon (points[0][1]).
 * 5. Iterate from the second balloon (i = 1).
 * 6. If the current balloon's 'start' (points[i][0]) is after the last arrow's position, it means the previous arrow cannot burst it.
 * 7. If a new arrow is needed, increment the arrow count and update the arrow's position to the 'end' of the current balloon (points[i][1]).
 * 8. If the current balloon's 'start' is at or before the arrow's position, it's guaranteed to be burst by the last arrow (since we sorted by end times), so we do nothing and continue.
 
 * Input: User enters the number of balloons, followed by the start and end coordinates for each balloon.
 * Output: The minimum number of arrows required.
 
 * Time Complexity: O(n log n), where n = number of balloons.
    * - The runtime is dominated by the initial sorting of the 'points' vector.
    * - The subsequent loop to count arrows is a single pass, which is O(n).
 * Space Complexity: O(log n) or O(n) depending on implementation.
    * - This space is used by the `std::sort` algorithm for its internal stack/storage.
    * - The iterative part of our solution only uses O(1) extra space for variables.
 */

#include <iostream>
#include <vector>
#include <algorithm> 

using namespace std;

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.empty()) {
            return 0;
        }
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });       
        int arrows = 1; 
        int arrowPosition = points[0][1]; // The first arrow is shot at the end of the first balloon .This is our greedy choice.       
        for (int i = 1; i < points.size(); ++i) { 
            int currentStart = points[i][0]; 
            
            if (currentStart > arrowPosition) {// If the current balloon starts after our last arrow was shot, it means our previous arrow cannot burst it.
                arrows++;
                arrowPosition = points[i][1]; 
            }
        }
        return arrows;
    }
};

int main() {
    Solution sol;
    vector<vector<int>> points;
    int n;
    cout << "Enter the number of balloons: ";
    cin >> n;
    cout << "Enter the start and end coordinates for each balloon (e.g., '1 6'):" << endl;
    for (int i = 0; i < n; ++i) {
        int start, end;
        cout << "Balloon " << i + 1 << ": ";
        cin >> start >> end;
        points.push_back({start, end});
    }
    int result = sol.findMinArrowShots(points);
    cout << "Minimum number of arrows needed: " << result << endl;
    return 0;
}