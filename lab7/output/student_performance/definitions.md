| Definition ID | Variable | Block | Line | Statement |
|---------------|----------|-------|------|-----------|
| D1 | students | B0 | 2 | `int students = 120;` |
| D2 | subjects | B0 | 3 | `int subjects = 6;` |
| D3 | assessments | B0 | 4 | `int assessments = 5;` |
| D4 | scores | B0 | 5 | `int scores[120][6][5];` |
| D5 | weights | B0 | 6 | `int weights[6][5];` |
| D6 | gradeThresholds | B0 | 7 | `int gradeThresholds[6];` |
| D7 | passCount | B0 | 8 | `int passCount = 0;` |
| D8 | failCount | B0 | 9 | `int failCount = 0;` |
| D9 | distinctionCount | B0 | 10 | `int distinctionCount = 0;` |
| D10 | auditFlag | B0 | 11 | `int auditFlag = 0;` |
| D11 | studentIndex | B0 | 12 | `int studentIndex = 0;` |
| D12 | subjectIndex | B0 | 13 | `int subjectIndex = 0;` |
| D13 | assessmentIndex | B0 | 14 | `int assessmentIndex = 0;` |
| D14 | totalScore | B0 | 15 | `int totalScore = 0;` |
| D15 | totalWeightedScore | B0 | 16 | `int totalWeightedScore = 0;` |
| D16 | highestScore | B0 | 17 | `int highestScore = 0;` |
| D17 | lowestScore | B0 | 18 | `int lowestScore = 0;` |
| D18 | subjectTopper | B0 | 19 | `int subjectTopper[6];` |
| D19 | subjectLowest | B0 | 20 | `int subjectLowest[6];` |
| D20 | improvementStreak | B0 | 21 | `int improvementStreak[120];` |
| D21 | declineStreak | B0 | 22 | `int declineStreak[120];` |
| D22 | consistentStreak | B0 | 23 | `int consistentStreak[120];` |
| D23 | bestImprovement | B0 | 24 | `int bestImprovement = 0;` |
| D24 | bestDecline | B0 | 25 | `int bestDecline = 0;` |
| D25 | consistentPerformers | B0 | 26 | `int consistentPerformers = 0;` |
| D26 | irregularPerformers | B0 | 27 | `int irregularPerformers = 0;` |
| D27 | gradeDistribution | B0 | 28 | `int gradeDistribution[6];` |
| D28 | warningIssued | B0 | 29 | `int warningIssued[120];` |
| D29 | excellenceAward | B0 | 30 | `int excellenceAward[120];` |
| D30 | remedialPlan | B0 | 31 | `int remedialPlan[120];` |
| D31 | classAverage | B0 | 32 | `int classAverage[6];` |
| D32 | classVariance | B0 | 33 | `int classVariance[6];` |
| D33 | deviationAccumulator | B0 | 34 | `int deviationAccumulator = 0;` |
| D34 | subjectDeviation | B0 | 35 | `int subjectDeviation = 0;` |
| D35 | attendance | B0 | 36 | `int attendance[120];` |
| D36 | attendanceWarning | B0 | 37 | `int attendanceWarning = 0;` |
| D37 | extraCredits | B0 | 38 | `int extraCredits[120];` |
| D38 | projectScores | B0 | 39 | `int projectScores[120];` |
| D39 | participation | B0 | 40 | `int participation[120];` |
| D40 | subjectIndex | B0 | 42 | `subjectIndex = 0;` |
| D41 | assessmentIndex | B4 | 49 | `assessmentIndex = 0;` |
| D42 | assessmentIndex | B7 | 49 | `assessmentIndex++;` |
| D43 | subjectIndex | B3 | 42 | `subjectIndex++;` |
| D44 | studentIndex | B2 | 54 | `studentIndex = 0;` |
| D45 | studentIndex | B11 | 54 | `studentIndex++;` |
| D46 | studentIndex | B10 | 67 | `studentIndex = 0;` |
| D47 | subjectIndex | B16 | 68 | `subjectIndex = 0;` |
| D48 | totalScore | B20 | 69 | `totalScore = 0;` |
| D49 | totalWeightedScore | B20 | 70 | `totalWeightedScore = 0;` |
| D50 | assessmentIndex | B20 | 71 | `assessmentIndex = 0;` |
| D51 | totalScore | B24 | 73 | `totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| D52 | totalWeightedScore | B24 | 74 | `totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| D53 | assessmentIndex | B23 | 71 | `assessmentIndex++;` |
| D54 | passCount | B32 | 86 | `passCount += 1;` |
| D55 | distinctionCount | B34 | 89 | `distinctionCount += 1;` |
| D56 | failCount | B36 | 93 | `failCount += 1;` |
| D57 | bestImprovement | B43 | 108 | `bestImprovement = improvementStreak[studentIndex];` |
| D58 | bestDecline | B46 | 111 | `bestDecline = declineStreak[studentIndex];` |
| D59 | deviationAccumulator | B47 | 114 | `deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| D60 | subjectDeviation | B47 | 115 | `subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| D61 | subjectIndex | B19 | 68 | `subjectIndex++;` |
| D62 | attendanceWarning | B49 | 119 | `attendanceWarning += 1;` |
| D63 | consistentPerformers | B56 | 132 | `consistentPerformers += 1;` |
| D64 | irregularPerformers | B57 | 134 | `irregularPerformers += 1;` |
| D65 | auditFlag | B60 | 138 | `auditFlag += 1;` |
| D66 | studentIndex | B15 | 67 | `studentIndex++;` |
| D67 | subjectIndex | B14 | 142 | `subjectIndex = 0;` |
| D68 | subjectIndex | B64 | 142 | `subjectIndex++;` |
| D69 | subjectIndex | B63 | 146 | `subjectIndex = 0;` |
| D70 | varianceAccumulator | B69 | 147 | `int varianceAccumulator = 0;` |
| D71 | studentIndex | B69 | 148 | `studentIndex = 0;` |
| D72 | totalSubjectScore | B73 | 149 | `int totalSubjectScore = 0;` |
| D73 | assessmentIndex | B73 | 150 | `assessmentIndex = 0;` |
| D74 | totalSubjectScore | B77 | 151 | `totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| D75 | assessmentIndex | B76 | 150 | `assessmentIndex++;` |
| D76 | diff | B75 | 153 | `int diff = totalSubjectScore - classAverage[subjectIndex];` |
| D77 | varianceAccumulator | B75 | 154 | `varianceAccumulator += diff * diff;` |
| D78 | studentIndex | B72 | 148 | `studentIndex++;` |
| D79 | auditFlag | B83 | 163 | `auditFlag += 1;` |
| D80 | subjectIndex | B68 | 146 | `subjectIndex++;` |
| D81 | studentIndex | B67 | 167 | `studentIndex = 0;` |
| D82 | attendanceWarning | B90 | 169 | `attendanceWarning += 1;` |
| D83 | distinctionCount | B93 | 172 | `distinctionCount += 1;` |
| D84 | failCount | B94 | 174 | `failCount += 1;` |
| D85 | passCount | B95 | 176 | `passCount += 1;` |
| D86 | studentIndex | B87 | 167 | `studentIndex++;` |
| D87 | auditFlag | B105 | 197 | `auditFlag += 1;` |
| D88 | failCount | B108 | 201 | `failCount += auditFlag;` |
| D89 | passCount | B109 | 203 | `passCount += auditFlag;` |