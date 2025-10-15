### Block B1
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| reorderCount | D6, D46 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |
| categoryIndex | D44, D50 | `categoryIndex = 0`<br>`categoryIndex++` |

### Block B2
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| reorderCount | D6, D46 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |
| categoryIndex | D44, D50 | `categoryIndex = 0`<br>`categoryIndex++` |

### Block B3
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| categoryIndex | D44, D50 | `categoryIndex = 0`<br>`categoryIndex++` |

### Block B4
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| reorderCount | D6, D46 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |
| categoryIndex | D44, D50 | `categoryIndex = 0`<br>`categoryIndex++` |

### Block B5
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| categoryIndex | D51, D61 | `categoryIndex = 0`<br>`categoryIndex++` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| storeIndex | D13, D52, D60 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| weekIndex | D15, D53, D59 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++` |

### Block B6
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| categoryIndex | D51, D61 | `categoryIndex = 0`<br>`categoryIndex++` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| weekIndex | D15, D53, D59 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++` |
| storeIndex | D13, D52, D60 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |

### Block B7
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| categoryIndex | D51, D61 | `categoryIndex = 0`<br>`categoryIndex++` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| weekIndex | D15, D53, D59 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++` |
| storeIndex | D52, D60 | `storeIndex = 0`<br>`storeIndex++` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |

### Block B8
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| categoryIndex | D51, D61 | `categoryIndex = 0`<br>`categoryIndex++` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| weekIndex | D15, D53, D59 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++` |
| storeIndex | D13, D52, D60 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |

### Block B9
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| categoryIndex | D51, D61 | `categoryIndex = 0`<br>`categoryIndex++` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| storeIndex | D52, D60 | `storeIndex = 0`<br>`storeIndex++` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| weekIndex | D15, D53, D59 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++` |

### Block B10
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| categoryIndex | D51, D61 | `categoryIndex = 0`<br>`categoryIndex++` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| weekIndex | D15, D53, D59 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++` |
| storeIndex | D52, D60 | `storeIndex = 0`<br>`storeIndex++` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |

### Block B11
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| categoryIndex | D51, D61 | `categoryIndex = 0`<br>`categoryIndex++` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| weekIndex | D53, D59 | `weekIndex = 0`<br>`weekIndex++` |
| storeIndex | D52, D60 | `storeIndex = 0`<br>`storeIndex++` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |

