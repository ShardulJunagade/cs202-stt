### Block B1
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| bucketWind | D55, D59 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0` |
| dayGroup | D56, D60 | `dayGroup = 0`<br>`dayGroup++` |
| bucketTemp | D53, D57 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0` |
| bucketHumidity | D54, D58 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0` |

### Block B2
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| bucketWind | D55, D59 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0` |
| dayGroup | D56, D60 | `dayGroup = 0`<br>`dayGroup++` |
| bucketTemp | D53, D57 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0` |
| bucketHumidity | D54, D58 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0` |

### Block B3
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| dayGroup | D56, D60 | `dayGroup = 0`<br>`dayGroup++` |

### Block B4
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| bucketWind | D55, D59 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0` |
| dayGroup | D56, D60 | `dayGroup = 0`<br>`dayGroup++` |
| bucketTemp | D53, D57 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0` |
| bucketHumidity | D54, D58 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0` |

### Block B5
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114 | `int hour = 0`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B6
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114 | `int hour = 0`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B7
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B8
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114 | `int hour = 0`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B9
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B10
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B11
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B12
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B13
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B14
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B15
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B16
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B17
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B18
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B19
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B20
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B21
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B22
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B23
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B24
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B25
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B26
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B27
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B28
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B29
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B30
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B31
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B32
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B33
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B34
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B35
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B36
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B37
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B38
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B39
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B40
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B41
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B42
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B43
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B44
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B45
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B46
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B47
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B48
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B49
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B50
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B51
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B52
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B53
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B54
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B55
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B56
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B57
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B58
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B59
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B60
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B61
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B62
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B63
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B64
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B65
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B66
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B67
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B68
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B69
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B70
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D103, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D91, D97, D101 | `sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| sequentialDrop | D92, D96, D102 | `sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| currentTrend | D90, D95, D100 | `currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B71
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B72
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B73
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B74
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D103, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D97, D101 | `sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| sequentialDrop | D96, D102 | `sequentialDrop += 1`<br>`sequentialDrop = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| currentTrend | D95, D100 | `currentTrend = -1`<br>`currentTrend = 0` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B75
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B76
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D103, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D91, D97, D101 | `sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| sequentialDrop | D92, D96, D102 | `sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| currentTrend | D90, D95, D100 | `currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B77
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D103, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D91, D97, D101 | `sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| sequentialDrop | D92, D96, D102 | `sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| currentTrend | D90, D95, D100 | `currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B78
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D104, D105, D106 | `sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D91, D97, D101 | `sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| sequentialDrop | D92, D96, D102 | `sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| currentTrend | D90, D95, D100 | `currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B79
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D103, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D91, D97, D101 | `sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| sequentialDrop | D92, D96, D102 | `sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| currentTrend | D90, D95, D100 | `currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B80
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D103, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D91, D97, D101 | `sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| sequentialDrop | D92, D96, D102 | `sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| currentTrend | D90, D95, D100 | `currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B81
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D103, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D91, D97, D101 | `sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| sequentialDrop | D92, D96, D102 | `sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| currentTrend | D90, D95, D100 | `currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B82
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D105, D106 | `sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D91, D97, D101 | `sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| sequentialDrop | D92, D96, D102 | `sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| currentTrend | D90, D95, D100 | `currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B83
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D103, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D91, D97, D101 | `sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| sequentialDrop | D92, D96, D102 | `sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| currentTrend | D90, D95, D100 | `currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B84
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B85
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B86
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B87
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B88
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B89
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B90
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B91
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B92
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B93
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B94
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B95
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |

### Block B96
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D63, D94, D98 | `currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D64, D114 | `hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| dropEvents | D27, D87 | `int dropEvents = 0`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| day | D61, D117 | `day = 0`<br>`day++` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1` |
| currentHotStreak | D62, D93, D99 | `currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| spikeEvents | D26, D86 | `int spikeEvents = 0`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B97
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B98
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B99
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B100
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B101
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B102
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B103
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |

### Block B104
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B105
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |

### Block B106
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |

### Block B107
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B108
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |

### Block B109
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |

### Block B110
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |

### Block B111
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B112
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |

### Block B113
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |

### Block B114
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B115
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |

### Block B116
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |

### Block B117
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |

### Block B118
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B119
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |

### Block B120
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |

