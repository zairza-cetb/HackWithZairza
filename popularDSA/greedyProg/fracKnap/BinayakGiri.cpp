//Fractional Knapsack
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Structure to represent an item with value and weight
struct Item {
    int value, weight;
};

// Comparison function to sort items based on value/weight ratio in descending order
bool cmp(Item a, Item b) {
    double r1 = (double)a.value / (double)a.weight;
    double r2 = (double)b.value / (double)b.weight;
    return r1 > r2;
}

// Function to get the maximum total value in the knapsack
double fractionalKnapsack(int W, vector<Item>& items, int n) {
    // Sort items by value-to-weight ratio
    sort(items.begin(), items.end(), cmp);
    
    double total_value = 0.0;  // Total value in knapsack
    int remaining_capacity = W;
    
    for (int i = 0; i < n; i++) {
        if (remaining_capacity == 0) break;
        
        if (items[i].weight <= remaining_capacity) {
            // If the item can be added fully
            total_value += items[i].value;
            remaining_capacity -= items[i].weight;
        } else {
            // If only a fraction of the item can be added
            total_value += items[i].value * ((double)remaining_capacity / (double)items[i].weight);
            remaining_capacity = 0;  // Knapsack is full
        }
    }
    
    return total_value;
}

int main() {
    int n, W;
    cout << "Enter the number of items: ";
    cin >> n;
    
    cout << "Enter the capacity of the knapsack: ";
    cin >> W;
    
    vector<Item> items(n);
    
    cout << "Enter the value and weight of each item:\n";
    for (int i = 0; i < n; i++) {
        cout << "Item " << i + 1 << " value: ";
        cin >> items[i].value;
        cout << "Item " << i + 1 << " weight: ";
        cin >> items[i].weight;
    }
    
    double max_value = fractionalKnapsack(W, items, n);
    cout << "Maximum value in Knapsack = " << max_value << endl;
    
    return 0;
}
