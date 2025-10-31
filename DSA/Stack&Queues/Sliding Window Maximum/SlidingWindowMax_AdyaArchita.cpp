/*
 * Author: AdyaArchita (inspired by user's request)
 
 * Problem: Sliding Window Maximum 
 
 * Approach:
  1. Use an optimized approach with a Deque (Double-Ended Queue).
  2. The deque will store *indices* of elements, not the elements themselves.
  3. We maintain a "monotonically decreasing" queue: the values at the indices in the deque are always in descending order (e.g., nums[deque[0]] > nums[deque[1]]).
  4. This structure cleverly ensures the *front* of the deque (`dq.front()`) is *always* the index of the maximum element in the current window.
 
 * Algorithm (for each element `nums[i]` at index `i`):
 * 1. *Clean Front:* Check if the *front* of the deque is the index that just fell out of the window (i.e., `dq.front() == i - k`). If so, pop it from the front (`dq.pop_front()`).
 * 2. *Clean Back:* While the deque isn't empty AND the new element `nums[i]` is greater than or equal to the element at the *back* of the deque (`nums[dq.back()]`), pop from the back (`dq.pop_back()`). This removes all smaller elements that are now "blocked" by `nums[i]` and can never be the maximum.
 * 3. *Add New:* Push the current index `i` onto the *back* of the deque (`dq.push_back(i)`).
 * 4. *Get Max:* Once the window is fully formed (`i >= k - 1`), the maximum element for this window is `nums[dq.front()]`. Add this value to our result vector.
 
 * Input: User enters the size of the array, the array elements, and the window size 'k'.
 * Output: A list of maximum values for each sliding window.
 
 * Time Complexity: O(n), where N = number of elements.
     - Each element is added to the deque exactly once and removed at most once (amortized O(1) per element).
 * Space Complexity: O(k)
     - The deque will store at most 'k' indices at any given time.
 */

#include <iostream>
#include <vector>
#include <deque>     
#include <limits>    
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> result;
        deque<int> dq; 
        for (int i = 0; i < nums.size(); ++i) {
            if (!dq.empty() && dq.front() == i - k) 
                dq.pop_front();
            while (!dq.empty() && nums[i] >= nums[dq.back()]) 
                dq.pop_back();
            dq.push_back(i);
            if (i >= k - 1)
                result.push_back(nums[dq.front()]);
        }
        return result;
    }
};

int main() {
    Solution sol;
    vector<int> nums;
    int n , i , k ;
    cout << "Enter the number of elements: ";
    while (!(cin >> n) || n <= 0) {
        cout << "Invalid input. Please enter a positive number: ";
        cin.clear(); 
        cin.ignore(numeric_limits<streamsize>::max(), '\n'); 
    }
    nums.resize(n);
    cout << "Enter " << n << " numbers (separated by spaces):" << endl;
    for (i = 0; i < n; ++i) {
        cout << "Element " << i + 1 << ": ";
        while (!(cin >> nums[i])) {
            cout << "Invalid input. Please enter a valid number: ";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
    }

    cout << "Enter the window size k: ";
    while (!(cin >> k) || k <= 0 || k > n) {
        cout << "Invalid input. Please enter k (where 1 <= k <= " << n << "): ";
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }
    vector<int> result = sol.maxSlidingWindow(nums, k);

    cout << "Maximums in each sliding window:" << endl;
    for (int maxVal : result) {
        cout << maxVal << " ";
    }
    cout << endl;
    return 0;
}