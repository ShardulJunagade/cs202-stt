### Block B1
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| dayGroup | D56, D57 | `dayGroup = 0;`<br>`dayGroup++;` |

### Block B2
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| dayGroup | D56, D57 | `dayGroup = 0;`<br>`dayGroup++;` |

### Block B3
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| dayGroup | D56, D57 | `dayGroup = 0;`<br>`dayGroup++;` |

### Block B4
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| dayGroup | D56, D57 | `dayGroup = 0;`<br>`dayGroup++;` |

### Block B5
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D7, D61, D105 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;` |

### Block B6
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D7, D61, D105 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;` |

### Block B7
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B8
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D7, D61, D105 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;` |

### Block B9
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B10
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B11
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D73, D83 | `stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B12
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B13
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B14
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B15
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B16
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B17
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B18
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B19
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B20
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B21
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B22
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B23
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B24
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B25
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B26
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B27
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B28
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B29
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B30
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B31
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B32
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B33
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B34
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B35
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B36
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B37
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B38
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B39
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B40
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B41
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B42
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B43
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B44
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B45
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B46
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B47
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B48
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B49
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B50
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B51
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B52
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| sequentialDrop | D86, D90 | `sequentialDrop = 0;`<br>`sequentialDrop += 1;` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| currentColdStreak | D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| currentHotStreak | D87, D93 | `currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| sequentialRise | D85, D91 | `sequentialRise += 1;`<br>`sequentialRise = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D84, D89 | `currentTrend = 1;`<br>`currentTrend = -1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B53
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D87, D93 | `currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B54
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D87, D93 | `currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B55
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D87, D93 | `currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B56
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| sameTrendStreak | D98, D99 | `sameTrendStreak += 1;`<br>`sameTrendStreak = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| currentColdStreak | D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| currentHotStreak | D87, D93 | `currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B57
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D73, D83 | `stableHours += 1;`<br>`stableHours += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B58
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D73, D83 | `stableHours += 1;`<br>`stableHours += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B59
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D73, D83 | `stableHours += 1;`<br>`stableHours += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B60
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D73, D83 | `stableHours += 1;`<br>`stableHours += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B61
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D73, D83 | `stableHours += 1;`<br>`stableHours += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B62
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D73, D83 | `stableHours += 1;`<br>`stableHours += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B63
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D76, D78 | `calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D73, D83 | `stableHours += 1;`<br>`stableHours += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B64
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B65
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B66
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B67
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B68
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B69
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| dropEvents | D27, D81 | `int dropEvents = 0;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| day | D58, D108 | `day = 0;`<br>`day++;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D60, D88, D92 | `currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D59, D87, D93 | `currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| spikeEvents | D26, D80 | `int spikeEvents = 0;`<br>`spikeEvents += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| hour | D61, D105 | `hour = 0;`<br>`hour++;` |

### Block B70
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B71
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |

### Block B72
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| hour | D113, D130 | `hour = 0;`<br>`hour++;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |

### Block B73
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |

### Block B74
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| hour | D113, D130 | `hour = 0;`<br>`hour++;` |
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B75
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| hour | D113, D130 | `hour = 0;`<br>`hour++;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |

### Block B76
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| hour | D113, D130 | `hour = 0;`<br>`hour++;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |

### Block B77
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| hour | D113, D130 | `hour = 0;`<br>`hour++;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |

### Block B78
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| hour | D113, D130 | `hour = 0;`<br>`hour++;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |

### Block B79
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| hour | D113, D130 | `hour = 0;`<br>`hour++;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |

### Block B80
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| hour | D113, D130 | `hour = 0;`<br>`hour++;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |

### Block B81
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| hour | D113, D130 | `hour = 0;`<br>`hour++;` |
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B82
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| hour | D113, D130 | `hour = 0;`<br>`hour++;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |

### Block B83
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| hour | D113, D130 | `hour = 0;`<br>`hour++;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |

### Block B84
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| hour | D113, D130 | `hour = 0;`<br>`hour++;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |

### Block B85
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| hour | D113, D130 | `hour = 0;`<br>`hour++;` |
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B86
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| hour | D113, D130 | `hour = 0;`<br>`hour++;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |

### Block B87
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| hour | D113, D130 | `hour = 0;`<br>`hour++;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |

### Block B88
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| hour | D113, D130 | `hour = 0;`<br>`hour++;` |
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B89
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| hour | D113, D130 | `hour = 0;`<br>`hour++;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |

