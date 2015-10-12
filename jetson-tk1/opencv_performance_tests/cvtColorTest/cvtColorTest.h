#ifndef CVTCOLORTEST_H
#define CVTCOLORTEST_H

#include "../testBase/testBase.h"

class CvtColorTest : public TestBase
{
  public:
    CvtColorTest(char* _imageLoad);
    CvtColorTest(char* _imageLoad, uint16_t _numExec);
    //CvtColorTest(void);
    int setLoadImage(char* imageLoad);  // Return error on loading image
    //void execute(void);

  private:
    char* imageLoad_;
    void cvtColorGPU(void);
    cv::Mat srcImage_;
    void runGPU(void);
    void runCPU(void);
};

#endif
