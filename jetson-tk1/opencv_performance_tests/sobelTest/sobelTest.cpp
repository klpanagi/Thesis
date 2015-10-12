#include "sobelTest.h"

SobelTest::SobelTest(char* _imageLoad)
  :
    imageLoad_(_imageLoad)
{
  srcImage_ = cv::imread(imageLoad_, CV_LOAD_IMAGE_COLOR);
  numExec_ = 1;
  if( !srcImage_.data )
  {
    std::cout << "Error on loading image data\n";
    throw "Error on loading image data";
  }
}


SobelTest::SobelTest(char* _imageLoad, uint16_t _numExec)
  :
    imageLoad_(_imageLoad),
    ddepth_(CV_16S),
    scale_(1),
    delta_(0)
{
  numExec_ = _numExec;
  srcImage_ = cv::imread(imageLoad_, CV_LOAD_IMAGE_COLOR);
  if( !srcImage_.data )
  {
    std::cout << "Error on loading image data\n";
    throw "Error on loading image data";
  }
}


void SobelTest::runGPU(void)
{
  // Transfer source image to the GPU.
  cv::gpu::GpuMat srcDevice(srcImage_);
  cv::gpu::GpuMat grayDevice;
  cv::gpu::cvtColor(srcDevice, grayDevice, CV_RGB2GRAY);

  cv::gpu::GpuMat gradX, gradY;

  // Gradient X
  cv::gpu::Sobel( grayDevice, gradX, ddepth_, 1, 0, 3, scale_, delta_, cv::BORDER_DEFAULT );

  // Gradient Y. Perform with ddepth=CV_16S for higher accuracy on
  // convolution operations. Sobel uses a 3x3 kernel.
  cv::gpu::Sobel( grayDevice, gradY, ddepth_, 1, 0, 3, scale_, delta_, cv::BORDER_DEFAULT );

  // Calculate the absolute values of gradX and gradY.
  cv::gpu::abs( gradY, gradY );
  cv::gpu::abs( gradX, gradX );

  gradX.convertTo(gradX, CV_8U);
  gradY.convertTo(gradY, CV_8U);

  cv::gpu::GpuMat resImageGPU;

  cv::gpu::addWeighted( gradX, 0.5, gradY, 0.5, 0, resImageGPU);
  resImageGPU.download(resImageGPU_);
  //resImageGPU_.convertTo(resImageGPU_, CV_8U, 1, 0);
}


void SobelTest::runCPU(void)
{
  cv::Mat grayDevice;
  cvtColor( srcImage_, grayDevice, CV_RGB2GRAY );
  /// Generate grad_x and grad_y
  cv::Mat gradX, gradY;
  cv::Mat absGradX, absGradY;

  // Gradient X
  cv::Sobel( grayDevice, gradX, ddepth_, 1, 0, 3, scale_, delta_, cv::BORDER_DEFAULT );
  cv::convertScaleAbs( gradX, absGradX );

  // Gradient Y
  cv::Sobel( grayDevice, gradY, ddepth_, 1, 0, 3, scale_, delta_, cv::BORDER_DEFAULT );
  cv::convertScaleAbs( gradY, absGradY );

  cv::addWeighted( absGradX, 0.5, absGradY, 0.5, 0, resImageCPU_ );
}


void SobelTest::showImage(void)
{
  char* inputWindow = "Input Image (Preprocessed)";
  char* outputCPUWindow = "Sobel Filtered Image (CPU Routines)";
  char* outputGPUWindow = "Sobel Filtered Image (GPU Routines)";
  cv::namedWindow( inputWindow, CV_WINDOW_AUTOSIZE );
  cv::namedWindow( outputCPUWindow, CV_WINDOW_AUTOSIZE );
  cv::namedWindow( outputGPUWindow, CV_WINDOW_AUTOSIZE );

  cv::imshow( inputWindow, srcImage_ );
  cv::imshow( outputCPUWindow, resImageCPU_ );
  cv::imshow( outputGPUWindow, resImageGPU_ );

  cv::waitKey(0);
}