### Block B90
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| hour | D113, D130 | `hour = 0;`<br>`hour++;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |

### Block B91
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| hour | D113, D130 | `hour = 0;`<br>`hour++;` |
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| trendDown | D24, D129 | `int trendDown = 0;`<br>`trendDown += 1;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D25, D73, D83 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128 | `int trendUp = 0;`<br>`trendUp += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| day | D112, D131 | `day = 0;`<br>`day++;` |
| stormWarnings | D21, D77 | `int stormWarnings = 0;`<br>`stormWarnings += 1;` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B92
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78, D147 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B93
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78, D147 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |

### Block B94
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D136, D140 | `day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78, D147 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |

### Block B95
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78, D147 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |

### Block B96
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| midTemp | D133, D137 | `int midTemp = 0;`<br>`midTemp += temp[day][hourGroup];` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D136, D140 | `day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78, D147 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| midWind | D135, D139 | `int midWind = 0;`<br>`midWind += wind[day][hourGroup];` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| midHumidity | D134, D138 | `int midHumidity = 0;`<br>`midHumidity += humidity[day][hourGroup];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B97
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| midWind | D135, D139 | `int midWind = 0;`<br>`midWind += wind[day][hourGroup];` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| midHumidity | D134, D138 | `int midHumidity = 0;`<br>`midHumidity += humidity[day][hourGroup];` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| midTemp | D133, D137 | `int midTemp = 0;`<br>`midTemp += temp[day][hourGroup];` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D136, D140 | `day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78, D147 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |

### Block B98
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D136, D140 | `day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78, D147 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |

### Block B99
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| midWind | D135, D139 | `int midWind = 0;`<br>`midWind += wind[day][hourGroup];` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| midHumidity | D134, D138 | `int midHumidity = 0;`<br>`midHumidity += humidity[day][hourGroup];` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| midTemp | D133, D137 | `int midTemp = 0;`<br>`midTemp += temp[day][hourGroup];` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D136, D140 | `day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78, D147 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |

### Block B100
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D136, D140 | `day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78, D147 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |

### Block B101
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D136, D140 | `day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78, D147 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |

### Block B102
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D136, D140 | `day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78, D147 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |

### Block B103
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D136, D140 | `day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78, D147 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B104
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D136, D140 | `day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78, D147 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |

### Block B105
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D136, D140 | `day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78, D147 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |

### Block B106
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D136, D140 | `day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78, D147 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |

### Block B107
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74 | `int wetDays = 0;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| dayGroup | D56, D57, D104 | `dayGroup = 0;`<br>`dayGroup++;`<br>`dayGroup = day / 5;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D136, D140 | `day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| calmHours | D22, D76, D78, D147 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75 | `int dryDays = 0;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| aboveAverageCount | D40, D123 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B108
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B109
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B110
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B111
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B112
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B113
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B114
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B115
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B116
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B117
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B118
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B119
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B120
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B121
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B122
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B123
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B124
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B125
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B126
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B127
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145, D162 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| stableHours | D25, D73, D83, D146 | `int stableHours = 0;`<br>`stableHours += 1;`<br>`stableHours += 1;`<br>`stableHours += 1;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144, D161 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B128
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145, D162 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144, D161 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B129
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145, D162 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144, D161 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B130
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145, D162 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| spikeEvents | D26, D80, D125 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144, D161 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B131
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126, D165 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| fluctuationEvents | D28, D82, D127 | `int fluctuationEvents = 0;`<br>`fluctuationEvents += 1;`<br>`fluctuationEvents += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145, D162 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| spikeEvents | D26, D80, D125, D164 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144, D161 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B132
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126, D165 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145, D162 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| spikeEvents | D26, D80, D125, D164 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144, D161 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B133
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126, D165 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145, D162 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| spikeEvents | D26, D80, D125, D164 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144, D161 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B134
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126, D165 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158, D167 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145, D162 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| spikeEvents | D26, D80, D125, D164 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144, D161 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B135
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126, D165 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158, D167 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145, D162 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| spikeEvents | D26, D80, D125, D164 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144, D161 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B136
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| wetDays | D19, D74, D156 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126, D165 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158, D167 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145, D162 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| spikeEvents | D26, D80, D125, D164 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144, D161 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |

