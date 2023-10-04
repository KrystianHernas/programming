cmake_minimum_required(VERSION 3.0.0)
project(kalkulator VERSION 0.1.0 LANGUAGES C CXX)

include(CTest)
enable_testing()

add_executable(kalkulator main.cpp)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)

# include(GoogleTest)
# add_executable(mytests mytests.cpp) # add this executable
# include_directories(googletest/include) # this is so we can #include <gtest/gtest.h>
# add_subdirectory(googletest) # add googletest subdirectory
# target_link_libraries(mytests PRIVATE gtest) # link google test to this executable
# gtest_discover_tests(mytests) # discovers tests by asking the compiled test executable to enumerate its tests