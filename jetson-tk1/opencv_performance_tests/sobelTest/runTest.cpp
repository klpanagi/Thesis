#include "sobelTest.h"
#include "../testEngine/testEngine.h"

using namespace cv;

int parseInt(char* arg)
{
  std::stringstream ss;
  int value;
  ss << arg;
  ss >> value;
  return value;
}

/** @function main */
int main( int argc, char** argv )
{
  if(argc < 2)
  {
    std:: cout << "Invalid number of arguments\n";
    return 1;
  }
  int numRuns = (argc == 2) ? 1 :  parseInt(argv[2]);

  SobelTest test(argv[1], numRuns);
  TestEngine::runTest(&test);
  test.showImage();

  return 0;
}
