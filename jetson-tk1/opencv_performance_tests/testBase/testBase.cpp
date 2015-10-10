#include "testBase.h"

TestBase::TestBase()
{}


void TestBase::calcExecAvg(void)
{
  std::vector<double>::iterator itGPU, itCPU;
  for(itGPU = gpuExec_.begin(), itCPU = cpuExec_.begin();
      itGPU < gpuExec_.end(); itCPU++, itGPU++
     )
  {
    gpuAvg_ += *itGPU;
    cpuAvg_ += *itCPU;
  }
  gpuAvg_ = gpuAvg_ / gpuExec_.size();
  cpuAvg_ = cpuAvg_ / cpuExec_.size();
}


void TestBase::results(void)
{
  std::vector<double>::iterator itGPU, itCPU;
  //double avgCPU = 0.0, avgGPU = 0.0;
  // using double iteration for loop
  #ifdef REPORT_FULL
    for(itGPU = gpuExec_.begin(), itCPU = cpuExec_.begin();
        itGPU < gpuExec_.end(); itCPU++, itGPU++
       )
    {
      //avgGPU += *itGPU;
      //avgCPU += *itCPU;
      int pos = itGPU - gpuExec_.begin();
      std::cout << "\033[1;33m[Run " << pos << "]\033[0m " <<
        "Execution Time:\n  -GPU --> " << *itGPU << "\n  -CPU --> " <<
        *itCPU << std::endl;
    }
  #endif
  calcExecAvg();

  std::cout << "\n\n\033[1;32m-------------> Results:\033[0m\n" <<
    "- Number of sequential test runs: [" << numExec_ << "]\n" <<
    "- GPU Execution average: [" << gpuAvg_ << "]\n" <<
    "- CPU Execution average: [" << cpuAvg_ << "]\n";
}


