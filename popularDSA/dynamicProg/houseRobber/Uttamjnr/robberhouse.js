function rob(houses) {   //we have to input an array where number of index = number of houses and the value of index is equal to the money the house have
    const n = houses.length; //stores number of houses 

    // Handle base cases
    if (n === 0) return 0;
    if (n === 1) return houses[0];
    if (n === 2) return Math.max(houses[0], houses[1]);

    // Initialize variables to store the maximum amounts
    let p1 = houses[0]; // Maximum amount robbed up to house 1
    let p2 = Math.max(houses[0], houses[1]); // Maximum amount robbed up to house 2

    // Iterate through the houses starting from the third one
    for (let i = 2; i < n; i++) {
        const current = Math.max(p2, houses[i] + p1); //stores the current and updates the value 
        p1 = p2; // Update p1 to be the previous maximum
        p2 = current; // Update p2 to be the current maximum
    }

    return p2; // returns  computed value, the maximum amount that can be robbed
}

// Example usage
console.log(rob([1, 2, 3, 1]));  // Output: 4
console.log(rob([2, 7, 9, 3, 1]));  // Output: 12
