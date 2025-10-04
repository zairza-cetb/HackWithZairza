#include <iostream>
#include <vector>
#include <string>
#include <unordered_set> // For efficient word dictionary lookups

bool wordBreak(std::string s, std::vector<std::string>& wordDict) {
    // Convert the word dictionary to an unordered_set for O(1) average time complexity lookups
    std::unordered_set<std::string> wordSet(wordDict.begin(), wordDict.end());

    int n = s.length();
    // dp[i] will be true if s[0...i-1] can be segmented into dictionary words
    std::vector<bool> dp(n + 1, false);

    // Base case: An empty string can always be segmented
    dp[0] = true;

    // Iterate through the string from left to right
    for (int i = 1; i <= n; ++i) {
        // Check all possible split points 'j' before 'i'
        for (int j = 0; j < i; ++j) {
            // If s[0...j-1] can be segmented (dp[j] is true)
            // AND the substring s[j...i-1] is a valid word in the dictionary
            if (dp[j] && wordSet.count(s.substr(j, i - j))) {
                dp[i] = true; // Then s[0...i-1] can also be segmented
                break;       // No need to check further split points for this 'i'
            }
        }
    }

    // The final result is whether the entire string s[0...n-1] can be segmented
    return dp[n];
}

int main() {
    std::string s1 = "leetcode";
    std::vector<std::string> wordDict1 = {"leet", "code"};
    std::cout << "Can \"" << s1 << "\" be broken? " << (wordBreak(s1, wordDict1) ? "Yes" : "No") << std::endl; // Expected: Yes

    std::string s2 = "applepenapple";
    std::vector<std::string> wordDict2 = {"apple", "pen"};
    std::cout << "Can \"" << s2 << "\" be broken? " << (wordBreak(s2, wordDict2) ? "Yes" : "No") << std::endl; // Expected: Yes

    std::string s3 = "catsandog";
    std::vector<std::string> wordDict3 = {"cats", "dog", "sand", "and", "cat"};
    std::cout << "Can \"" << s3 << "\" be broken? " << (wordBreak(s3, wordDict3) ? "Yes" : "No") << std::endl; // Expected: No

    return 0;
}
