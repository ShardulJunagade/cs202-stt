### Block B1
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0` |
| assessmentIndex | D13, D47, D49 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectTopper | D18, D43 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0` |
| classAverage | D31, D45 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000` |
| subjectIndex | D40, D50 | `subjectIndex = 0`<br>`subjectIndex++` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B2
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| subjectTopper | D18, D43 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0` |
| assessmentIndex | D13, D47, D49 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000` |
| classAverage | D31, D45 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0` |
| subjectIndex | D40, D50 | `subjectIndex = 0`<br>`subjectIndex++` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B3
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D47, D49 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectIndex | D40, D50 | `subjectIndex = 0`<br>`subjectIndex++` |

### Block B4
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| subjectTopper | D18, D43 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0` |
| assessmentIndex | D13, D47, D49 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000` |
| classAverage | D31, D45 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0` |
| subjectIndex | D40, D50 | `subjectIndex = 0`<br>`subjectIndex++` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B5
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D47, D49 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectIndex | D40, D50 | `subjectIndex = 0`<br>`subjectIndex++` |

### Block B6
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D47, D49 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectIndex | D40, D50 | `subjectIndex = 0`<br>`subjectIndex++` |

### Block B7
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| assessmentIndex | D47, D49 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectIndex | D40, D50 | `subjectIndex = 0`<br>`subjectIndex++` |

### Block B8
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D47, D49 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectIndex | D40, D50 | `subjectIndex = 0`<br>`subjectIndex++` |

### Block B9
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0` |
| assessmentIndex | D13, D47, D49 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| improvementStreak | D20, D52 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0` |
| declineStreak | D21, D53 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0` |
| consistentStreak | D22, D54 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0` |
| remedialPlan | D30, D57 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0` |
| classAverage | D31, D45 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000` |
| subjectIndex | D40, D50 | `subjectIndex = 0`<br>`subjectIndex++` |
| studentIndex | D51, D62 | `studentIndex = 0`<br>`studentIndex++` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B10
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| warningIssued | D28, D55 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0` |
| subjectTopper | D18, D43 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0` |
| excellenceAward | D29, D56 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0` |
| assessmentIndex | D13, D47, D49 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000` |
| classAverage | D31, D45 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0` |
| subjectIndex | D40, D50 | `subjectIndex = 0`<br>`subjectIndex++` |
| declineStreak | D21, D53 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| improvementStreak | D20, D52 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0` |
| consistentStreak | D22, D54 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| studentIndex | D51, D62 | `studentIndex = 0`<br>`studentIndex++` |
| remedialPlan | D30, D57 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B11
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| subjectTopper | D18, D43 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0` |
| assessmentIndex | D13, D47, D49 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000` |
| classAverage | D31, D45 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0` |
| subjectIndex | D40, D50 | `subjectIndex = 0`<br>`subjectIndex++` |
| studentIndex | D51, D62 | `studentIndex = 0`<br>`studentIndex++` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B12
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| warningIssued | D28, D55 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0` |
| subjectTopper | D18, D43 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0` |
| excellenceAward | D29, D56 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0` |
| assessmentIndex | D13, D47, D49 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000` |
| classAverage | D31, D45 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0` |
| subjectIndex | D40, D50 | `subjectIndex = 0`<br>`subjectIndex++` |
| declineStreak | D21, D53 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| improvementStreak | D20, D52 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0` |
| consistentStreak | D22, D54 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| studentIndex | D51, D62 | `studentIndex = 0`<br>`studentIndex++` |
| remedialPlan | D30, D57 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B13
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectIndex | D40, D50, D64, D90 | `subjectIndex = 0`<br>`subjectIndex++`<br>`subjectIndex = 0`<br>`subjectIndex++` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B14
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D40, D50, D64, D90 | `subjectIndex = 0`<br>`subjectIndex++`<br>`subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B15
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B16
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D40, D50, D64, D90 | `subjectIndex = 0`<br>`subjectIndex++`<br>`subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B17
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B18
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B19
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B20
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B21
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B22
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B23
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B24
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B25
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B26
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B27
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B28
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B29
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B30
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B31
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B32
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B33
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B34
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B35
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B36
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B37
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B38
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B39
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B40
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B41
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B42
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B43
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B44
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B45
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B46
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B47
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B48
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B49
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B50
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B51
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D66, D70 | `totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D65, D69 | `totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| assessmentIndex | D67, D71 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B52
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B53
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B54
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B55
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B56
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B57
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B58
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B59
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B60
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B61
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B62
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B63
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B64
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B65
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B66
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B67
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B68
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B69
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B70
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B71
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B72
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classAverage | D31, D45, D74 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectIndex | D64, D90 | `subjectIndex = 0`<br>`subjectIndex++` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B73
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| subjectIndex | D100, D102 | `subjectIndex = 0`<br>`subjectIndex++` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |

