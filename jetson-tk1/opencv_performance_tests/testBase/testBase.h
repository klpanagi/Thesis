#ifndef TESTBASE_H
#define TESTBASE_H
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <cstdint>

#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/gpu/gpu.hpp"

class TestBase
{
  public:
    TestBase();
    void results(void);
    virtual void execute(void);
    virtual ~TestBase(void){};
    virtual void runGPU(void) = 0;
    virtual void runCPU(void) = 0;

  protected:
    std::vector<double> gpuExec_;
    std::vector<double> cpuExec_;
    uint16_t numExec_;
    double gpuAvg_;
    double cpuAvg_;

  private:
    void calcExecAvg(void);
    void initGPU(void);
};

#endif