### Block B12
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| categoryIndex | D51, D61 | `categoryIndex = 0`<br>`categoryIndex++` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| weekIndex | D15, D53, D59 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++` |
| storeIndex | D52, D60 | `storeIndex = 0`<br>`storeIndex++` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |

### Block B13
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| categoryIndex | D51, D61 | `categoryIndex = 0`<br>`categoryIndex++` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| storeIndex | D52, D60 | `storeIndex = 0`<br>`storeIndex++` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| weekIndex | D53, D59 | `weekIndex = 0`<br>`weekIndex++` |

### Block B14
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| categoryIndex | D51, D61 | `categoryIndex = 0`<br>`categoryIndex++` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| weekIndex | D53, D59 | `weekIndex = 0`<br>`weekIndex++` |
| storeIndex | D52, D60 | `storeIndex = 0`<br>`storeIndex++` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |

### Block B15
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| categoryIndex | D51, D61 | `categoryIndex = 0`<br>`categoryIndex++` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| weekIndex | D53, D59 | `weekIndex = 0`<br>`weekIndex++` |
| storeIndex | D52, D60 | `storeIndex = 0`<br>`storeIndex++` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |

### Block B16
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| categoryIndex | D51, D61 | `categoryIndex = 0`<br>`categoryIndex++` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| weekIndex | D53, D59 | `weekIndex = 0`<br>`weekIndex++` |
| storeIndex | D52, D60 | `storeIndex = 0`<br>`storeIndex++` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |

### Block B17
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| categoryIndex | D51, D61 | `categoryIndex = 0`<br>`categoryIndex++` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| weekIndex | D53, D59 | `weekIndex = 0`<br>`weekIndex++` |
| storeIndex | D52, D60 | `storeIndex = 0`<br>`storeIndex++` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |

### Block B18
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| categoryIndex | D51, D61 | `categoryIndex = 0`<br>`categoryIndex++` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| weekIndex | D53, D59 | `weekIndex = 0`<br>`weekIndex++` |
| storeIndex | D52, D60 | `storeIndex = 0`<br>`storeIndex++` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |

### Block B19
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| categoryIndex | D51, D61 | `categoryIndex = 0`<br>`categoryIndex++` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| storeIndex | D52, D60 | `storeIndex = 0`<br>`storeIndex++` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| weekIndex | D53, D59 | `weekIndex = 0`<br>`weekIndex++` |

### Block B20
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| categoryIndex | D51, D61 | `categoryIndex = 0`<br>`categoryIndex++` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| weekIndex | D53, D59 | `weekIndex = 0`<br>`weekIndex++` |
| storeIndex | D52, D60 | `storeIndex = 0`<br>`storeIndex++` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |

### Block B21
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| categoryIndex | D51, D61 | `categoryIndex = 0`<br>`categoryIndex++` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| weekIndex | D53, D59 | `weekIndex = 0`<br>`weekIndex++` |
| storeIndex | D52, D60 | `storeIndex = 0`<br>`storeIndex++` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |

### Block B22
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| categoryIndex | D51, D61 | `categoryIndex = 0`<br>`categoryIndex++` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| weekIndex | D53, D59 | `weekIndex = 0`<br>`weekIndex++` |
| storeIndex | D52, D60 | `storeIndex = 0`<br>`storeIndex++` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |

### Block B23
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| categoryIndex | D51, D61 | `categoryIndex = 0`<br>`categoryIndex++` |
| auditFlag | D40, D49 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0` |
| storeIndex | D52, D60 | `storeIndex = 0`<br>`storeIndex++` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| restockPlan | D38, D47 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| clearancePlan | D39, D48 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0` |
| weekIndex | D53, D59 | `weekIndex = 0`<br>`weekIndex++` |

### Block B24
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D13, D52, D60, D66, D95 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B25
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D13, D52, D60, D66, D95 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B26
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B27
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D13, D52, D60, D66, D95 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B28
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B29
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B30
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B31
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B32
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B33
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B34
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B35
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B36
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B37
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B38
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B39
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B40
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B41
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B42
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B43
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B44
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B45
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B46
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B47
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B48
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B49
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B50
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B51
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B52
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B53
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B54
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B55
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B56
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D78, D82, D84 | `currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D79, D81, D85 | `currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D77, D80, D83 | `trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B57
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B58
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B59
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B60
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| currentDeclineStreak | D81, D85 | `currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D80, D83 | `trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| currentGrowthStreak | D82, D84 | `currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |

### Block B61
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B62
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D78, D82, D84 | `currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D79, D81, D85 | `currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D77, D80, D83 | `trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B63
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D78, D82, D84 | `currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D79, D81, D85 | `currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D77, D80, D83 | `trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B64
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D78, D82, D84 | `currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D79, D81, D85 | `currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| sameTrendCount | D86, D87 | `sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D77, D80, D83 | `trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B65
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D78, D82, D84 | `currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D79, D81, D85 | `currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D77, D80, D83 | `trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B66
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D78, D82, D84 | `currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D79, D81, D85 | `currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D86, D87 | `sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D77, D80, D83 | `trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B67
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D78, D82, D84 | `currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D79, D81, D85 | `currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D86, D87 | `sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D77, D80, D83 | `trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B68
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D78, D82, D84 | `currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D79, D81, D85 | `currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| sameTrendCount | D86, D87 | `sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D77, D80, D83 | `trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B69
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D78, D82, D84 | `currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D79, D81, D85 | `currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D86, D87 | `sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D77, D80, D83 | `trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B70
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D78, D82, D84 | `currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D79, D81, D85 | `currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| sameTrendCount | D86, D87 | `sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D77, D80, D83 | `trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B71
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D78, D82, D84 | `currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D79, D81, D85 | `currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| sameTrendCount | D86, D87 | `sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D77, D80, D83 | `trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B72
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B73
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B74
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B75
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| weekIndex | D68, D92 | `weekIndex = 0`<br>`weekIndex++` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B76
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B77
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B78
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B79
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B80
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B81
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B82
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B83
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B84
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B85
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B86
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B87
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B88
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B89
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B90
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B91
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| storeIndex | D66, D95 | `storeIndex = 0`<br>`storeIndex++` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| categoryIndex | D64, D104 | `categoryIndex = 0`<br>`categoryIndex++` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| weekIndex | D15, D53, D59, D68, D92 | `int weekIndex = 0`<br>`weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B92
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115 | `weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| categoryIndex | D64, D104, D107, D113 | `categoryIndex = 0`<br>`categoryIndex++`<br>`categoryIndex = 0`<br>`categoryIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B93
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115 | `weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| categoryIndex | D64, D104, D107, D113 | `categoryIndex = 0`<br>`categoryIndex++`<br>`categoryIndex = 0`<br>`categoryIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B94
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115 | `weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| categoryIndex | D107, D113 | `categoryIndex = 0`<br>`categoryIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B95
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115 | `weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| categoryIndex | D64, D104, D107, D113 | `categoryIndex = 0`<br>`categoryIndex++`<br>`categoryIndex = 0`<br>`categoryIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B96
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115 | `weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| categoryIndex | D107, D113 | `categoryIndex = 0`<br>`categoryIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B97
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115 | `weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| categoryIndex | D107, D113 | `categoryIndex = 0`<br>`categoryIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B98
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115 | `weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| storeIndex | D109, D111 | `storeIndex = 0`<br>`storeIndex++` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| categoryIndex | D107, D113 | `categoryIndex = 0`<br>`categoryIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B99
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115 | `weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| categoryIndex | D107, D113 | `categoryIndex = 0`<br>`categoryIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B100
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115 | `weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| storeIndex | D109, D111 | `storeIndex = 0`<br>`storeIndex++` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| categoryIndex | D107, D113 | `categoryIndex = 0`<br>`categoryIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B101
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115 | `weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| storeIndex | D109, D111 | `storeIndex = 0`<br>`storeIndex++` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| categoryIndex | D107, D113 | `categoryIndex = 0`<br>`categoryIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B102
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115 | `weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| storeIndex | D109, D111 | `storeIndex = 0`<br>`storeIndex++` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| categoryIndex | D107, D113 | `categoryIndex = 0`<br>`categoryIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B103
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115 | `weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| storeIndex | D109, D111 | `storeIndex = 0`<br>`storeIndex++` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| categoryIndex | D107, D113 | `categoryIndex = 0`<br>`categoryIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B104
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115 | `weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| storeIndex | D109, D111 | `storeIndex = 0`<br>`storeIndex++` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| categoryIndex | D107, D113 | `categoryIndex = 0`<br>`categoryIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B105
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115 | `weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| storeIndex | D109, D111 | `storeIndex = 0`<br>`storeIndex++` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| categoryIndex | D107, D113 | `categoryIndex = 0`<br>`categoryIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B106
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115 | `weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| storeIndex | D109, D111 | `storeIndex = 0`<br>`storeIndex++` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| categoryIndex | D107, D113 | `categoryIndex = 0`<br>`categoryIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B107
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115 | `weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| categoryIndex | D107, D113 | `categoryIndex = 0`<br>`categoryIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B108
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115 | `weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| categoryIndex | D107, D113 | `categoryIndex = 0`<br>`categoryIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B109
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115 | `weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| categoryIndex | D107, D113 | `categoryIndex = 0`<br>`categoryIndex++` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B110
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B111
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B112
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B113
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B114
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B115
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B116
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| weekIndex | D121, D125 | `weekIndex = 0`<br>`weekIndex++` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B117
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B118
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| weekIndex | D121, D125 | `weekIndex = 0`<br>`weekIndex++` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B119
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| weekIndex | D121, D125 | `weekIndex = 0`<br>`weekIndex++` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B120
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| weekIndex | D121, D125 | `weekIndex = 0`<br>`weekIndex++` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B121
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| weekIndex | D121, D125 | `weekIndex = 0`<br>`weekIndex++` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B122
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| weekIndex | D121, D125 | `weekIndex = 0`<br>`weekIndex++` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B123
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| weekIndex | D121, D125 | `weekIndex = 0`<br>`weekIndex++` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B124
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| weekIndex | D121, D125 | `weekIndex = 0`<br>`weekIndex++` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B125
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| weekIndex | D121, D125 | `weekIndex = 0`<br>`weekIndex++` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B126
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| weekIndex | D121, D125 | `weekIndex = 0`<br>`weekIndex++` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B127
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| weekIndex | D121, D125 | `weekIndex = 0`<br>`weekIndex++` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B128
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B129
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B130
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B131
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B132
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B133
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B134
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B135
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B136
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B137
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B138
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B139
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B140
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B141
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B142
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B143
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| storeIndex | D120, D126 | `storeIndex = 0`<br>`storeIndex++` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B144
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B145
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B146
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| sameTrendCount | D134, D135, D136 | `sameTrendCount += trendGrowth`<br>`sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B147
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B148
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B149
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B150
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| sameTrendCount | D135, D136 | `sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B151
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| sameTrendCount | D31, D86, D87 | `int sameTrendCount = 0`<br>`sameTrendCount += 1`<br>`sameTrendCount = 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B152
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| sameTrendCount | D134, D135, D136 | `sameTrendCount += trendGrowth`<br>`sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B153
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| sameTrendCount | D134, D135, D136 | `sameTrendCount += trendGrowth`<br>`sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B154
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| auditFlag | D137, D138, D139 | `auditFlag[0] = 1`<br>`auditFlag[1] = 1`<br>`auditFlag[2] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| sameTrendCount | D134, D135, D136 | `sameTrendCount += trendGrowth`<br>`sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B155
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| sameTrendCount | D134, D135, D136 | `sameTrendCount += trendGrowth`<br>`sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B156
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| sameTrendCount | D134, D135, D136 | `sameTrendCount += trendGrowth`<br>`sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B157
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| sameTrendCount | D134, D135, D136 | `sameTrendCount += trendGrowth`<br>`sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B158
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| sameTrendCount | D134, D135, D136 | `sameTrendCount += trendGrowth`<br>`sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| auditFlag | D138, D139 | `auditFlag[1] = 1`<br>`auditFlag[2] = 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B159
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| auditFlag | D40, D49, D98 | `int auditFlag[8]`<br>`auditFlag[categoryIndex] = 0`<br>`auditFlag[categoryIndex] = 1` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| sameTrendCount | D134, D135, D136 | `sameTrendCount += trendGrowth`<br>`sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B160
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| sameTrendCount | D134, D135, D136 | `sameTrendCount += trendGrowth`<br>`sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| auditFlag | D137, D138, D139 | `auditFlag[0] = 1`<br>`auditFlag[1] = 1`<br>`auditFlag[2] = 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B161
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132 | `int balanced = 0`<br>`balanced += 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| sameTrendCount | D134, D135, D136 | `sameTrendCount += trendGrowth`<br>`sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| auditFlag | D137, D138, D139 | `auditFlag[0] = 1`<br>`auditFlag[1] = 1`<br>`auditFlag[2] = 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B162
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| auditFlag | D137, D138, D139 | `auditFlag[0] = 1`<br>`auditFlag[1] = 1`<br>`auditFlag[2] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| sameTrendCount | D134, D135, D136 | `sameTrendCount += trendGrowth`<br>`sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132, D140 | `int balanced = 0`<br>`balanced += 1`<br>`balanced = balanced - exceptionCount` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B163
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132, D140 | `int balanced = 0`<br>`balanced += 1`<br>`balanced = balanced - exceptionCount` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| sameTrendCount | D134, D135, D136 | `sameTrendCount += trendGrowth`<br>`sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| auditFlag | D137, D138, D139 | `auditFlag[0] = 1`<br>`auditFlag[1] = 1`<br>`auditFlag[2] = 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B164
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132, D140 | `int balanced = 0`<br>`balanced += 1`<br>`balanced = balanced - exceptionCount` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| sameTrendCount | D134, D135, D136 | `sameTrendCount += trendGrowth`<br>`sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| auditFlag | D137, D138, D139 | `auditFlag[0] = 1`<br>`auditFlag[1] = 1`<br>`auditFlag[2] = 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B165
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131, D142 | `int overStocked = 0`<br>`overStocked += 1`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| auditFlag | D137, D138, D139 | `auditFlag[0] = 1`<br>`auditFlag[1] = 1`<br>`auditFlag[2] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| sameTrendCount | D134, D135, D136 | `sameTrendCount += trendGrowth`<br>`sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132, D140, D141 | `int balanced = 0`<br>`balanced += 1`<br>`balanced = balanced - exceptionCount`<br>`balanced += 1` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B166
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131 | `int overStocked = 0`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132, D140 | `int balanced = 0`<br>`balanced += 1`<br>`balanced = balanced - exceptionCount` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| sameTrendCount | D134, D135, D136 | `sameTrendCount += trendGrowth`<br>`sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| auditFlag | D137, D138, D139 | `auditFlag[0] = 1`<br>`auditFlag[1] = 1`<br>`auditFlag[2] = 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B167
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131, D142 | `int overStocked = 0`<br>`overStocked += 1`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132, D140, D141 | `int balanced = 0`<br>`balanced += 1`<br>`balanced = balanced - exceptionCount`<br>`balanced += 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| sameTrendCount | D134, D135, D136 | `sameTrendCount += trendGrowth`<br>`sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| auditFlag | D137, D138, D139 | `auditFlag[0] = 1`<br>`auditFlag[1] = 1`<br>`auditFlag[2] = 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B168
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131, D142 | `int overStocked = 0`<br>`overStocked += 1`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132, D140, D141 | `int balanced = 0`<br>`balanced += 1`<br>`balanced = balanced - exceptionCount`<br>`balanced += 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| sameTrendCount | D134, D135, D136 | `sameTrendCount += trendGrowth`<br>`sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| auditFlag | D137, D138, D139 | `auditFlag[0] = 1`<br>`auditFlag[1] = 1`<br>`auditFlag[2] = 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |

