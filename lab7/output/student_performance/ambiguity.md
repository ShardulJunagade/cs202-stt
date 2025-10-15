### Block B1
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| subjectIndex | D40, D43 | `subjectIndex = 0;`<br>`subjectIndex++;` |

### Block B2
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| subjectIndex | D40, D43 | `subjectIndex = 0;`<br>`subjectIndex++;` |

### Block B3
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D41, D42 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| subjectIndex | D40, D43 | `subjectIndex = 0;`<br>`subjectIndex++;` |

### Block B4
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| subjectIndex | D40, D43 | `subjectIndex = 0;`<br>`subjectIndex++;` |

### Block B5
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D41, D42 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| subjectIndex | D40, D43 | `subjectIndex = 0;`<br>`subjectIndex++;` |

### Block B6
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D41, D42 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| subjectIndex | D40, D43 | `subjectIndex = 0;`<br>`subjectIndex++;` |

### Block B7
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D41, D42 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| subjectIndex | D40, D43 | `subjectIndex = 0;`<br>`subjectIndex++;` |

### Block B8
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D41, D42 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| subjectIndex | D40, D43 | `subjectIndex = 0;`<br>`subjectIndex++;` |

### Block B9
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| subjectIndex | D40, D43 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| studentIndex | D44, D45 | `studentIndex = 0;`<br>`studentIndex++;` |

### Block B10
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| subjectIndex | D40, D43 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| studentIndex | D44, D45 | `studentIndex = 0;`<br>`studentIndex++;` |

### Block B11
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| subjectIndex | D40, D43 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| studentIndex | D44, D45 | `studentIndex = 0;`<br>`studentIndex++;` |

### Block B12
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| subjectIndex | D40, D43 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| studentIndex | D44, D45 | `studentIndex = 0;`<br>`studentIndex++;` |

### Block B13
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| subjectIndex | D40, D43, D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;`<br>`subjectIndex = 0;`<br>`subjectIndex++;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |

### Block B14
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D40, D43, D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;`<br>`subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B15
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B16
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D40, D43, D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;`<br>`subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B17
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |

### Block B18
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B19
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B20
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B21
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |

### Block B22
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B23
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B24
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B25
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B26
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B27
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |

### Block B28
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B29
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B30
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |

### Block B31
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B32
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B33
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B34
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B35
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |

### Block B36
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B37
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |

### Block B38
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B39
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B40
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B41
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |

### Block B42
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B43
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B44
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |

### Block B45
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B46
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B47
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D50, D53 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D49, D52 | `totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| totalScore | D48, D51 | `totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |

### Block B48
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B49
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B50
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |

### Block B51
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B52
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B53
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B54
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |

### Block B55
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B56
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B57
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B58
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |

### Block B59
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B60
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B61
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| subjectIndex | D47, D61 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |

### Block B62
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D67, D68 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |

### Block B63
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D67, D68 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B64
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D67, D68 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B65
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D13, D41, D42, D50, D53 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| subjectIndex | D67, D68 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66 | `studentIndex = 0;`<br>`studentIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| auditFlag | D10, D65 | `int auditFlag = 0;`<br>`auditFlag += 1;` |

### Block B66
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66, D71, D78 | `studentIndex = 0;`<br>`studentIndex++;`<br>`studentIndex = 0;`<br>`studentIndex++;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B67
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66, D71, D78 | `studentIndex = 0;`<br>`studentIndex++;`<br>`studentIndex = 0;`<br>`studentIndex++;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B68
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| studentIndex | D71, D78 | `studentIndex = 0;`<br>`studentIndex++;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B69
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| studentIndex | D46, D66, D71, D78 | `studentIndex = 0;`<br>`studentIndex++;`<br>`studentIndex = 0;`<br>`studentIndex++;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B70
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| studentIndex | D71, D78 | `studentIndex = 0;`<br>`studentIndex++;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B71
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| studentIndex | D71, D78 | `studentIndex = 0;`<br>`studentIndex++;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B72
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| studentIndex | D71, D78 | `studentIndex = 0;`<br>`studentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| assessmentIndex | D73, D75 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |

### Block B73
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| studentIndex | D71, D78 | `studentIndex = 0;`<br>`studentIndex++;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B74
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| studentIndex | D71, D78 | `studentIndex = 0;`<br>`studentIndex++;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| assessmentIndex | D73, D75 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B75
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| studentIndex | D71, D78 | `studentIndex = 0;`<br>`studentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| assessmentIndex | D73, D75 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |

### Block B76
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D71, D78 | `studentIndex = 0;`<br>`studentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| assessmentIndex | D73, D75 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |

