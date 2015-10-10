#include <iostream>
#include <stdlib.h>
#include <vector>
#include <cstdint>


class TestBase
{
  public:
    TestBase();
    void results(void);
    virtual ~TestBase(void){};

  protected:
    std::vector<double> gpuExec_;
    std::vector<double> cpuExec_;
    uint16_t numExec_;
    double gpuAvg_;
    double cpuAvg_;

  private:
    void calcExecAvg(void);
};


