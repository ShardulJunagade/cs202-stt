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
| D44 | categoryIndex | B0 | 46 | `categoryIndex = 0;` |
| D45 | categoryIndex | B3 | 46 | `categoryIndex++;` |
| D46 | categoryIndex | B2 | 54 | `categoryIndex = 0;` |
| D47 | storeIndex | B8 | 55 | `storeIndex = 0;` |
| D48 | weekIndex | B12 | 56 | `weekIndex = 0;` |
| D49 | totalStock | B16 | 58 | `totalStock += stock[categoryIndex][storeIndex][weekIndex];` |
| D50 | totalDeficit | B18 | 60 | `totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex];` |
| D51 | totalSurplus | B19 | 63 | `totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - reorderThreshold[categoryIndex] * 2;` |
| D52 | weekIndex | B15 | 56 | `weekIndex++;` |
| D53 | storeIndex | B11 | 55 | `storeIndex++;` |
| D54 | categoryIndex | B7 | 54 | `categoryIndex++;` |
| D55 | highestStock | B6 | 69 | `highestStock = totalStock / (categories * stores * weeks);` |
| D56 | lowestStock | B6 | 70 | `lowestStock = highestStock;` |
| D57 | categoryIndex | B6 | 72 | `categoryIndex = 0;` |
| D58 | tempVariance | B24 | 73 | `tempVariance = 0;` |
| D59 | storeIndex | B24 | 74 | `storeIndex = 0;` |
| D60 | runningTotal | B28 | 75 | `int runningTotal = 0;` |
| D61 | weekIndex | B28 | 76 | `weekIndex = 0;` |
| D62 | runningTotal | B32 | 77 | `runningTotal += stock[categoryIndex][storeIndex][weekIndex];` |
| D63 | highestStock | B37 | 83 | `highestStock = stock[categoryIndex][storeIndex][weekIndex];` |
| D64 | lowestStock | B40 | 86 | `lowestStock = stock[categoryIndex][storeIndex][weekIndex];` |
| D65 | previousStock | B43 | 90 | `previousStock = stock[categoryIndex][storeIndex][weekIndex - 1];` |
| D66 | stockChange | B43 | 91 | `stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock;` |
| D67 | trendDirection | B49 | 99 | `trendDirection = 1;` |
| D68 | currentGrowthStreak | B49 | 100 | `currentGrowthStreak += 1;` |
| D69 | currentDeclineStreak | B49 | 101 | `currentDeclineStreak = 0;` |
| D70 | trendDirection | B50 | 103 | `trendDirection = -1;` |
| D71 | currentDeclineStreak | B50 | 104 | `currentDeclineStreak += 1;` |
| D72 | currentGrowthStreak | B50 | 105 | `currentGrowthStreak = 0;` |
| D73 | trendDirection | B51 | 107 | `trendDirection = 0;` |
| D74 | currentGrowthStreak | B51 | 108 | `currentGrowthStreak = 0;` |
| D75 | currentDeclineStreak | B51 | 109 | `currentDeclineStreak = 0;` |
| D76 | sameTrendCount | B53 | 113 | `sameTrendCount += 1;` |
| D77 | sameTrendCount | B54 | 115 | `sameTrendCount = 1;` |
| D78 | longestGrowthStreak | B57 | 119 | `longestGrowthStreak = currentGrowthStreak;` |
| D79 | longestDeclineStreak | B60 | 122 | `longestDeclineStreak = currentDeclineStreak;` |
| D80 | lastTrendDirection | B61 | 125 | `lastTrendDirection = trendDirection;` |
| D81 | runningTotal | B62 | 128 | `runningTotal += stock[categoryIndex][storeIndex][weekIndex];` |
| D82 | weekIndex | B31 | 76 | `weekIndex++;` |
| D83 | balancedStores | B64 | 132 | `balancedStores += 1;` |
| D84 | storeIndex | B27 | 74 | `storeIndex++;` |
| D85 | exceptionCount | B71 | 144 | `exceptionCount += 1;` |
| D86 | tempVariance | B72 | 147 | `tempVariance = highestStock - lowestStock;` |
| D87 | cumulativeVariance | B72 | 148 | `cumulativeVariance += tempVariance;` |
| D88 | maxVarianceCategory | B74 | 150 | `maxVarianceCategory = tempVariance;` |
| D89 | minVarianceCategory | B77 | 153 | `minVarianceCategory = tempVariance;` |
| D90 | categoryIndex | B23 | 72 | `categoryIndex++;` |
| D91 | weekIndex | B22 | 157 | `weekIndex = 0;` |
| D92 | weekBalanced | B82 | 158 | `int weekBalanced = 0;` |
| D93 | categoryIndex | B82 | 159 | `categoryIndex = 0;` |
| D94 | totalWeekStock | B86 | 160 | `int totalWeekStock = 0;` |
| D95 | storeIndex | B86 | 161 | `storeIndex = 0;` |
| D96 | totalWeekStock | B90 | 162 | `totalWeekStock += stock[categoryIndex][storeIndex][weekIndex];` |
| D97 | storeIndex | B89 | 161 | `storeIndex++;` |
| D98 | weekBalanced | B92 | 165 | `weekBalanced += 1;` |
| D99 | categoryIndex | B85 | 159 | `categoryIndex++;` |
| D100 | balancedWeeks | B95 | 169 | `balancedWeeks += 1;` |
| D101 | weekIndex | B81 | 157 | `weekIndex++;` |
| D102 | categoryIndex | B80 | 173 | `categoryIndex = 0;` |
| D103 | totalCategoryStock | B100 | 174 | `int totalCategoryStock = 0;` |
| D104 | totalCategoryDeficit | B100 | 175 | `int totalCategoryDeficit = 0;` |
| D105 | totalCategorySurplus | B100 | 176 | `int totalCategorySurplus = 0;` |
| D106 | storeIndex | B100 | 177 | `storeIndex = 0;` |
| D107 | weekIndex | B104 | 178 | `weekIndex = 0;` |
| D108 | totalCategoryStock | B108 | 179 | `totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex];` |
| D109 | totalCategoryDeficit | B110 | 181 | `totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex];` |
| D110 | totalCategorySurplus | B113 | 184 | `totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - reorderThreshold[categoryIndex] * 2;` |
| D111 | weekIndex | B107 | 178 | `weekIndex++;` |
| D112 | storeIndex | B103 | 177 | `storeIndex++;` |
| D113 | trendDecline | B116 | 190 | `trendDecline += 1;` |
| D114 | trendGrowth | B117 | 192 | `trendGrowth += 1;` |
| D115 | trendStable | B118 | 194 | `trendStable += 1;` |
| D116 | outOfStock | B120 | 198 | `outOfStock += 1;` |
| D117 | overStocked | B121 | 200 | `overStocked += 1;` |
| D118 | balanced | B122 | 202 | `balanced += 1;` |
| D119 | categoryIndex | B99 | 173 | `categoryIndex++;` |
| D120 | sameTrendCount | B124 | 207 | `sameTrendCount += trendGrowth;` |
| D121 | sameTrendCount | B125 | 209 | `sameTrendCount += trendDecline;` |
| D122 | sameTrendCount | B126 | 211 | `sameTrendCount += trendStable;` |
| D123 | balanced | B132 | 223 | `balanced = balanced - exceptionCount;` |
| D124 | balanced | B135 | 227 | `balanced += 1;` |
| D125 | overStocked | B136 | 229 | `overStocked += 1;` |
| D126 | trendStable | B139 | 233 | `trendStable += 1;` |
| D127 | trendDecline | B140 | 235 | `trendDecline += 1;` |