### Block B77
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| studentIndex | D71, D78 | `studentIndex = 0;`<br>`studentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| assessmentIndex | D73, D75 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |

### Block B78
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| studentIndex | D71, D78 | `studentIndex = 0;`<br>`studentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| assessmentIndex | D73, D75 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |

### Block B79
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| studentIndex | D71, D78 | `studentIndex = 0;`<br>`studentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| assessmentIndex | D73, D75 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |

### Block B80
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| studentIndex | D71, D78 | `studentIndex = 0;`<br>`studentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| assessmentIndex | D73, D75 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |

### Block B81
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| studentIndex | D71, D78 | `studentIndex = 0;`<br>`studentIndex++;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| assessmentIndex | D73, D75 | `assessmentIndex = 0;`<br>`assessmentIndex++;` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |

### Block B82
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| studentIndex | D71, D78 | `studentIndex = 0;`<br>`studentIndex++;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B83
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| studentIndex | D71, D78 | `studentIndex = 0;`<br>`studentIndex++;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B84
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55 | `int distinctionCount = 0;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54 | `int passCount = 0;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| failCount | D8, D56 | `int failCount = 0;`<br>`failCount += 1;` |
| studentIndex | D71, D78 | `studentIndex = 0;`<br>`studentIndex++;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B85
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B86
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B87
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B88
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B89
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B90
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B91
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B92
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B93
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B94
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B95
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B96
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B97
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B98
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B99
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B100
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B101
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B102
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B103
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B104
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B105
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B106
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| auditFlag | D10, D65, D79, D87 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B107
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| auditFlag | D10, D65, D79, D87 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B108
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| auditFlag | D10, D65, D79, D87 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B109
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| failCount | D8, D56, D84 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;` |
| auditFlag | D10, D65, D79, D87 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |

### Block B110
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| totalSubjectScore | D72, D74 | `int totalSubjectScore = 0;`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| assessmentIndex | D13, D41, D42, D50, D53, D73, D75 | `int assessmentIndex = 0;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;`<br>`assessmentIndex = 0;`<br>`assessmentIndex++;` |
| attendanceWarning | D36, D62, D82 | `int attendanceWarning = 0;`<br>`attendanceWarning += 1;`<br>`attendanceWarning += 1;` |
| totalWeightedScore | D15, D49, D52 | `int totalWeightedScore = 0;`<br>`totalWeightedScore = 0;`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| distinctionCount | D9, D55, D83 | `int distinctionCount = 0;`<br>`distinctionCount += 1;`<br>`distinctionCount += 1;` |
| bestDecline | D24, D58 | `int bestDecline = 0;`<br>`bestDecline = declineStreak[studentIndex];` |
| studentIndex | D81, D86 | `studentIndex = 0;`<br>`studentIndex++;` |
| auditFlag | D10, D65, D79, D87 | `int auditFlag = 0;`<br>`auditFlag += 1;`<br>`auditFlag += 1;`<br>`auditFlag += 1;` |
| failCount | D8, D56, D84, D88 | `int failCount = 0;`<br>`failCount += 1;`<br>`failCount += 1;`<br>`failCount += auditFlag;` |
| subjectDeviation | D34, D60 | `int subjectDeviation = 0;`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| passCount | D7, D54, D85, D89 | `int passCount = 0;`<br>`passCount += 1;`<br>`passCount += 1;`<br>`passCount += auditFlag;` |
| consistentPerformers | D25, D63 | `int consistentPerformers = 0;`<br>`consistentPerformers += 1;` |
| totalScore | D14, D48, D51 | `int totalScore = 0;`<br>`totalScore = 0;`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| deviationAccumulator | D33, D59 | `int deviationAccumulator = 0;`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| bestImprovement | D23, D57 | `int bestImprovement = 0;`<br>`bestImprovement = improvementStreak[studentIndex];` |
| subjectIndex | D69, D80 | `subjectIndex = 0;`<br>`subjectIndex++;` |
| irregularPerformers | D26, D64 | `int irregularPerformers = 0;`<br>`irregularPerformers += 1;` |
| varianceAccumulator | D70, D77 | `int varianceAccumulator = 0;`<br>`varianceAccumulator += diff * diff;` |
