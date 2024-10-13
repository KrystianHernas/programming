#include <iostream>
#include <vector>
#include <algorithm>
#include <climits> // For INT_MAX

// Function to calculate the maximum number of times a row can fit in arr2
int calculateFit(const std::vector<int>& row, const std::vector<int>& arr2) {
    int minFit = INT_MAX;
    for (int i = 0; i < 4; ++i) {
        if (row[i] > 0) {
            minFit = std::min(minFit, arr2[i] / row[i]);
        }
    }
    return minFit;
}

int main() {
    // Using vectors instead of arrays
    std::vector<std::vector<int>> arr1 = {
        {3, 3, 2, 1},
        {1, 0, 0, 9},
        {0, 1, 0, 9},
        {0, 0, 1, 9},
        {0, 0, 0, 1}
    };

    std::vector<int> arr2 = {9, 9, 8, 5};

    // Sort the array using the custom comparator
    std::sort(arr1.begin(), arr1.end(), [&arr2](const std::vector<int>& row1, const std::vector<int>& row2) {
        return calculateFit(row1, arr2) > calculateFit(row2, arr2);
    });

    // Print the sorted array
    for (const auto& row : arr1) {
        for (int val : row) {
            std::cout << val << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
