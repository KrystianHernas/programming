#include <iostream>

class MyClass {
private:
    int myPrivateVariable;

public:
    // Constructor
    MyClass(int initialValue) : myPrivateVariable(initialValue) {
        // Initialization code here     
    }

    // Destructor
    ~MyClass() {
        // Cleanup code here
    }

    // Member function to get private variable
    int getPrivateVariable() const {
        return myPrivateVariable;
    }

    // Member function to set private variable
    void setPrivateVariable(int value) {
        myPrivateVariable = value;
    }
};

int main() {
    // Create an instance of MyClass
    MyClass myObject(42);

    // Use member functions
    int value = myObject.getPrivateVariable();
    std::cout << "Value: " << value << std::endl;

    myObject.setPrivateVariable(99);
    value = myObject.getPrivateVariable();
    std::cout << "Updated Value: " << value << std::endl;

    return 0;
}