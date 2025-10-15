int main() {
    int days = 30;
    int hours = 24;
    int temp[30][24];
    int humidity[30][24];
    int wind[30][24];
    int day = 0;
    int hour = 0;
    int totalTemp = 0;
    int totalHumidity = 0;
    int totalWind = 0;
    int maxTemp = -1000;
    int minTemp = 1000;
    int maxHumidity = -1000;
    int minHumidity = 1000;
    int maxWind = -1000;
    int minWind = 1000;
    int hotDays = 0;
    int coldDays = 0;
    int wetDays = 0;
    int dryDays = 0;
    int stormWarnings = 0;
    int calmHours = 0;
    int trendUp = 0;
    int trendDown = 0;
    int stableHours = 0;
    int spikeEvents = 0;
    int dropEvents = 0;
    int fluctuationEvents = 0;
    int sequentialRise = 0;
    int sequentialDrop = 0;
    int sameTrendStreak = 0;
    int previousTrend = 0;
    int currentTrend = 0;
    int longHotStreak = 0;
    int longColdStreak = 0;
    int longestHotStreak = 0;
    int longestColdStreak = 0;
    int currentHotStreak = 0;
    int currentColdStreak = 0;
    int aboveAverageCount = 0;
    int belowAverageCount = 0;
    int averageTemp = 0;
    int averageHumidity = 0;
    int averageWind = 0;
    int varianceAccumulator = 0;
    int humidityVarianceAccumulator = 0;
    int windVarianceAccumulator = 0;
    int normalized = 0;
    int normalizedHumidity = 0;
    int normalizedWind = 0;
    int dayGroup = 0;
    int hourGroup = 0;
    int bucketTemp[6];
    int bucketHumidity[6];
    int bucketWind[6];

    for (dayGroup = 0; dayGroup < 6; dayGroup++) {
        bucketTemp[dayGroup] = 0;
        bucketHumidity[dayGroup] = 0;
        bucketWind[dayGroup] = 0;
    }

    for (day = 0; day < days; day++) {
        currentHotStreak = 0;
        currentColdStreak = 0;
        for (hour = 0; hour < hours; hour++) {
            temp[day][hour] = (day * 3 + hour * 2) % 45 + 10;
            humidity[day][hour] = (day * 5 + hour) % 70 + 20;
            wind[day][hour] = (day * 4 + hour * 3) % 35 + 5;

            totalTemp += temp[day][hour];
            totalHumidity += humidity[day][hour];
            totalWind += wind[day][hour];

            if (temp[day][hour] > maxTemp) {
                maxTemp = temp[day][hour];
            }
            if (temp[day][hour] < minTemp) {
                minTemp = temp[day][hour];
            }
            if (humidity[day][hour] > maxHumidity) {
                maxHumidity = humidity[day][hour];
            }
            if (humidity[day][hour] < minHumidity) {
                minHumidity = humidity[day][hour];
            }
            if (wind[day][hour] > maxWind) {
                maxWind = wind[day][hour];
            }
            if (wind[day][hour] < minWind) {
                minWind = wind[day][hour];
            }

            if (temp[day][hour] >= 35) {
                hotDays += 1;
            } else if (temp[day][hour] <= 15) {
                coldDays += 1;
            } else {
                stableHours += 1;
            }

            if (humidity[day][hour] >= 75) {
                wetDays += 1;
            } else if (humidity[day][hour] <= 25) {
                dryDays += 1;
            } else {
                calmHours += 1;
            }

            if (wind[day][hour] >= 30) {
                stormWarnings += 1;
            } else if (wind[day][hour] <= 10) {
                calmHours += 1;
            }

            if (hour > 0) {
                int tempDiff = temp[day][hour] - temp[day][hour - 1];
                if (tempDiff > 4) {
                    spikeEvents += 1;
                } else if (tempDiff < -4) {
                    dropEvents += 1;
                } else if (tempDiff != 0) {
                    fluctuationEvents += 1;
                } else {
                    stableHours += 1;
                }

                if (tempDiff > 0) {
                    currentTrend = 1;
                    sequentialRise += 1;
                    sequentialDrop = 0;
                    currentHotStreak += 1;
                    currentColdStreak = 0;
                } else if (tempDiff < 0) {
                    currentTrend = -1;
                    sequentialDrop += 1;
                    sequentialRise = 0;
                    currentColdStreak += 1;
                    currentHotStreak = 0;
                } else {
                    currentTrend = 0;
                    sequentialRise = 0;
                    sequentialDrop = 0;
                    sameTrendStreak += 1;
                }

                if (previousTrend == currentTrend && currentTrend != 0) {
                    sameTrendStreak += 1;
                } else if (currentTrend == 0) {
                    sameTrendStreak = 0;
                } else {
                    sameTrendStreak = 1;
                }

                previousTrend = currentTrend;
            }

            if (currentHotStreak > longestHotStreak) {
                longestHotStreak = currentHotStreak;
            }
            if (currentColdStreak > longestColdStreak) {
                longestColdStreak = currentColdStreak;
            }

            dayGroup = day / 5;
            bucketTemp[dayGroup] += temp[day][hour];
            bucketHumidity[dayGroup] += humidity[day][hour];
            bucketWind[dayGroup] += wind[day][hour];
        }

        if (currentHotStreak >= 5) {
            longHotStreak += 1;
        }
        if (currentColdStreak >= 5) {
            longColdStreak += 1;
        }
    }

    averageTemp = totalTemp / (days * hours);
    averageHumidity = totalHumidity / (days * hours);
    averageWind = totalWind / (days * hours);

    for (day = 0; day < days; day++) {
        for (hour = 0; hour < hours; hour++) {
            int tempDiffMean = temp[day][hour] - averageTemp;
            int humidityDiffMean = humidity[day][hour] - averageHumidity;
            int windDiffMean = wind[day][hour] - averageWind;

            varianceAccumulator += tempDiffMean * tempDiffMean;
            humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;
            windVarianceAccumulator += windDiffMean * windDiffMean;

            normalized = temp[day][hour] - minTemp;
            normalizedHumidity = humidity[day][hour] - minHumidity;
            normalizedWind = wind[day][hour] - minWind;

            if (normalized > averageTemp) {
                aboveAverageCount += 1;
            } else if (normalized < averageTemp) {
                belowAverageCount += 1;
            }

            if (normalizedHumidity > averageHumidity && normalizedWind > averageWind) {
                spikeEvents += 1;
            } else if (normalizedHumidity < averageHumidity && normalizedWind < averageWind) {
                dropEvents += 1;
            } else {
                fluctuationEvents += 1;
            }

            if (temp[day][hour] > 30 && humidity[day][hour] > 60 && wind[day][hour] < 15) {
                trendUp += 1;
            }
            if (temp[day][hour] < 20 && humidity[day][hour] < 40 && wind[day][hour] > 20) {
                trendDown += 1;
            }
        }
    }

    for (hourGroup = 0; hourGroup < hours; hourGroup++) {
        int midTemp = 0;
        int midHumidity = 0;
        int midWind = 0;
        for (day = 0; day < days; day++) {
            midTemp += temp[day][hourGroup];
            midHumidity += humidity[day][hourGroup];
            midWind += wind[day][hourGroup];
        }
        midTemp = midTemp / days;
        midHumidity = midHumidity / days;
        midWind = midWind / days;

        if (midTemp > averageTemp && midHumidity > averageHumidity) {
            trendUp += 1;
        } else if (midTemp < averageTemp && midHumidity < averageHumidity) {
            trendDown += 1;
        } else {
            stableHours += 1;
        }

        if (midWind < averageWind) {
            calmHours += 1;
        } else {
            stormWarnings += 1;
        }
    }

    for (dayGroup = 0; dayGroup < 6; dayGroup++) {
        int groupTemp = bucketTemp[dayGroup] / (hours * 5);
        int groupHumidity = bucketHumidity[dayGroup] / (hours * 5);
        int groupWind = bucketWind[dayGroup] / (hours * 5);

        if (groupTemp > averageTemp) {
            aboveAverageCount += 1;
        } else {
            belowAverageCount += 1;
        }

        if (groupHumidity > averageHumidity) {
            wetDays += 1;
        } else {
            dryDays += 1;
        }

        if (groupWind > averageWind) {
            stormWarnings += 1;
        } else {
            calmHours += 1;
        }
    }

    if (aboveAverageCount > belowAverageCount) {
        trendUp += 1;
    } else if (aboveAverageCount < belowAverageCount) {
        trendDown += 1;
    } else {
        stableHours += 1;
    }

    if (longHotStreak > longColdStreak) {
        spikeEvents += 1;
    } else if (longHotStreak < longColdStreak) {
        dropEvents += 1;
    } else {
        fluctuationEvents += 1;
    }

    if (longestHotStreak > 10) {
        stormWarnings += 1;
    }
    if (longestColdStreak > 10) {
        wetDays += 1;
    }

    return trendUp + trendDown + stableHours + spikeEvents + dropEvents + fluctuationEvents + calmHours + stormWarnings + wetDays + dryDays + hotDays + coldDays + aboveAverageCount + belowAverageCount;
}