### Block B74
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| subjectIndex | D100, D102 | `subjectIndex = 0`<br>`subjectIndex++` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B75
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| subjectIndex | D100, D102 | `subjectIndex = 0`<br>`subjectIndex++` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B76
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| remedialPlan | D30, D57, D80, D94 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| auditFlag | D10, D98 | `int auditFlag = 0`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| assessmentIndex | D13, D47, D49, D67, D71 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| studentIndex | D63, D99 | `studentIndex = 0`<br>`studentIndex++` |
| subjectIndex | D100, D102 | `subjectIndex = 0`<br>`subjectIndex++` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| classVariance | D32, D46 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B77
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D63, D99, D105, D114 | `studentIndex = 0`<br>`studentIndex++`<br>`studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |

### Block B78
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D63, D99, D105, D114 | `studentIndex = 0`<br>`studentIndex++`<br>`studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B79
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D105, D114 | `studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B80
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D63, D99, D105, D114 | `studentIndex = 0`<br>`studentIndex++`<br>`studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B81
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D105, D114 | `studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |

### Block B82
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D105, D114 | `studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B83
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D105, D114 | `studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D107, D109 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B84
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D105, D114 | `studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B85
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D105, D114 | `studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| assessmentIndex | D107, D109 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |

### Block B86
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D105, D114 | `studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D107, D109 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B87
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D105, D114 | `studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D107, D109 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B88
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D105, D114 | `studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D107, D109 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B89
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D105, D114 | `studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D107, D109 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B90
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D105, D114 | `studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D107, D109 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B91
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D105, D114 | `studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| assessmentIndex | D107, D109 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |

### Block B92
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D105, D114 | `studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D107, D109 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B93
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D105, D114 | `studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D107, D109 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B94
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D105, D114 | `studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D107, D109 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B95
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D105, D114 | `studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| assessmentIndex | D107, D109 | `assessmentIndex = 0`<br>`assessmentIndex++` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |

### Block B96
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D105, D114 | `studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B97
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D105, D114 | `studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B98
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| studentIndex | D105, D114 | `studentIndex = 0`<br>`studentIndex++` |
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| attendanceWarning | D36, D91 | `int attendanceWarning = 0`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| failCount | D8, D79 | `int failCount = 0`<br>`failCount += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77 | `int distinctionCount = 0`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| passCount | D7, D75 | `int passCount = 0`<br>`passCount += 1` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |

### Block B99
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |

### Block B100
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B101
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B102
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B103
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B104
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B105
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |

### Block B106
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B107
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B108
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |

### Block B109
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B110
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B111
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B112
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |

### Block B113
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B114
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B115
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B116
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| gradeDistribution | D124, D125, D126 | `gradeDistribution[0] += consistentPerformers`<br>`gradeDistribution[1] += irregularPerformers`<br>`gradeDistribution[2] += consistentPerformers` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |

### Block B117
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B118
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B119
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B120
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| gradeDistribution | D125, D126 | `gradeDistribution[1] += irregularPerformers`<br>`gradeDistribution[2] += consistentPerformers` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |

### Block B121
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D27, D42, D76 | `int gradeDistribution[6]`<br>`gradeDistribution[subjectIndex] = 0`<br>`gradeDistribution[subjectIndex] += 1` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B122
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| gradeDistribution | D124, D125, D126 | `gradeDistribution[0] += consistentPerformers`<br>`gradeDistribution[1] += irregularPerformers`<br>`gradeDistribution[2] += consistentPerformers` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B123
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| gradeDistribution | D124, D125, D126 | `gradeDistribution[0] += consistentPerformers`<br>`gradeDistribution[1] += irregularPerformers`<br>`gradeDistribution[2] += consistentPerformers` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B124
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D127, D128, D129 | `gradeDistribution[3] += bestImprovement`<br>`gradeDistribution[4] += bestDecline`<br>`gradeDistribution[5] += bestImprovement` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |

