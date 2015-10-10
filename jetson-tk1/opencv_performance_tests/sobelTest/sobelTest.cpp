#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/gpu/gpu.hpp"
#include <stdlib.h>
#include <iostream>

using namespace cv;


cv::Mat& sobelCPU(cv::Mat& srcImage)
{
  static cv::Mat grayHostCPU;
  cv::cvtColor(srcImage, grayHostCPU, CV_RGB2GRAY);

  return grayHostCPU;
}


cv::Mat& sobelGPU(cv::Mat& srcImage)
{
  cv::gpu::GpuMat srcDevice(srcImage);
  cv::gpu::GpuMat grayDevice;
  cv::gpu::cvtColor(srcDevice, grayDevice, CV_RGB2GRAY);

  static cv::Mat grayHostGPU(grayDevice);

  return grayHostGPU;
}


/** @function main */
int main( int argc, char** argv )
{
  if(argc != 2) { std:: cout << "Invalid number of arguments\n"; }
  cv::Mat srcImage = imread(argv[1], CV_LOAD_IMAGE_COLOR);
  if( !srcImage.data )
  {
    std::cout << "Error on loading image data\n";
    return -1;
  }

  //std::stringstream ss;
  double t = (double)cv::getTickCount();  // Measure time.
  cv::Mat gray = cvtColorGPU(srcImage);
  double gpuExecTime = ((double)cv::getTickCount() - t)/cv::getTickFrequency();

  t = (double)cv::getTickCount();  // Measure time.
  gray = cvtColorGPU(srcImage);
  double cpuExecTime = ((double)cv::getTickCount() - t)/cv::getTickFrequency();

  std::cout << "Color Conversion Execution time results:\n" << "- CPU: " <<
    cpuExecTime << "\n" << "- GPU: " << gpuExecTime << std::endl;

  //namedWindow( "CVTCOLOR-GPU", CV_WINDOW_AUTOSIZE );
  //imshow( "CVTCOLOR-GPU", gray );
  //waitKey(0);
  return 0;
}
