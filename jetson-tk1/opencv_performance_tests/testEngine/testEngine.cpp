#include "testEngine.h"

void TestEngine::runTest(TestBase* T)
{
  T->execute();
  T->results();
}