### Block B125
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| gradeDistribution | D124, D125, D126 | `gradeDistribution[0] += consistentPerformers`<br>`gradeDistribution[1] += irregularPerformers`<br>`gradeDistribution[2] += consistentPerformers` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B126
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| gradeDistribution | D124, D125, D126 | `gradeDistribution[0] += consistentPerformers`<br>`gradeDistribution[1] += irregularPerformers`<br>`gradeDistribution[2] += consistentPerformers` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B127
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| gradeDistribution | D124, D125, D126 | `gradeDistribution[0] += consistentPerformers`<br>`gradeDistribution[1] += irregularPerformers`<br>`gradeDistribution[2] += consistentPerformers` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B128
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D128, D129 | `gradeDistribution[4] += bestDecline`<br>`gradeDistribution[5] += bestImprovement` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |

### Block B129
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| gradeDistribution | D124, D125, D126 | `gradeDistribution[0] += consistentPerformers`<br>`gradeDistribution[1] += irregularPerformers`<br>`gradeDistribution[2] += consistentPerformers` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B130
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D127, D128, D129 | `gradeDistribution[3] += bestImprovement`<br>`gradeDistribution[4] += bestDecline`<br>`gradeDistribution[5] += bestImprovement` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B131
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| auditFlag | D10, D98, D116 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D127, D128, D129 | `gradeDistribution[3] += bestImprovement`<br>`gradeDistribution[4] += bestDecline`<br>`gradeDistribution[5] += bestImprovement` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B132
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| auditFlag | D10, D98, D116, D130 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D127, D128, D129 | `gradeDistribution[3] += bestImprovement`<br>`gradeDistribution[4] += bestDecline`<br>`gradeDistribution[5] += bestImprovement` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |

### Block B133
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| auditFlag | D10, D98, D116, D130 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D127, D128, D129 | `gradeDistribution[3] += bestImprovement`<br>`gradeDistribution[4] += bestDecline`<br>`gradeDistribution[5] += bestImprovement` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B134
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| auditFlag | D10, D98, D116, D130 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D127, D128, D129 | `gradeDistribution[3] += bestImprovement`<br>`gradeDistribution[4] += bestDecline`<br>`gradeDistribution[5] += bestImprovement` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |

### Block B135
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| auditFlag | D10, D98, D116, D130 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D127, D128, D129 | `gradeDistribution[3] += bestImprovement`<br>`gradeDistribution[4] += bestDecline`<br>`gradeDistribution[5] += bestImprovement` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121, D131 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1`<br>`failCount += auditFlag` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| passCount | D7, D75, D122, D132 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1`<br>`passCount += auditFlag` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |

