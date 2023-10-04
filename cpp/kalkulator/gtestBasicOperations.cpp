#include <gtest/gtest.h>
#include "main.cpp"  // Include the header file for Calculator

// Create a test suite for Calculator
class CalculatorTest : public ::testing::Test {
protected:
    Calculator calc;
};

// Define tests
TEST_F(CalculatorTest, AddTest) {
    EXPECT_EQ(calc.calculate(2, 3, "a"), 5);  // 2 + 3 should be 5
}

TEST_F(CalculatorTest, SubtractTest) {
    EXPECT_EQ(calc.calculate(5, 2, "s"), 3); // 5 - 2 should be 3
}

void testExample() {
  // Your test code goes here
  ASSERT_TRUE(true); // Example assertion
  // TEST(TestCalc, TestPos) {
  //   Calc calculate;
  //   EXPECT_EQ(10.0, calculate.add(5.0, 5.0));
  //   EXPECT_EQ(9, calculate.mul(3, 3));
  //   EXPECT_EQ(9, calculate.div(27, 3));
  //   EXPECT_EQ(9, calculate.sub(12, 3));
  // }
  // TEST(TestCalc, TestNeg) {
  //   Calc calculate;
  //   EXPECT_EQ(-1.0, calculate.add(5.0, -6.0));
  //   EXPECT_EQ(-9, calculate.mul(3, -3));
  //   EXPECT_EQ(-9, calculate.div(27, -3));
  //   EXPECT_EQ(15, calculate.sub(12, -3));
  // }

  // TEST(TestCalc, TestZero) {
  //   Calc calculate;
  //   EXPECT_EQ(10.0, calculate.add(5.0, 0));
  //   EXPECT_EQ(9, calculate.mul(3, 0));
  //   EXPECT_EQ(, calculate.div(27, 0));
  //   EXPECT_EQ(12, calculate.sub(12, 0));
  // }
}

TEST(testExample, FirstTest) {
  ASSERT_TRUE(true); // Example assertion
}
