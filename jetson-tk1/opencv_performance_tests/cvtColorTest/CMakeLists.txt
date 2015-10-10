cmake_minimum_required(VERSION 2.8)
project( CvtColorPerfTest )
find_package( OpenCV REQUIRED )

add_library(cvtColorTest SHARED cvtColorTest.cpp)
target_link_libraries( cvtColorTest testBase ${OpenCV_LIBS} )

add_executable( runTest runTest.cpp )
target_link_libraries(runTest cvtColorTest)