### Block B169
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131, D142 | `int overStocked = 0`<br>`overStocked += 1`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129, D143 | `int trendStable = 0`<br>`trendStable += 1`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| trendDecline | D21, D127, D144 | `int trendDecline = 0`<br>`trendDecline += 1`<br>`trendDecline += 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| auditFlag | D137, D138, D139 | `auditFlag[0] = 1`<br>`auditFlag[1] = 1`<br>`auditFlag[2] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| sameTrendCount | D134, D135, D136 | `sameTrendCount += trendGrowth`<br>`sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132, D140, D141 | `int balanced = 0`<br>`balanced += 1`<br>`balanced = balanced - exceptionCount`<br>`balanced += 1` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |

### Block B170
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weekIndex | D105, D115, D121, D125 | `weekIndex = 0`<br>`weekIndex++`<br>`weekIndex = 0`<br>`weekIndex++` |
| totalDeficit | D8, D56 | `int totalDeficit = 0`<br>`totalDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| balancedStores | D43, D94 | `int balancedStores = 0`<br>`balancedStores += 1` |
| currentGrowthStreak | D36, D78, D82, D84 | `int currentGrowthStreak = 0`<br>`currentGrowthStreak += 1`<br>`currentGrowthStreak = 0`<br>`currentGrowthStreak = 0` |
| outOfStock | D10, D130 | `int outOfStock = 0`<br>`outOfStock += 1` |
| storeIndex | D13, D52, D60, D66, D95, D109, D111, D120, D126 | `int storeIndex = 0`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++`<br>`storeIndex = 0`<br>`storeIndex++` |
| overStocked | D11, D131, D142 | `int overStocked = 0`<br>`overStocked += 1`<br>`overStocked += 1` |
| longestGrowthStreak | D34, D88 | `int longestGrowthStreak = 0`<br>`longestGrowthStreak = currentGrowthStreak` |
| balancedWeeks | D42, D114 | `int balancedWeeks = 0`<br>`balancedWeeks += 1` |
| totalCategoryDeficit | D118, D123 | `int totalCategoryDeficit = 0`<br>`totalCategoryDeficit += reorderThreshold[categoryIndex] - stock[categoryIndex][storeIndex][weekIndex]` |
| exceptionCount | D41, D99 | `int exceptionCount = 0`<br>`exceptionCount += 1` |
| trendStable | D22, D129 | `int trendStable = 0`<br>`trendStable += 1` |
| minVarianceCategory | D27, D103 | `int minVarianceCategory = 0`<br>`minVarianceCategory = tempVariance` |
| currentDeclineStreak | D37, D79, D81, D85 | `int currentDeclineStreak = 0`<br>`currentDeclineStreak = 0`<br>`currentDeclineStreak += 1`<br>`currentDeclineStreak = 0` |
| runningTotal | D67, D91 | `int runningTotal = 0`<br>`runningTotal += stock[categoryIndex][storeIndex][weekIndex]` |
| balanced | D12, D132, D140, D141 | `int balanced = 0`<br>`balanced += 1`<br>`balanced = balanced - exceptionCount`<br>`balanced += 1` |
| clearancePlan | D39, D48, D97 | `int clearancePlan[8]`<br>`clearancePlan[categoryIndex] = 0`<br>`clearancePlan[categoryIndex] = 1` |
| cumulativeVariance | D25, D101 | `int cumulativeVariance = 0`<br>`cumulativeVariance += tempVariance` |
| trendGrowth | D20, D128 | `int trendGrowth = 0`<br>`trendGrowth += 1` |
| trendDecline | D21, D127 | `int trendDecline = 0`<br>`trendDecline += 1` |
| lastTrendDirection | D33, D90 | `int lastTrendDirection = 0`<br>`lastTrendDirection = trendDirection` |
| totalWeekStock | D108, D110 | `int totalWeekStock = 0`<br>`totalWeekStock += stock[categoryIndex][storeIndex][weekIndex]` |
| totalSurplus | D9, D58 | `int totalSurplus = 0`<br>`totalSurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| demandDrop | D18, D76 | `int demandDrop[8][12]`<br>`demandDrop[categoryIndex][storeIndex] += 1` |
| stock | D4, D54 | `int stock[8][12][10]`<br>`stock[categoryIndex][storeIndex][weekIndex] = ((((categoryIndex * 13) + (storeIndex * 7)) + (weekIndex * 5)) % 200) + 20` |
| sameTrendCount | D134, D135, D136 | `sameTrendCount += trendGrowth`<br>`sameTrendCount += trendDecline`<br>`sameTrendCount += trendStable` |
| totalCategoryStock | D117, D122 | `int totalCategoryStock = 0`<br>`totalCategoryStock += stock[categoryIndex][storeIndex][weekIndex]` |
| previousStock | D30, D73 | `int previousStock = 0`<br>`previousStock = stock[categoryIndex][storeIndex][weekIndex - 1]` |
| reorderCount | D6, D46, D57 | `int reorderCount[8]`<br>`reorderCount[categoryIndex] = 0`<br>`reorderCount[categoryIndex] += 1` |
| tempVariance | D28, D100 | `int tempVariance = 0`<br>`tempVariance = highestStock - lowestStock` |
| trendDirection | D32, D77, D80, D83 | `int trendDirection = 0`<br>`trendDirection = 1`<br>`trendDirection = -1`<br>`trendDirection = 0` |
| totalCategorySurplus | D119, D124 | `int totalCategorySurplus = 0`<br>`totalCategorySurplus += stock[categoryIndex][storeIndex][weekIndex] - (reorderThreshold[categoryIndex] * 2)` |
| categoryIndex | D116, D133 | `categoryIndex = 0`<br>`categoryIndex++` |
| auditFlag | D137, D138, D139 | `auditFlag[0] = 1`<br>`auditFlag[1] = 1`<br>`auditFlag[2] = 1` |
| restockPlan | D38, D47, D96 | `int restockPlan[8]`<br>`restockPlan[categoryIndex] = 0`<br>`restockPlan[categoryIndex] = 1` |
| lowestStock | D63, D72 | `lowestStock = highestStock`<br>`lowestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| maxVarianceCategory | D26, D102 | `int maxVarianceCategory = 0`<br>`maxVarianceCategory = tempVariance` |
| reorderThreshold | D5, D45 | `int reorderThreshold[8]`<br>`reorderThreshold[categoryIndex] = 50 + (categoryIndex * 5)` |
| totalStock | D7, D55 | `int totalStock = 0`<br>`totalStock += stock[categoryIndex][storeIndex][weekIndex]` |
| highestStock | D62, D71 | `highestStock = totalStock / ((categories * stores) * weeks)`<br>`highestStock = stock[categoryIndex][storeIndex][weekIndex]` |
| longestDeclineStreak | D35, D89 | `int longestDeclineStreak = 0`<br>`longestDeclineStreak = currentDeclineStreak` |
| movingAvg | D19, D93 | `int movingAvg[8][12]`<br>`movingAvg[categoryIndex][storeIndex] = runningTotal / weeks` |
| stockChange | D29, D74 | `int stockChange = 0`<br>`stockChange = stock[categoryIndex][storeIndex][weekIndex] - previousStock` |
| demandSpike | D17, D75 | `int demandSpike[8][12]`<br>`demandSpike[categoryIndex][storeIndex] += 1` |
| forecast | D16, D70 | `int forecast[8][12]`<br>`forecast[categoryIndex][storeIndex] = runningTotal / weeks` |
| weekBalanced | D106, D112 | `int weekBalanced = 0`<br>`weekBalanced += 1` |