### Block B121
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |

### Block B122
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B123
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |

### Block B124
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |

### Block B125
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140 | `day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| stormWarnings | D21, D83 | `int stormWarnings = 0`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| trendUp | D23, D137 | `int trendUp = 0`<br>`trendUp += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| stableHours | D25, D79, D89 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hour | D122, D139 | `hour = 0`<br>`hour++` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| trendDown | D24, D138 | `int trendDown = 0`<br>`trendDown += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B126
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B127
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B128
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| day | D145, D149 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B129
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B130
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| midTemp | D142, D146 | `int midTemp = 0`<br>`midTemp += temp[day][hourGroup]` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| midHumidity | D143, D147 | `int midHumidity = 0`<br>`midHumidity += humidity[day][hourGroup]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| day | D145, D149 | `day = 0`<br>`day++` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| midWind | D144, D148 | `int midWind = 0`<br>`midWind += wind[day][hourGroup]` |

### Block B131
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| midWind | D144, D148 | `int midWind = 0`<br>`midWind += wind[day][hourGroup]` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| midTemp | D142, D146 | `int midTemp = 0`<br>`midTemp += temp[day][hourGroup]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| midHumidity | D143, D147 | `int midHumidity = 0`<br>`midHumidity += humidity[day][hourGroup]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| day | D145, D149 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B132
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| day | D145, D149 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B133
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| midWind | D144, D148 | `int midWind = 0`<br>`midWind += wind[day][hourGroup]` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| midTemp | D142, D146 | `int midTemp = 0`<br>`midTemp += temp[day][hourGroup]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| midHumidity | D143, D147 | `int midHumidity = 0`<br>`midHumidity += humidity[day][hourGroup]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| day | D145, D149 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B134
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| day | D145, D149 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B135
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| day | D145, D149 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B136
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| day | D145, D149 | `day = 0`<br>`day++` |
| calmHours | D22, D82, D84, D156 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B137
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| day | D145, D149 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B138
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| day | D145, D149 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B139
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| day | D145, D149 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B140
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| day | D145, D149 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B141
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| day | D145, D149 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B142
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| day | D145, D149 | `day = 0`<br>`day++` |
| calmHours | D22, D82, D84, D156 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B143
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| day | D145, D149 | `day = 0`<br>`day++` |
| calmHours | D22, D82, D84, D156 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B144
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| day | D145, D149 | `day = 0`<br>`day++` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B145
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dayGroup | D56, D60, D110 | `dayGroup = 0`<br>`dayGroup++`<br>`dayGroup = day / 5` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133 | `int belowAverageCount = 0`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| dryDays | D20, D81 | `int dryDays = 0`<br>`dryDays += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| wetDays | D19, D80 | `int wetDays = 0`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| day | D145, D149 | `day = 0`<br>`day++` |
| calmHours | D22, D82, D84, D156 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B146
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B147
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B148
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B149
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B150
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B151
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B152
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B153
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B154
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B155
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B156
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B157
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B158
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B159
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B160
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B161
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B162
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B163
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B164
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| stableHours | D25, D79, D89, D155, D172 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153, D170 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154, D171 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B165
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B166
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B167
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B168
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| stableHours | D25, D79, D89, D155, D172 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154, D171 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B169
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| stableHours | D25, D79, D89, D155 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B170
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| stableHours | D25, D79, D89, D155, D172 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153, D170 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154, D171 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B171
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| stableHours | D25, D79, D89, D155, D172 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153, D170 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154, D171 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B172
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| fluctuationEvents | D28, D88, D136, D175 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135, D174 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| stableHours | D25, D79, D89, D155, D172 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153, D170 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134, D173 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154, D171 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B173
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| stableHours | D25, D79, D89, D155, D172 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153, D170 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154, D171 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B174
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| stableHours | D25, D79, D89, D155, D172 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153, D170 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154, D171 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B175
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| stableHours | D25, D79, D89, D155, D172 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153, D170 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154, D171 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B176
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| fluctuationEvents | D28, D88, D136, D175 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135, D174 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| stableHours | D25, D79, D89, D155, D172 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153, D170 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154, D171 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B177
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| stableHours | D25, D79, D89, D155, D172 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153, D170 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| fluctuationEvents | D28, D88, D136 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154, D171 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B178
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| fluctuationEvents | D28, D88, D136, D175 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135, D174 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| stableHours | D25, D79, D89, D155, D172 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153, D170 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134, D173 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154, D171 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B179
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| fluctuationEvents | D28, D88, D136, D175 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135, D174 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| stableHours | D25, D79, D89, D155, D172 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| stormWarnings | D21, D83, D157, D167 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153, D170 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134, D173 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154, D171 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B180
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| stormWarnings | D21, D83, D157, D167, D176 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| stableHours | D25, D79, D89, D155, D172 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153, D170 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1`<br>`trendUp += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| dropEvents | D27, D87, D135, D174 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154, D171 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1`<br>`trendDown += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| spikeEvents | D26, D86, D134, D173 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| fluctuationEvents | D28, D88, D136, D175 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |

### Block B181
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| fluctuationEvents | D28, D88, D136, D175 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| stormWarnings | D21, D83, D157, D167, D176 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135, D174 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| stableHours | D25, D79, D89, D155, D172 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153, D170 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134, D173 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154, D171 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B182
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| fluctuationEvents | D28, D88, D136, D175 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| stormWarnings | D21, D83, D157, D167, D176 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
| dropEvents | D27, D87, D135, D174 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| stableHours | D25, D79, D89, D155, D172 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153, D170 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1`<br>`trendUp += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| spikeEvents | D26, D86, D134, D173 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154, D171 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1`<br>`trendDown += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |

### Block B183
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| dryDays | D20, D81, D166 | `int dryDays = 0`<br>`dryDays += 1`<br>`dryDays += 1` |
| coldDays | D18, D78 | `int coldDays = 0`<br>`coldDays += 1` |
| totalWind | D10, D70 | `int totalWind = 0`<br>`totalWind += wind[day][hour]` |
| bucketTemp | D53, D57, D111 | `int bucketTemp[6]`<br>`bucketTemp[dayGroup] = 0`<br>`bucketTemp[dayGroup] += temp[day][hour]` |
| longHotStreak | D34, D115 | `int longHotStreak = 0`<br>`longHotStreak += 1` |
| hour | D7, D64, D114, D122, D139 | `int hour = 0`<br>`hour = 0`<br>`hour++`<br>`hour = 0`<br>`hour++` |
| humidity | D4, D66 | `int humidity[30][24]`<br>`humidity[day][hour] = (((day * 5) + hour) % 70) + 20` |
| belowAverageCount | D41, D133, D164 | `int belowAverageCount = 0`<br>`belowAverageCount += 1`<br>`belowAverageCount += 1` |
| stormWarnings | D21, D83, D157, D167, D176 | `int stormWarnings = 0`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1`<br>`stormWarnings += 1` |
| sequentialRise | D29, D91, D97, D101 | `int sequentialRise = 0`<br>`sequentialRise += 1`<br>`sequentialRise = 0`<br>`sequentialRise = 0` |
| stableHours | D25, D79, D89, D155, D172 | `int stableHours = 0`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1`<br>`stableHours += 1` |
| previousTrend | D32, D107 | `int previousTrend = 0`<br>`previousTrend = currentTrend` |
| windVarianceAccumulator | D47, D128 | `int windVarianceAccumulator = 0`<br>`windVarianceAccumulator += windDiffMean * windDiffMean` |
| totalTemp | D8, D68 | `int totalTemp = 0`<br>`totalTemp += temp[day][hour]` |
| longestHotStreak | D36, D108 | `int longestHotStreak = 0`<br>`longestHotStreak = currentHotStreak` |
| totalHumidity | D9, D69 | `int totalHumidity = 0`<br>`totalHumidity += humidity[day][hour]` |
| bucketHumidity | D54, D58, D112 | `int bucketHumidity[6]`<br>`bucketHumidity[dayGroup] = 0`<br>`bucketHumidity[dayGroup] += humidity[day][hour]` |
| trendUp | D23, D137, D153, D170 | `int trendUp = 0`<br>`trendUp += 1`<br>`trendUp += 1`<br>`trendUp += 1` |
| currentHotStreak | D38, D62, D93, D99 | `int currentHotStreak = 0`<br>`currentHotStreak = 0`<br>`currentHotStreak += 1`<br>`currentHotStreak = 0` |
| wind | D5, D67 | `int wind[30][24]`<br>`wind[day][hour] = (((day * 4) + (hour * 3)) % 35) + 5` |
| maxHumidity | D13, D73 | `int maxHumidity = -1000`<br>`maxHumidity = humidity[day][hour]` |
| humidityVarianceAccumulator | D46, D127 | `int humidityVarianceAccumulator = 0`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean` |
| dayGroup | D159, D169 | `dayGroup = 0`<br>`dayGroup++` |
| wetDays | D19, D80, D165, D177 | `int wetDays = 0`<br>`wetDays += 1`<br>`wetDays += 1`<br>`wetDays += 1` |
| normalizedHumidity | D49, D130 | `int normalizedHumidity = 0`<br>`normalizedHumidity = humidity[day][hour] - minHumidity` |
| currentTrend | D33, D90, D95, D100 | `int currentTrend = 0`<br>`currentTrend = 1`<br>`currentTrend = -1`<br>`currentTrend = 0` |
| minTemp | D12, D72 | `int minTemp = 1000`<br>`minTemp = temp[day][hour]` |
| calmHours | D22, D82, D84, D156, D168 | `int calmHours = 0`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1`<br>`calmHours += 1` |
| dropEvents | D27, D87, D135, D174 | `int dropEvents = 0`<br>`dropEvents += 1`<br>`dropEvents += 1`<br>`dropEvents += 1` |
| varianceAccumulator | D45, D126 | `int varianceAccumulator = 0`<br>`varianceAccumulator += tempDiffMean * tempDiffMean` |
| trendDown | D24, D138, D154, D171 | `int trendDown = 0`<br>`trendDown += 1`<br>`trendDown += 1`<br>`trendDown += 1` |
| longestColdStreak | D37, D109 | `int longestColdStreak = 0`<br>`longestColdStreak = currentColdStreak` |
| spikeEvents | D26, D86, D134, D173 | `int spikeEvents = 0`<br>`spikeEvents += 1`<br>`spikeEvents += 1`<br>`spikeEvents += 1` |
| minWind | D16, D76 | `int minWind = 1000`<br>`minWind = wind[day][hour]` |
| day | D121, D140, D145, D149 | `day = 0`<br>`day++`<br>`day = 0`<br>`day++` |
| bucketWind | D55, D59, D113 | `int bucketWind[6]`<br>`bucketWind[dayGroup] = 0`<br>`bucketWind[dayGroup] += wind[day][hour]` |
| minHumidity | D14, D74 | `int minHumidity = 1000`<br>`minHumidity = humidity[day][hour]` |
| hourGroup | D141, D158 | `hourGroup = 0`<br>`hourGroup++` |
| aboveAverageCount | D40, D132, D163 | `int aboveAverageCount = 0`<br>`aboveAverageCount += 1`<br>`aboveAverageCount += 1` |
| normalizedWind | D50, D131 | `int normalizedWind = 0`<br>`normalizedWind = wind[day][hour] - minWind` |
| hotDays | D17, D77 | `int hotDays = 0`<br>`hotDays += 1` |
| sequentialDrop | D30, D92, D96, D102 | `int sequentialDrop = 0`<br>`sequentialDrop = 0`<br>`sequentialDrop += 1`<br>`sequentialDrop = 0` |
| temp | D3, D65 | `int temp[30][24]`<br>`temp[day][hour] = (((day * 3) + (hour * 2)) % 45) + 10` |
| maxWind | D15, D75 | `int maxWind = -1000`<br>`maxWind = wind[day][hour]` |
| currentColdStreak | D39, D63, D94, D98 | `int currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak = 0`<br>`currentColdStreak += 1` |
| longColdStreak | D35, D116 | `int longColdStreak = 0`<br>`longColdStreak += 1` |
| fluctuationEvents | D28, D88, D136, D175 | `int fluctuationEvents = 0`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1`<br>`fluctuationEvents += 1` |
| sameTrendStreak | D31, D104, D105, D106 | `int sameTrendStreak = 0`<br>`sameTrendStreak += 1`<br>`sameTrendStreak = 0`<br>`sameTrendStreak = 1` |
| maxTemp | D11, D71 | `int maxTemp = -1000`<br>`maxTemp = temp[day][hour]` |
| normalized | D48, D129 | `int normalized = 0`<br>`normalized = temp[day][hour] - minTemp` |
