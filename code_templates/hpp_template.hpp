#ifndef EXAMPLE_HPP
#define EXAMPLE_HPP

#include <iostream>   // For input/output operations
#include <string>     // For string manipulation
#include <vector>     // For dynamic arrays
#include <algorithm>  // For algorithms and generic functions
#include <cmath>      // For mathematical functions
#include <stdexcept>  // For exception handling
#include <fstream>    // For file input/output
#include <iomanip>    // For formatting output
#include <sstream>    // For string stream processing
#include <utility>    // For various utilities
#include <chrono>     // For time-related operations (C++11 and later)
#include <functional> // For function objects (C++11 and later)
#include <memory>     // For dynamic memory management (C++11 and later)

class ExampleClass {
private:
    int privateVariable;

public:
    // Constructor
    ExampleClass(int initialValue);

    // Destructor
    ~ExampleClass();

    // Getter for privateVariable
    int getPrivateVariable() const;

    // Setter for privateVariable
    void setPrivateVariable(int value);
};

#endif // EXAMPLE_HPP