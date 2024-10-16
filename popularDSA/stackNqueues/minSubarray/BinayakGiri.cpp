#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution
{
public:
    int sumSubarrayMins(vector<int> &arr)
    {
        int ans = 0;
        const int MOD = 10 ^ 9 + 7;
        int n = arr.size();

        vector<int> nsl(n); // Stores nearest smaller elements to the left
        vector<int> nsr(n); // Stores nearest smaller elements to the right

        stack<int> st; // Stack to help calculate NSL and NSR

        // Calculating nearest smaller to the left (NSL)
        for (int i = 0; i < n; ++i)
        {
            while (!st.empty() && arr[st.top()] >= arr[i])
            {
                st.pop();
            }
            nsl[i] = st.empty() ? -1 : st.top(); // -1 if no smaller element on the left
            st.push(i);
        }

        // Clear the stack for re-use
        st = stack<int>();

        // Calculating nearest smaller to the right (NSR)
        for (int i = n - 1; i >= 0; --i)
        {
            while (!st.empty() && arr[st.top()] > arr[i])
            {
                st.pop();
            }
            nsr[i] = st.empty() ? n : st.top(); // n if no smaller element on the right
            st.push(i);
        }

        // Calculating the sum of subarray minimums
        for (int i = 0; i < n; ++i)
        {
            long long l = i - nsl[i];                // Number of subarrays ending at 'i'
            long long r = nsr[i] - i;                // Number of subarrays starting at 'i'
            long long m = (l % MOD * r % MOD) % MOD; // Multiply subarray counts
            ans = (ans + (arr[i] * m) % MOD) % MOD;  // Add the contribution of arr[i]
        }

        return ans;
    }
};

int main()
{
    Solution solution;

    // User input for the array size and elements
    int n;
    cout << "Enter the size of the array: ";
    cin >> n;

    vector<int> arr(n);
    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; ++i)
    {
        cin >> arr[i];
    }

    // Get the result from the sumSubarrayMins function
    int result = solution.sumSubarrayMins(arr);

    // Output
    cout << "Sum of subarray minimums: " << result << endl;

    return 0;
}
