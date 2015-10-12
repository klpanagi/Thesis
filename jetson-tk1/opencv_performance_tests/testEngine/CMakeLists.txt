cmake_minimum_required(VERSION 2.8)
#include(${CMAKE_CURRENT_SOURCE_DIR}/maskFilter/CMakeLists.txt)
project( TestEngine )

add_library(testEngine SHARED testEngine.cpp)
#target_link_libraries(testEngine testBase)


