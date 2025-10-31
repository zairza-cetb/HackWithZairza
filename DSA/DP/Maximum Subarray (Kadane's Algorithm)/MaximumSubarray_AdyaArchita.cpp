#include <iostream>
#include <vector>
#include <algorithm> // Needed for std::max

using namespace std;

int main() {

    int n;
    cout << "Enter the number of elements: ";
    cin >> n;

    // Handle case where user enters non-positive number of elements
    if (n <= 0) {
        cout << "The number of elements must be positive." << endl;
        return 1; // Exit with an error code
    }

    // Create a vector (a dynamic array) to hold the numbers.
    vector<int> nums(n);

    cout << "Enter " << n << " numbers (separated by spaces): ";
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }

    // --- Step 2: The Core Algorithm (Kadane's) ---

    // We need two variables:
    // 1. currentMax: Stores the maximum sum of a subarray ending at the current position.
    // 2. maxSoFar:   Stores the overall maximum sum we have found anywhere in the array.
    // We start by assuming the first number is the best we can do for both.
    int maxSoFar = nums[0];
    int currentMax = nums[0];

    // We've already handled the first element, so we loop from the second one.
    for (int i = 1; i < nums.size(); ++i) {
        
        // At each number, we make a choice:
        // Choice A: Start a new subarray here. The sum would just be the current number (nums[i]).
        // Choice B: Extend the previous subarray. The sum would be (the best sum ending at the previous spot) + (the current number).
        
        // We pick whichever choice gives us a bigger number.
        currentMax = max(nums[i], currentMax + nums[i]);
        
        // Now, we check if the best subarray ending here (currentMax) is even better
        // than the overall best subarray we've seen anywhere so far (maxSoFar).
        // If it is, we update our overall best.
        maxSoFar = max(maxSoFar, currentMax);
    }

    cout << "The maximum subarray sum is: " << maxSoFar << endl;

    return 0;
}