### Block B137
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| previousTrend | D32, D101 | `int previousTrend = 0;`<br>`previousTrend = currentTrend;` |
| hour | D7, D61, D105, D113, D130 | `int hour = 0;`<br>`hour = 0;`<br>`hour++;`<br>`hour = 0;`<br>`hour++;` |
| wetDays | D19, D74, D156, D168 | `int wetDays = 0;`<br>`wetDays += 1;`<br>`wetDays += 1;`<br>`wetDays += 1;` |
| longestHotStreak | D36, D102 | `int longestHotStreak = 0;`<br>`longestHotStreak = currentHotStreak;` |
| totalTemp | D8, D62 | `int totalTemp = 0;`<br>`totalTemp += temp[day][hour];` |
| totalHumidity | D9, D63 | `int totalHumidity = 0;`<br>`totalHumidity += humidity[day][hour];` |
| aboveAverageCount | D40, D123, D154 | `int aboveAverageCount = 0;`<br>`aboveAverageCount += 1;`<br>`aboveAverageCount += 1;` |
| calmHours | D22, D76, D78, D147, D159 | `int calmHours = 0;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;`<br>`calmHours += 1;` |
| windVarianceAccumulator | D47, D119 | `int windVarianceAccumulator = 0;`<br>`windVarianceAccumulator += windDiffMean * windDiffMean;` |
| dropEvents | D27, D81, D126, D165 | `int dropEvents = 0;`<br>`dropEvents += 1;`<br>`dropEvents += 1;`<br>`dropEvents += 1;` |
| maxTemp | D11, D65 | `int maxTemp = -1000;`<br>`maxTemp = temp[day][hour];` |
| stormWarnings | D21, D77, D148, D158, D167 | `int stormWarnings = 0;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;`<br>`stormWarnings += 1;` |
| minTemp | D12, D66 | `int minTemp = 1000;`<br>`minTemp = temp[day][hour];` |
| dayGroup | D150, D160 | `dayGroup = 0;`<br>`dayGroup++;` |
| minWind | D16, D70 | `int minWind = 1000;`<br>`minWind = wind[day][hour];` |
| longHotStreak | D34, D106 | `int longHotStreak = 0;`<br>`longHotStreak += 1;` |
| normalizedWind | D50, D122 | `int normalizedWind = 0;`<br>`normalizedWind = wind[day][hour] - minWind;` |
| hourGroup | D132, D149 | `hourGroup = 0;`<br>`hourGroup++;` |
| trendDown | D24, D129, D145, D162 | `int trendDown = 0;`<br>`trendDown += 1;`<br>`trendDown += 1;`<br>`trendDown += 1;` |
| varianceAccumulator | D45, D117 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += tempDiffMean * tempDiffMean;` |
| totalWind | D10, D64 | `int totalWind = 0;`<br>`totalWind += wind[day][hour];` |
| day | D112, D131, D136, D140 | `day = 0;`<br>`day++;`<br>`day = 0;`<br>`day++;` |
| currentColdStreak | D39, D60, D88, D92 | `int currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak = 0;`<br>`currentColdStreak += 1;` |
| minHumidity | D14, D68 | `int minHumidity = 1000;`<br>`minHumidity = humidity[day][hour];` |
| currentHotStreak | D38, D59, D87, D93 | `int currentHotStreak = 0;`<br>`currentHotStreak = 0;`<br>`currentHotStreak += 1;`<br>`currentHotStreak = 0;` |
| hotDays | D17, D71 | `int hotDays = 0;`<br>`hotDays += 1;` |
| longColdStreak | D35, D107 | `int longColdStreak = 0;`<br>`longColdStreak += 1;` |
| spikeEvents | D26, D80, D125, D164 | `int spikeEvents = 0;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;`<br>`spikeEvents += 1;` |
| sequentialRise | D29, D95 | `int sequentialRise = 0;`<br>`sequentialRise = 0;` |
| longestColdStreak | D37, D103 | `int longestColdStreak = 0;`<br>`longestColdStreak = currentColdStreak;` |
| dryDays | D20, D75, D157 | `int dryDays = 0;`<br>`dryDays += 1;`<br>`dryDays += 1;` |
| maxWind | D15, D69 | `int maxWind = -1000;`<br>`maxWind = wind[day][hour];` |
| humidityVarianceAccumulator | D46, D118 | `int humidityVarianceAccumulator = 0;`<br>`humidityVarianceAccumulator += humidityDiffMean * humidityDiffMean;` |
| coldDays | D18, D72 | `int coldDays = 0;`<br>`coldDays += 1;` |
| normalized | D48, D120 | `int normalized = 0;`<br>`normalized = temp[day][hour] - minTemp;` |
| belowAverageCount | D41, D124, D155 | `int belowAverageCount = 0;`<br>`belowAverageCount += 1;`<br>`belowAverageCount += 1;` |
| sequentialDrop | D30, D96 | `int sequentialDrop = 0;`<br>`sequentialDrop = 0;` |
| trendUp | D23, D128, D144, D161 | `int trendUp = 0;`<br>`trendUp += 1;`<br>`trendUp += 1;`<br>`trendUp += 1;` |
| normalizedHumidity | D49, D121 | `int normalizedHumidity = 0;`<br>`normalizedHumidity = humidity[day][hour] - minHumidity;` |
| maxHumidity | D13, D67 | `int maxHumidity = -1000;`<br>`maxHumidity = humidity[day][hour];` |
| currentTrend | D33, D94 | `int currentTrend = 0;`<br>`currentTrend = 0;` |
| sameTrendStreak | D31, D100 | `int sameTrendStreak = 0;`<br>`sameTrendStreak = 1;` |
