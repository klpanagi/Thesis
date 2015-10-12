#include "testBase.h"


TestBase::TestBase()
{
  initGPU();
}

void TestBase::initGPU(void)
{
  int cudaDevices = 0;
  if( ! (cudaDevices = cv::gpu::getCudaEnabledDeviceCount()) )
  {
    std::cout << "No cuda enabled device found\n";
    std::exit(-1);
  }
  cv::gpu::setDevice(0);
  cv::gpu::DeviceInfo deviceInfo(0);

  std::cout << "Nvidia cuda enabled device information:\n" <<
    "---------------------------------------" << std::endl <<
    "-Name: " << deviceInfo.name() << std::endl <<
    "-Version: " << deviceInfo.majorVersion() << " -- " << deviceInfo.minorVersion() << std::endl <<
    "-MultiProcessorCount: " << deviceInfo.multiProcessorCount() << std::endl <<
    "-Total Memory: " << deviceInfo.totalMemory() << std::endl;
}


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
  #ifdef REPORT_FULL
    // using double iteration for loop
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


void TestBase::execute(void)
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
}
