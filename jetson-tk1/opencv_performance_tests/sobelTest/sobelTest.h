#ifndef SOBELTEST_H
#define SOBELTEST_H

#include "../testBase/testBase.h"

class SobelTest: public TestBase
{
  public:
    SobelTest(char* _imageLoad);
    SobelTest(char* _imageLoad, uint16_t _numExec);
    int setLoadImage(char* imageLoad);  // Return error on loading image
    void showImage(void);

  private:
    int ddepth_;
    int scale_;
    int delta_;
    char* imageLoad_;
    cv::Mat srcImage_;
    cv::Mat resImageCPU_;
    cv::Mat resImageGPU_;
    void runGPU(void);
    void runCPU(void);
};

#endif
