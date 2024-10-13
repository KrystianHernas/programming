#include "judge.h"
#include <fstream> // Include for file handling
#include <iostream>

// Define DEBUG flag: set to true to enable debug logs, false to disable
const bool DEBUG = false;

int count;
const uint8_t rows = 10, columns = 4;
int favorite[rows][columns];
int available[columns];

void Judge::run(IPIE *solution) {
  std::string inputFileName = "input.txt", outputFileName = "output.txt";
  // Open the input file
  std::ifstream infile(inputFileName);
  if (!infile) {
    std::cerr << "Error opening input file: " << inputFileName << std::endl;
    return;
  } else if (DEBUG) {
    std::cerr << "Input file " << inputFileName << " opened successfully."
              << std::endl;
  }

  // Read count
  infile >> count;
  if (DEBUG) {
    std::cerr << "Read count: " << count << std::endl;
  }

  // Debug to ensure count is valid
  if (count < 1 || count > 10) {
    std::cerr << "Error: Invalid count value =" << count << std::endl;
    return;
  }

  // Read the array available
  for (int i = 0; i < rows; i++) {
    infile >> favorite[i][0] >> favorite[i][1] >> favorite[i][2] >>
        favorite[i][3];
    if (DEBUG) {
      std::cerr << "Item " << i << ": favorite[i][0]= " << favorite[i][0]
                << ", favorite[i][1] = " << favorite[i][1]
                << ", favorite[i][2] = " << favorite[i][2]
                << ", favorite[i][3] = " << favorite[i][3] << std::endl;
    }

    // Debug invalid item values
    if ((favorite[i][0] <= 0 && favorite[i][0] >= 20) ||
        (favorite[i][1] <= 0 && favorite[i][1] >= 20) ||
        (favorite[i][2] <= 0 && favorite[i][2] >= 20) ||
        (favorite[i][3] <= 0 && favorite[i][3] >= 20)) {
      std::cerr << "Error: Invalid value or weight at index " << i
                << ". value = " << favorite[i] << ", weight = " << favorite[i]
                << std::endl;
      return;
    }
  }

  // Read the array favorite
  for (int i = 0; i < rows; i++) {
    infile >> favorite[i][0] >> favorite[i][1] >> favorite[i][2] >>
        favorite[i][3];
    if (DEBUG) {
      std::cerr << "Item " << i << ": favorite[i][0]= " << favorite[i][0]
                << ", favorite[i][1] = " << favorite[i][1]
                << ", favorite[i][2] = " << favorite[i][2]
                << ", favorite[i][3] = " << favorite[i][3] << std::endl;
    }

    // Debug invalid item values
    if ((favorite[i][0] <= 0 && favorite[i][0] >= 20) ||
        (favorite[i][1] <= 0 && favorite[i][1] >= 20) ||
        (favorite[i][2] <= 0 && favorite[i][2] >= 20) ||
        (favorite[i][3] <= 0 && favorite[i][3] >= 20)) {
      std::cerr << "Error: Invalid value or weight at index " << i
                << ". value = " << favorite[i] << ", weight = " << favorite[i]
                << std::endl;
      return;
    }
  }

  // Call the solution's getMaxPierniczkiCount method
  int count = 3;
  int favorite[3][4] = {{0, 1, 2, 3}, {0, 1, 2, 4}, {0, 1, 2, 5}};
  int available[4] = {1, 2, 3, 4};
  int result = solution->getMaxPierniczkiCount(count, favorite, available);
  // std::cout << "Solution computed result: " << result << std::endl;

  // Open the output file
  std::ifstream outfile(outputFileName);
  if (!outfile) {
    std::cerr << "Error opening output file: " << outputFileName << std::endl;
    return;
  } else if (DEBUG) {
    std::cerr << "Output file " << outputFileName << " opened successfully."
              << std::endl;
  }

  // Read expected result from output file
  int expectedResult;
  outfile >> expectedResult;

  if (DEBUG) {
    std::cerr << "Expected result from output file: " << expectedResult
              << std::endl;
  }

  // Compare the computed result with the expected result
  // if (result == expectedResult) {
  //   std::cout << "Success! The result matches the expected output."
  //             << std::endl;
  // } else {
  //   std::cout << "Mismatch! Computed result: " << result
  //             << ", Expected result: " << expectedResult << std::endl;
  // }

  // Close the files
  infile.close();
  outfile.close();

  if (DEBUG) {
    std::cerr << "Files closed." << std::endl;
  }
}
