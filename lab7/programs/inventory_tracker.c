int main() {
    int categories = 8;
    int stores = 12;
    int weeks = 10;
    int stock[8][12][10];
    int reorderThreshold[8];
    int reorderCount[8];
    int totalStock = 0;
    int totalDeficit = 0;
    int totalSurplus = 0;
    int outOfStock = 0;
    int overStocked = 0;
    int balanced = 0;
    int storeIndex = 0;
    int categoryIndex = 0;
    int weekIndex = 0;
    int forecast[8][12];
    int demandSpike[8][12];
    int demandDrop[8][12];
    int movingAvg[8][12];
    int trendGrowth = 0;
    int trendDecline = 0;
    int trendStable = 0;
    int highestStock = 0;
    int lowestStock = 0;
    int cumulativeVariance = 0;
    int maxVarianceCategory = 0;
    int minVarianceCategory = 0;
    int tempVariance = 0;
    int stockChange = 0;
    int previousStock = 0;
    int sameTrendCount = 0;
    int trendDirection = 0;
    int lastTrendDirection = 0;
    int longestGrowthStreak = 0;
    int longestDeclineStreak = 0;
    int currentGrowthStreak = 0;
    int currentDeclineStreak = 0;
    int restockPlan[8];
    int clearancePlan[8];
    int auditFlag[8];
    int exceptionCount = 0;
    int balancedWeeks = 0;
    int balancedStores = 0;

    for (categoryIndex = 0; categoryIndex < categories; categoryIndex++) {
        reorderThreshold[categoryIndex] = 50 + categoryIndex * 5;
        reorderCount[categoryIndex] = 0;
        restockPlan[categoryIndex] = 0;
        clearancePlan[categoryIndex] = 0;
        auditFlag[categoryIndex] = 0;
    }

    for (categoryIndex = 0; categoryIndex < categories; categoryIndex++) {
        for (storeIndex = 0; storeIndex < stores; storeIndex++) {
            for (weekIndex = 0; weekIndex < weeks; weekIndex++) {
                stock[categoryIndex][storeIndex][weekIndex] = (categoryIndex * 13 + storeIndex * 7 + weekIndex * 5) % 200 + 20;
                totalStock += stock[categoryIndex][storeIndex][weekIndex];
                if (stock[categoryIndex][storeIndex][weekIndex] < reorderThreshold[categoryIndex]) {
                    totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex];
                    reorderCount[categoryIndex] += 1;
                } else if (stock[categoryIndex][storeIndex][weekIndex] > reorderThreshold[categoryIndex] * 2) {
                    totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - reorderThreshold[categoryIndex] * 2;
                }
            }
        }
    }

    highestStock = totalStock / (categories * stores * weeks);
    lowestStock = highestStock;

    for (categoryIndex = 0; categoryIndex < categories; categoryIndex++) {
        tempVariance = 0;
        for (storeIndex = 0; storeIndex < stores; storeIndex++) {
            int runningTotal = 0;
            for (weekIndex = 0; weekIndex < weeks; weekIndex++) {
                runningTotal += stock[categoryIndex][storeIndex][weekIndex];
                if (weekIndex == weeks - 1) {
                    forecast[categoryIndex][storeIndex] = runningTotal / weeks;
                }

                if (stock[categoryIndex][storeIndex][weekIndex] > highestStock) {
                    highestStock = stock[categoryIndex][storeIndex][weekIndex];
                }
                if (stock[categoryIndex][storeIndex][weekIndex] < lowestStock) {
                    lowestStock = stock[categoryIndex][storeIndex][weekIndex];
                }

                if (weekIndex > 0) {
                    previousStock = stock[categoryIndex][storeIndex][weekIndex - 1];
                    stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock;
                    if (stockChange > 30) {
                        demandSpike[categoryIndex][storeIndex] += 1;
                    } else if (stockChange < -30) {
                        demandDrop[categoryIndex][storeIndex] += 1;
                    }

                    if (stockChange > 0) {
                        trendDirection = 1;
                        currentGrowthStreak += 1;
                        currentDeclineStreak = 0;
                    } else if (stockChange < 0) {
                        trendDirection = -1;
                        currentDeclineStreak += 1;
                        currentGrowthStreak = 0;
                    } else {
                        trendDirection = 0;
                        currentGrowthStreak = 0;
                        currentDeclineStreak = 0;
                    }

                    if (trendDirection == lastTrendDirection && trendDirection != 0) {
                        sameTrendCount += 1;
                    } else {
                        sameTrendCount = 1;
                    }

                    if (currentGrowthStreak > longestGrowthStreak) {
                        longestGrowthStreak = currentGrowthStreak;
                    }
                    if (currentDeclineStreak > longestDeclineStreak) {
                        longestDeclineStreak = currentDeclineStreak;
                    }

                    lastTrendDirection = trendDirection;
                }

                runningTotal += stock[categoryIndex][storeIndex][weekIndex];
            }
            movingAvg[categoryIndex][storeIndex] = runningTotal / weeks;
            if (movingAvg[categoryIndex][storeIndex] >= reorderThreshold[categoryIndex] && movingAvg[categoryIndex][storeIndex] <= reorderThreshold[categoryIndex] * 2) {
                balancedStores += 1;
            }
        }

        if (reorderCount[categoryIndex] > weeks * stores / 2) {
            restockPlan[categoryIndex] = 1;
        } else if (reorderCount[categoryIndex] == 0) {
            clearancePlan[categoryIndex] = 1;
        }

        if (restockPlan[categoryIndex] == 1 && clearancePlan[categoryIndex] == 1) {
            auditFlag[categoryIndex] = 1;
            exceptionCount += 1;
        }

        tempVariance = highestStock - lowestStock;
        cumulativeVariance += tempVariance;
        if (tempVariance > maxVarianceCategory) {
            maxVarianceCategory = tempVariance;
        }
        if (tempVariance < minVarianceCategory || categoryIndex == 0) {
            minVarianceCategory = tempVariance;
        }
    }

    for (weekIndex = 0; weekIndex < weeks; weekIndex++) {
        int weekBalanced = 0;
        for (categoryIndex = 0; categoryIndex < categories; categoryIndex++) {
            int totalWeekStock = 0;
            for (storeIndex = 0; storeIndex < stores; storeIndex++) {
                totalWeekStock += stock[categoryIndex][storeIndex][weekIndex];
            }
            if (totalWeekStock >= reorderThreshold[categoryIndex] * stores && totalWeekStock <= reorderThreshold[categoryIndex] * 3) {
                weekBalanced += 1;
            }
        }
        if (weekBalanced == categories) {
            balancedWeeks += 1;
        }
    }

    for (categoryIndex = 0; categoryIndex < categories; categoryIndex++) {
        int totalCategoryStock = 0;
        int totalCategoryDeficit = 0;
        int totalCategorySurplus = 0;
        for (storeIndex = 0; storeIndex < stores; storeIndex++) {
            for (weekIndex = 0; weekIndex < weeks; weekIndex++) {
                totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex];
                if (stock[categoryIndex][storeIndex][weekIndex] < reorderThreshold[categoryIndex]) {
                    totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex];
                }
                if (stock[categoryIndex][storeIndex][weekIndex] > reorderThreshold[categoryIndex] * 2) {
                    totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - reorderThreshold[categoryIndex] * 2;
                }
            }
        }

        if (totalCategoryDeficit > totalCategorySurplus) {
            trendDecline += 1;
        } else if (totalCategoryDeficit < totalCategorySurplus) {
            trendGrowth += 1;
        } else {
            trendStable += 1;
        }

        if (totalCategoryStock < reorderThreshold[categoryIndex] * stores * weeks) {
            outOfStock += 1;
        } else if (totalCategoryStock > reorderThreshold[categoryIndex] * stores * weeks * 2) {
            overStocked += 1;
        } else {
            balanced += 1;
        }
    }

    if (trendGrowth > trendDecline) {
        sameTrendCount += trendGrowth;
    } else if (trendGrowth < trendDecline) {
        sameTrendCount += trendDecline;
    } else {
        sameTrendCount += trendStable;
    }

    if (longestGrowthStreak > longestDeclineStreak) {
        auditFlag[0] = 1;
    } else if (longestGrowthStreak < longestDeclineStreak) {
        auditFlag[1] = 1;
    } else {
        auditFlag[2] = 1;
    }

    if (exceptionCount > 0) {
        balanced = balanced - exceptionCount;
    }

    if (balancedStores > stores * categories / 2) {
        balanced += 1;
    } else {
        overStocked += 1;
    }

    if (balancedWeeks > weeks / 2) {
        trendStable += 1;
    } else {
        trendDecline += 1;
    }

    return totalStock + totalDeficit + totalSurplus + outOfStock + overStocked + balanced + trendGrowth + trendDecline + trendStable + sameTrendCount + auditFlag[0] + auditFlag[1] + auditFlag[2] + reorderCount[0] + reorderCount[1] + reorderCount[2];
}
