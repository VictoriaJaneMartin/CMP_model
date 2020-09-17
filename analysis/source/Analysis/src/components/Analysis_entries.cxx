
#include "GaudiKernel/DeclareFactoryEntries.h"

#include "../AnalysisAlg.h"

DECLARE_ALGORITHM_FACTORY( AnalysisAlg )

DECLARE_FACTORY_ENTRIES( Analysis ) 
{
  DECLARE_ALGORITHM( AnalysisAlg );
}
