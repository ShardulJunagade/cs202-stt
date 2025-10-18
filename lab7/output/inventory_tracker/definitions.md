| Definition ID | Variable | Block | Line | Statement |
|---------------|----------|-------|------|-----------|
| D1 | categories | B0 | 2 | `int categories = 8;` |
| D2 | stores | B0 | 3 | `int stores = 12;` |
| D3 | weeks | B0 | 4 | `int weeks = 10;` |
| D4 | stock | B0 | 5 | `int stock[8][12][10];` |
| D5 | reorderThreshold | B0 | 6 | `int reorderThreshold[8];` |
| D6 | reorderCount | B0 | 7 | `int reorderCount[8];` |
| D7 | totalStock | B0 | 8 | `int totalStock = 0;` |
| D8 | totalDeficit | B0 | 9 | `int totalDeficit = 0;` |
| D9 | totalSurplus | B0 | 10 | `int totalSurplus = 0;` |
| D10 | outOfStock | B0 | 11 | `int outOfStock = 0;` |
| D11 | overStocked | B0 | 12 | `int overStocked = 0;` |
| D12 | balanced | B0 | 13 | `int balanced = 0;` |
| D13 | storeIndex | B0 | 14 | `int storeIndex = 0;` |
| D14 | categoryIndex | B0 | 15 | `int categoryIndex = 0;` |
| D15 | weekIndex | B0 | 16 | `int weekIndex = 0;` |
| D16 | forecast | B0 | 17 | `int forecast[8][12];` |
| D17 | demandSpike | B0 | 18 | `int demandSpike[8][12];` |
| D18 | demandDrop | B0 | 19 | `int demandDrop[8][12];` |
| D19 | movingAvg | B0 | 20 | `int movingAvg[8][12];` |
| D20 | trendGrowth | B0 | 21 | `int trendGrowth = 0;` |
| D21 | trendDecline | B0 | 22 | `int trendDecline = 0;` |
| D22 | trendStable | B0 | 23 | `int trendStable = 0;` |
| D23 | highestStock | B0 | 24 | `int highestStock = 0;` |
| D24 | lowestStock | B0 | 25 | `int lowestStock = 0;` |
| D25 | cumulativeVariance | B0 | 26 | `int cumulativeVariance = 0;` |
| D26 | maxVarianceCategory | B0 | 27 | `int maxVarianceCategory = 0;` |
| D27 | minVarianceCategory | B0 | 28 | `int minVarianceCategory = 0;` |
| D28 | tempVariance | B0 | 29 | `int tempVariance = 0;` |
| D29 | stockChange | B0 | 30 | `int stockChange = 0;` |
| D30 | previousStock | B0 | 31 | `int previousStock = 0;` |
| D31 | sameTrendCount | B0 | 32 | `int sameTrendCount = 0;` |
| D32 | trendDirection | B0 | 33 | `int trendDirection = 0;` |
| D33 | lastTrendDirection | B0 | 34 | `int lastTrendDirection = 0;` |
| D34 | longestGrowthStreak | B0 | 35 | `int longestGrowthStreak = 0;` |
| D35 | longestDeclineStreak | B0 | 36 | `int longestDeclineStreak = 0;` |
| D36 | currentGrowthStreak | B0 | 37 | `int currentGrowthStreak = 0;` |
| D37 | currentDeclineStreak | B0 | 38 | `int currentDeclineStreak = 0;` |
| D38 | restockPlan | B0 | 39 | `int restockPlan[8];` |
| D39 | clearancePlan | B0 | 40 | `int clearancePlan[8];` |
| D40 | auditFlag | B0 | 41 | `int auditFlag[8];` |
| D41 | exceptionCount | B0 | 42 | `int exceptionCount = 0;` |
| D42 | balancedWeeks | B0 | 43 | `int balancedWeeks = 0;` |
| D43 | balancedStores | B0 | 44 | `int balancedStores = 0;` |
| D44 | totalStock | B6 | 58 | `totalStock += stock[categoryIndex][storeIndex][weekIndex];` |
| D45 | totalDeficit | B8 | 60 | `totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex];` |
| D46 | totalSurplus | B8 | 63 | `totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - reorderThreshold[categoryIndex] * 2;` |
| D47 | highestStock | B8 | 69 | `highestStock = totalStock / (categories * stores * weeks);` |
| D48 | lowestStock | B8 | 70 | `lowestStock = highestStock;` |
| D49 | tempVariance | B10 | 73 | `tempVariance = 0;` |
| D50 | runningTotal | B12 | 75 | `int runningTotal = 0;` |
| D51 | runningTotal | B14 | 77 | `runningTotal += stock[categoryIndex][storeIndex][weekIndex];` |
| D52 | highestStock | B18 | 83 | `highestStock = stock[categoryIndex][storeIndex][weekIndex];` |
| D53 | lowestStock | B20 | 86 | `lowestStock = stock[categoryIndex][storeIndex][weekIndex];` |
| D54 | previousStock | B22 | 90 | `previousStock = stock[categoryIndex][storeIndex][weekIndex - 1];` |
| D55 | stockChange | B22 | 91 | `stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock;` |
| D56 | trendDirection | B26 | 99 | `trendDirection = 1;` |
| D57 | currentGrowthStreak | B26 | 100 | `currentGrowthStreak += 1;` |
| D58 | currentDeclineStreak | B26 | 101 | `currentDeclineStreak = 0;` |
| D59 | trendDirection | B26 | 103 | `trendDirection = -1;` |
| D60 | currentDeclineStreak | B26 | 104 | `currentDeclineStreak += 1;` |
| D61 | currentGrowthStreak | B26 | 105 | `currentGrowthStreak = 0;` |
| D62 | trendDirection | B26 | 107 | `trendDirection = 0;` |
| D63 | currentGrowthStreak | B26 | 108 | `currentGrowthStreak = 0;` |
| D64 | currentDeclineStreak | B26 | 109 | `currentDeclineStreak = 0;` |
| D65 | sameTrendCount | B28 | 113 | `sameTrendCount += 1;` |
| D66 | sameTrendCount | B28 | 115 | `sameTrendCount = 1;` |
| D67 | longestGrowthStreak | B30 | 119 | `longestGrowthStreak = currentGrowthStreak;` |
| D68 | longestDeclineStreak | B32 | 122 | `longestDeclineStreak = currentDeclineStreak;` |
| D69 | lastTrendDirection | B32 | 125 | `lastTrendDirection = trendDirection;` |
| D70 | runningTotal | B32 | 128 | `runningTotal += stock[categoryIndex][storeIndex][weekIndex];` |
| D71 | balancedStores | B34 | 132 | `balancedStores += 1;` |
| D72 | exceptionCount | B38 | 144 | `exceptionCount += 1;` |
| D73 | tempVariance | B38 | 147 | `tempVariance = highestStock - lowestStock;` |
| D74 | cumulativeVariance | B38 | 148 | `cumulativeVariance += tempVariance;` |
| D75 | maxVarianceCategory | B40 | 150 | `maxVarianceCategory = tempVariance;` |
| D76 | minVarianceCategory | B42 | 153 | `minVarianceCategory = tempVariance;` |
| D77 | weekBalanced | B44 | 158 | `int weekBalanced = 0;` |
| D78 | totalWeekStock | B46 | 160 | `int totalWeekStock = 0;` |
| D79 | totalWeekStock | B48 | 162 | `totalWeekStock += stock[categoryIndex][storeIndex][weekIndex];` |
| D80 | weekBalanced | B50 | 165 | `weekBalanced += 1;` |
| D81 | balancedWeeks | B52 | 169 | `balancedWeeks += 1;` |
| D82 | totalCategoryStock | B54 | 174 | `int totalCategoryStock = 0;` |
| D83 | totalCategoryDeficit | B54 | 175 | `int totalCategoryDeficit = 0;` |
| D84 | totalCategorySurplus | B54 | 176 | `int totalCategorySurplus = 0;` |
| D85 | totalCategoryStock | B57 | 179 | `totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex];` |
| D86 | totalCategoryDeficit | B59 | 181 | `totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex];` |
| D87 | totalCategorySurplus | B61 | 184 | `totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - reorderThreshold[categoryIndex] * 2;` |
| D88 | trendDecline | B63 | 190 | `trendDecline += 1;` |
| D89 | trendGrowth | B63 | 192 | `trendGrowth += 1;` |
| D90 | trendStable | B63 | 194 | `trendStable += 1;` |
| D91 | outOfStock | B65 | 198 | `outOfStock += 1;` |
| D92 | overStocked | B65 | 200 | `overStocked += 1;` |
| D93 | balanced | B65 | 202 | `balanced += 1;` |
| D94 | sameTrendCount | B67 | 207 | `sameTrendCount += trendGrowth;` |
| D95 | sameTrendCount | B67 | 209 | `sameTrendCount += trendDecline;` |
| D96 | sameTrendCount | B67 | 211 | `sameTrendCount += trendStable;` |
| D97 | balanced | B71 | 223 | `balanced = balanced - exceptionCount;` |
| D98 | balanced | B73 | 227 | `balanced += 1;` |
| D99 | overStocked | B73 | 229 | `overStocked += 1;` |
| D100 | trendStable | B75 | 233 | `trendStable += 1;` |
| D101 | trendDecline | B75 | 235 | `trendDecline += 1;` |