#include "cvtColorTest.h"

//using namespace cv;

CvtColorTest::CvtColorTest(char* _imageLoad)
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


CvtColorTest::CvtColorTest(char* _imageLoad, uint16_t _numExec)
  :
    imageLoad_(_imageLoad)
{
  numExec_ = _numExec;
  srcImage_ = cv::imread(imageLoad_, CV_LOAD_IMAGE_COLOR);
  if( !srcImage_.data )
  {
    std::cout << "Error on loading image data\n";
    throw "Error on loading image data";
  }
}


void CvtColorTest::runGPU(void)
{
  cv::gpu::GpuMat srcDevice(srcImage_);
  cv::gpu::GpuMat grayDevice;
  cv::gpu::cvtColor(srcDevice, grayDevice, CV_RGB2GRAY);
  cv::Mat grayHostGPU(grayDevice);
}


void CvtColorTest::runCPU(void)
{
  cv::Mat grayHostCPU;
  cv::cvtColor(srcImage_, grayHostCPU, CV_RGB2GRAY);
}
