#include <iostream>

class Calculator {
private:
  std::string optionValue;

public:
  // Constructor
  Calculator() {
    std::cout
        << "This program allows to perform some basic calculation operations"
        << std::endl;
  }

  // Destructor
  ~Calculator() {
    // Cleanup code here
  }

  std::string selectOption() {
    std::cout << "What do you want to do? Insert letter for operation below. "
                 "List of available operations: "
              << std::endl;
    std::cout << "A - Addition. " << std::endl;
    std::cout << "S - Substraction. " << std::endl;
    std::cout << "M - Multiplication. " << std::endl;
    std::cout << "D - Division. " << std::endl;
    std::cout << "Or if you want to abort press n/N:" << std::endl;
    std::cin >> optionValue;
    return optionValue;
  }

  float inputNumber() {
    std::string input;
    float numberValue;
    std::cout << "Input number" << std::endl;
    std::cin >> input;
    try {
      size_t pos;
      numberValue = std::stof(input, &pos);

      if (pos != input.length()) {
        throw std::invalid_argument(
            "Input is not a valid floating-point number.");
      }
      std::cout << "You entered: " << input << std::endl;
    } catch (std::invalid_argument const &e) {
      std::cerr << e.what() << std::endl;
    } catch (std::out_of_range const &e) {
      std::cerr << "Input out of range for float type.\n";
    }
    return numberValue;
  }

  // calculate
  float calculate(float x, float y, std::string selectOption) {
    switch (tolower(selectOption[0])) {
    case 'a':
      return x + y;
    case 's':
      return x - y;
    case 'm':
      return x * y;
    case 'd':
      if (static_cast<int>(y) != 0) {
        return x / y;
      } else {
        std::cout << "ZERO DIV !!!" << std::endl;
        return 0;
      }
    default:
      return 0;
    }
  }

  // Member function to get private variable
  std::string getOptionValue() const { return optionValue; }

  // Member function to set private variable
  void setOptionValue(std::string value) { optionValue = value; }
};

int main() {
  Calculator Calculator;
  std::string option;
  do {
    option = Calculator.selectOption();
    Calculator.calculate(Calculator.inputNumber(), Calculator.inputNumber(),
                         option);
  } while (option != "n" && option != "N");

  return 0;
}