cmake_minimum_required(VERSION 2.8)
#include(${CMAKE_CURRENT_SOURCE_DIR}/maskFilter/CMakeLists.txt)
project( TestBaseClass )

add_library( testBase SHARED testBase.cpp )
target_link_libraries( testBase )
