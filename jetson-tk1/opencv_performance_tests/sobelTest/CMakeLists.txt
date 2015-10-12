cmake_minimum_required(VERSION 2.8)
project( SobelFilterPerfTest )
find_package( OpenCV REQUIRED )

add_executable( SobelTest sobelTest.cpp runTest.cpp )
target_link_libraries( SobelTest testEngine testBase ${OpenCV_LIBS} )