### Block B136
| Variable | Definition IDs | Statements |
|----------|----------------|------------|
| excellenceAward | D29, D56, D78, D93, D112 | `int excellenceAward[120]`<br>`excellenceAward[studentIndex] = 0`<br>`excellenceAward[studentIndex] += 1`<br>`excellenceAward[studentIndex] += extraCredits[studentIndex]`<br>`excellenceAward[studentIndex] += 1` |
| remedialPlan | D30, D57, D80, D94, D113 | `int remedialPlan[120]`<br>`remedialPlan[studentIndex] = 0`<br>`remedialPlan[studentIndex] += 1`<br>`remedialPlan[studentIndex] += projectScores[studentIndex] / 10`<br>`remedialPlan[studentIndex] += 1` |
| varianceAccumulator | D104, D111 | `int varianceAccumulator = 0`<br>`varianceAccumulator += diff * diff` |
| auditFlag | D10, D98, D116, D130 | `int auditFlag = 0`<br>`auditFlag += 1`<br>`auditFlag += 1`<br>`auditFlag += 1` |
| participation | D39, D61 | `int participation[120]`<br>`participation[studentIndex] = 50 + (studentIndex % 40)` |
| assessmentIndex | D13, D47, D49, D67, D71, D107, D109 | `int assessmentIndex = 0`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++`<br>`assessmentIndex = 0`<br>`assessmentIndex++` |
| subjectDeviation | D34, D89 | `int subjectDeviation = 0`<br>`subjectDeviation += deviationAccumulator * deviationAccumulator` |
| studentIndex | D118, D123 | `studentIndex = 0`<br>`studentIndex++` |
| totalWeightedScore | D15, D66, D70 | `int totalWeightedScore = 0`<br>`totalWeightedScore = 0`<br>`totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| gradeThresholds | D6, D41 | `int gradeThresholds[6]`<br>`gradeThresholds[subjectIndex] = 200` |
| gradeDistribution | D127, D128, D129 | `gradeDistribution[3] += bestImprovement`<br>`gradeDistribution[4] += bestDecline`<br>`gradeDistribution[5] += bestImprovement` |
| improvementStreak | D20, D52, D81, D84 | `int improvementStreak[120]`<br>`improvementStreak[studentIndex] = 0`<br>`improvementStreak[studentIndex] += 1`<br>`improvementStreak[studentIndex] = 0` |
| failCount | D8, D79, D121 | `int failCount = 0`<br>`failCount += 1`<br>`failCount += 1` |
| attendanceWarning | D36, D91, D119 | `int attendanceWarning = 0`<br>`attendanceWarning += 1`<br>`attendanceWarning += 1` |
| totalScore | D14, D65, D69 | `int totalScore = 0`<br>`totalScore = 0`<br>`totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| bestDecline | D24, D87 | `int bestDecline = 0`<br>`bestDecline = declineStreak[studentIndex]` |
| irregularPerformers | D26, D97 | `int irregularPerformers = 0`<br>`irregularPerformers += 1` |
| classAverage | D31, D45, D74, D101 | `int classAverage[6]`<br>`classAverage[subjectIndex] = 0`<br>`classAverage[subjectIndex] += totalScore`<br>`classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| scores | D4, D68 | `int scores[120][6][5]`<br>`scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| declineStreak | D21, D53, D82, D83 | `int declineStreak[120]`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] = 0`<br>`declineStreak[studentIndex] += 1` |
| consistentStreak | D22, D54, D85, D95 | `int consistentStreak[120]`<br>`consistentStreak[studentIndex] = 0`<br>`consistentStreak[studentIndex] += 1`<br>`consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| deviationAccumulator | D33, D88 | `int deviationAccumulator = 0`<br>`deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| projectScores | D38, D60 | `int projectScores[120]`<br>`projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| totalSubjectScore | D106, D108 | `int totalSubjectScore = 0`<br>`totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| distinctionCount | D9, D77, D120 | `int distinctionCount = 0`<br>`distinctionCount += 1`<br>`distinctionCount += 1` |
| subjectTopper | D18, D43, D72 | `int subjectTopper[6]`<br>`subjectTopper[subjectIndex] = 0`<br>`subjectTopper[subjectIndex] = totalScore` |
| subjectIndex | D103, D117 | `subjectIndex = 0`<br>`subjectIndex++` |
| extraCredits | D37, D59 | `int extraCredits[120]`<br>`extraCredits[studentIndex] = studentIndex % 5` |
| warningIssued | D28, D55, D92 | `int warningIssued[120]`<br>`warningIssued[studentIndex] = 0`<br>`warningIssued[studentIndex] += 1` |
| bestImprovement | D23, D86 | `int bestImprovement = 0`<br>`bestImprovement = improvementStreak[studentIndex]` |
| weights | D5, D48 | `int weights[6][5]`<br>`weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| passCount | D7, D75, D122 | `int passCount = 0`<br>`passCount += 1`<br>`passCount += 1` |
| subjectLowest | D19, D44, D73 | `int subjectLowest[6]`<br>`subjectLowest[subjectIndex] = 10000`<br>`subjectLowest[subjectIndex] = totalScore` |
| classVariance | D32, D46, D115 | `int classVariance[6]`<br>`classVariance[subjectIndex] = 0`<br>`classVariance[subjectIndex] = varianceAccumulator / students` |
| consistentPerformers | D25, D96 | `int consistentPerformers = 0`<br>`consistentPerformers += 1` |
| attendance | D35, D58 | `int attendance[120]`<br>`attendance[studentIndex] = 80 + (studentIndex % 20)` |
