#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/gpu/gpu.hpp"

#include "../testBase/testBase.h"

using namespace cv;


class CvtColorTest : public TestBase
{
  public:
    CvtColorTest(char* _imageLoad);
    CvtColorTest(char* _imageLoad, uint16_t _numExec);
    //CvtColorTest(void);
    int setLoadImage(char* imageLoad);  // Return error on loading image
    void execute(void);

  private:
    char* imageLoad_;
    void cvtColorGPU(void);
    cv::Mat srcImage_;
    void runGPU(void);
    void runCPU(void);
};


CvtColorTest::CvtColorTest(char* _imageLoad)
  :
    imageLoad_(_imageLoad)
{
  srcImage_ = imread(imageLoad_, CV_LOAD_IMAGE_COLOR);
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
  srcImage_ = imread(imageLoad_, CV_LOAD_IMAGE_COLOR);
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


void CvtColorTest::execute(void)
{
    int runIndex = 0;
    double t1, t2, execTimeCPU, execTimeGPU;

    for(int ii = 0; ii < numExec_; ii++)
    {
      t1 = (double)cv::getTickCount();  // Measure time.
      runCPU();
      execTimeCPU = ((double)cv::getTickCount() - t1)/cv::getTickFrequency();
      t2 = (double)cv::getTickCount();  // Measure time.
      runGPU();
      execTimeGPU = ((double)cv::getTickCount() - t2)/cv::getTickFrequency();

      gpuExec_.push_back(execTimeGPU);
      cpuExec_.push_back(execTimeCPU);
    }
    //std::cout << "\033[1;33m[Run " << runIndex << "]\033[0m " <<
      //"Execution Time:\n  -GPU --> " << execTimeGPU << "\n  -CPU --> " <<
      //execTimeCPU << std::endl;
}

