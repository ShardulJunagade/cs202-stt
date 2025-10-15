| Definition ID | Variable | Block | Line | Statement |
|---------------|----------|-------|------|-----------|
| D1 | categories | B0 | 2 | `int categories = 8` |
| D2 | stores | B0 | 3 | `int stores = 12` |
| D3 | weeks | B0 | 4 | `int weeks = 10` |
| D4 | stock | B0 | 5 | `int stock[8][12][10]` |
| D5 | reorderThreshold | B0 | 6 | `int reorderThreshold[8]` |
| D6 | reorderCount | B0 | 7 | `int reorderCount[8]` |
| D7 | totalStock | B0 | 8 | `int totalStock = 0` |
| D8 | totalDeficit | B0 | 9 | `int totalDeficit = 0` |
| D9 | totalSurplus | B0 | 10 | `int totalSurplus = 0` |
| D10 | outOfStock | B0 | 11 | `int outOfStock = 0` |
| D11 | overStocked | B0 | 12 | `int overStocked = 0` |
| D12 | balanced | B0 | 13 | `int balanced = 0` |
| D13 | storeIndex | B0 | 14 | `int storeIndex = 0` |
| D14 | categoryIndex | B0 | 15 | `int categoryIndex = 0` |
| D15 | weekIndex | B0 | 16 | `int weekIndex = 0` |
| D16 | forecast | B0 | 17 | `int forecast[8][12]` |
| D17 | demandSpike | B0 | 18 | `int demandSpike[8][12]` |
| D18 | demandDrop | B0 | 19 | `int demandDrop[8][12]` |
| D19 | movingAvg | B0 | 20 | `int movingAvg[8][12]` |
| D20 | trendGrowth | B0 | 21 | `int trendGrowth = 0` |
| D21 | trendDecline | B0 | 22 | `int trendDecline = 0` |
| D22 | trendStable | B0 | 23 | `int trendStable = 0` |
| D23 | highestStock | B0 | 24 | `int highestStock = 0` |
| D24 | lowestStock | B0 | 25 | `int lowestStock = 0` |
| D25 | cumulativeVariance | B0 | 26 | `int cumulativeVariance = 0` |
| D26 | maxVarianceCategory | B0 | 27 | `int maxVarianceCategory = 0` |
| D27 | minVarianceCategory | B0 | 28 | `int minVarianceCategory = 0` |
| D28 | tempVariance | B0 | 29 | `int tempVariance = 0` |
| D29 | stockChange | B0 | 30 | `int stockChange = 0` |
| D30 | previousStock | B0 | 31 | `int previousStock = 0` |
| D31 | sameTrendCount | B0 | 32 | `int sameTrendCount = 0` |
| D32 | trendDirection | B0 | 33 | `int trendDirection = 0` |
| D33 | lastTrendDirection | B0 | 34 | `int lastTrendDirection = 0` |
| D34 | longestGrowthStreak | B0 | 35 | `int longestGrowthStreak = 0` |
| D35 | longestDeclineStreak | B0 | 36 | `int longestDeclineStreak = 0` |
| D36 | currentGrowthStreak | B0 | 37 | `int currentGrowthStreak = 0` |
| D37 | currentDeclineStreak | B0 | 38 | `int currentDeclineStreak = 0` |
| D38 | restockPlan | B0 | 39 | `int restockPlan[8]` |
| D39 | clearancePlan | B0 | 40 | `int clearancePlan[8]` |
| D40 | auditFlag | B0 | 41 | `int auditFlag[8]` |
| D41 | exceptionCount | B0 | 42 | `int exceptionCount = 0` |
| D42 | balancedWeeks | B0 | 43 | `int balancedWeeks = 0` |
| D43 | balancedStores | B0 | 44 | `int balancedStores = 0` |
| D44 | categoryIndex | B0 | 46 | `categoryIndex = 0` |
| D45 | reorderThreshold | B4 | 47 | `reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| D46 | reorderCount | B4 | 48 | `reorderCount[categoryIndex] = 0` |
| D47 | restockPlan | B4 | 49 | `restockPlan[categoryIndex] = 0` |
| D48 | clearancePlan | B4 | 50 | `clearancePlan[categoryIndex] = 0` |
| D49 | auditFlag | B4 | 51 | `auditFlag[categoryIndex] = 0` |
| D50 | categoryIndex | B3 | 46 | `categoryIndex++` |
| D51 | categoryIndex | B2 | 54 | `categoryIndex = 0` |
| D52 | storeIndex | B8 | 55 | `storeIndex = 0` |
| D53 | weekIndex | B12 | 56 | `weekIndex = 0` |
| D54 | stock | B16 | 57 | `stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| D55 | totalStock | B16 | 58 | `totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| D56 | totalDeficit | B18 | 60 | `totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| D57 | reorderCount | B18 | 61 | `reorderCount[categoryIndex] += 1` |
| D58 | totalSurplus | B22 | 63 | `totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| D59 | weekIndex | B15 | 56 | `weekIndex++` |
| D60 | storeIndex | B11 | 55 | `storeIndex++` |
| D61 | categoryIndex | B7 | 54 | `categoryIndex++` |
| D62 | highestStock | B6 | 69 | `highestStock = totalStock / ((categories * stores) * weeks)` |
| D63 | lowestStock | B6 | 70 | `lowestStock = highestStock` |
| D64 | categoryIndex | B6 | 72 | `categoryIndex = 0` |
| D65 | tempVariance | B27 | 73 | `tempVariance = 0` |
| D66 | storeIndex | B27 | 74 | `storeIndex = 0` |
| D67 | runningTotal | B31 | 75 | `int runningTotal = 0` |
| D68 | weekIndex | B31 | 76 | `weekIndex = 0` |
| D69 | runningTotal | B35 | 77 | `runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| D70 | forecast | B37 | 79 | `forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| D71 | highestStock | B40 | 83 | `highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| D72 | lowestStock | B43 | 86 | `lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| D73 | previousStock | B46 | 90 | `previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| D74 | stockChange | B46 | 91 | `stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| D75 | demandSpike | B48 | 93 | `demandSpike[categoryIndex][storeIndex] += 1` |
| D76 | demandDrop | B52 | 95 | `demandDrop[categoryIndex][storeIndex] += 1` |
| D77 | trendDirection | B55 | 99 | `trendDirection = 1` |
| D78 | currentGrowthStreak | B55 | 100 | `currentGrowthStreak += 1` |
| D79 | currentDeclineStreak | B55 | 101 | `currentDeclineStreak = 0` |
| D80 | trendDirection | B59 | 103 | `trendDirection = -1` |
| D81 | currentDeclineStreak | B59 | 104 | `currentDeclineStreak += 1` |
| D82 | currentGrowthStreak | B59 | 105 | `currentGrowthStreak = 0` |
| D83 | trendDirection | B61 | 107 | `trendDirection = 0` |
| D84 | currentGrowthStreak | B61 | 108 | `currentGrowthStreak = 0` |
| D85 | currentDeclineStreak | B61 | 109 | `currentDeclineStreak = 0` |
| D86 | sameTrendCount | B63 | 113 | `sameTrendCount += 1` |
| D87 | sameTrendCount | B65 | 115 | `sameTrendCount = 1` |
| D88 | longestGrowthStreak | B67 | 119 | `longestGrowthStreak = currentGrowthStreak` |
| D89 | longestDeclineStreak | B70 | 122 | `longestDeclineStreak = currentDeclineStreak` |
| D90 | lastTrendDirection | B71 | 125 | `lastTrendDirection = trendDirection` |
| D91 | runningTotal | B72 | 128 | `runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| D92 | weekIndex | B34 | 76 | `weekIndex++` |
| D93 | movingAvg | B33 | 130 | `movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| D94 | balancedStores | B74 | 132 | `balancedStores += 1` |
| D95 | storeIndex | B30 | 74 | `storeIndex++` |
| D96 | restockPlan | B77 | 137 | `restockPlan[categoryIndex] = 1` |
| D97 | clearancePlan | B81 | 139 | `clearancePlan[categoryIndex] = 1` |
| D98 | auditFlag | B84 | 143 | `auditFlag[categoryIndex] = 1` |
| D99 | exceptionCount | B84 | 144 | `exceptionCount += 1` |
| D100 | tempVariance | B85 | 147 | `tempVariance = highestStock - lowestStock` |
| D101 | cumulativeVariance | B85 | 148 | `cumulativeVariance += tempVariance` |
| D102 | maxVarianceCategory | B87 | 150 | `maxVarianceCategory = tempVariance` |
| D103 | minVarianceCategory | B90 | 153 | `minVarianceCategory = tempVariance` |
| D104 | categoryIndex | B26 | 72 | `categoryIndex++` |
| D105 | weekIndex | B25 | 157 | `weekIndex = 0` |
| D106 | weekBalanced | B95 | 158 | `int weekBalanced = 0` |
| D107 | categoryIndex | B95 | 159 | `categoryIndex = 0` |
| D108 | totalWeekStock | B99 | 160 | `int totalWeekStock = 0` |
| D109 | storeIndex | B99 | 161 | `storeIndex = 0` |
| D110 | totalWeekStock | B103 | 162 | `totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| D111 | storeIndex | B102 | 161 | `storeIndex++` |
| D112 | weekBalanced | B105 | 165 | `weekBalanced += 1` |
| D113 | categoryIndex | B98 | 159 | `categoryIndex++` |
| D114 | balancedWeeks | B108 | 169 | `balancedWeeks += 1` |
| D115 | weekIndex | B94 | 157 | `weekIndex++` |
| D116 | categoryIndex | B93 | 173 | `categoryIndex = 0` |
| D117 | totalCategoryStock | B113 | 174 | `int totalCategoryStock = 0` |
| D118 | totalCategoryDeficit | B113 | 175 | `int totalCategoryDeficit = 0` |
| D119 | totalCategorySurplus | B113 | 176 | `int totalCategorySurplus = 0` |
| D120 | storeIndex | B113 | 177 | `storeIndex = 0` |
| D121 | weekIndex | B117 | 178 | `weekIndex = 0` |
| D122 | totalCategoryStock | B121 | 179 | `totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| D123 | totalCategoryDeficit | B123 | 181 | `totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| D124 | totalCategorySurplus | B126 | 184 | `totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| D125 | weekIndex | B120 | 178 | `weekIndex++` |
| D126 | storeIndex | B116 | 177 | `storeIndex++` |
| D127 | trendDecline | B129 | 190 | `trendDecline += 1` |
| D128 | trendGrowth | B133 | 192 | `trendGrowth += 1` |
| D129 | trendStable | B135 | 194 | `trendStable += 1` |
| D130 | outOfStock | B137 | 198 | `outOfStock += 1` |
| D131 | overStocked | B141 | 200 | `overStocked += 1` |
| D132 | balanced | B143 | 202 | `balanced += 1` |
| D133 | categoryIndex | B112 | 173 | `categoryIndex++` |
| D134 | sameTrendCount | B145 | 207 | `sameTrendCount += trendGrowth` |
| D135 | sameTrendCount | B149 | 209 | `sameTrendCount += trendDecline` |
| D136 | sameTrendCount | B151 | 211 | `sameTrendCount += trendStable` |
| D137 | auditFlag | B153 | 215 | `auditFlag[0] = 1` |
| D138 | auditFlag | B157 | 217 | `auditFlag[1] = 1` |
| D139 | auditFlag | B159 | 219 | `auditFlag[2] = 1` |
| D140 | balanced | B161 | 223 | `balanced = balanced - exceptionCount` |
| D141 | balanced | B164 | 227 | `balanced += 1` |
| D142 | overStocked | B166 | 229 | `overStocked += 1` |
| D143 | trendStable | B168 | 233 | `trendStable += 1` |
| D144 | trendDecline | B170 | 235 | `trendDecline += 1` |