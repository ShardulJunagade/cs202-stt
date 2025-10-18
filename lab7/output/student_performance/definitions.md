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
| D40 | totalScore | B9 | 69 | `totalScore = 0;` |
| D41 | totalWeightedScore | B9 | 70 | `totalWeightedScore = 0;` |
| D42 | totalScore | B11 | 73 | `totalScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| D43 | totalWeightedScore | B11 | 74 | `totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];` |
| D44 | passCount | B17 | 86 | `passCount += 1;` |
| D45 | distinctionCount | B19 | 89 | `distinctionCount += 1;` |
| D46 | failCount | B19 | 93 | `failCount += 1;` |
| D47 | bestImprovement | B23 | 108 | `bestImprovement = improvementStreak[studentIndex];` |
| D48 | bestDecline | B25 | 111 | `bestDecline = declineStreak[studentIndex];` |
| D49 | deviationAccumulator | B25 | 114 | `deviationAccumulator = totalScore - gradeThresholds[subjectIndex];` |
| D50 | subjectDeviation | B25 | 115 | `subjectDeviation += deviationAccumulator * deviationAccumulator;` |
| D51 | attendanceWarning | B27 | 119 | `attendanceWarning += 1;` |
| D52 | consistentPerformers | B31 | 132 | `consistentPerformers += 1;` |
| D53 | irregularPerformers | B31 | 134 | `irregularPerformers += 1;` |
| D54 | auditFlag | B33 | 138 | `auditFlag += 1;` |
| D55 | varianceAccumulator | B37 | 147 | `int varianceAccumulator = 0;` |
| D56 | totalSubjectScore | B39 | 149 | `int totalSubjectScore = 0;` |
| D57 | totalSubjectScore | B41 | 151 | `totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];` |
| D58 | diff | B41 | 153 | `int diff = totalSubjectScore - classAverage[subjectIndex];` |
| D59 | varianceAccumulator | B41 | 154 | `varianceAccumulator += diff * diff;` |
| D60 | auditFlag | B45 | 163 | `auditFlag += 1;` |
| D61 | attendanceWarning | B48 | 169 | `attendanceWarning += 1;` |
| D62 | distinctionCount | B50 | 172 | `distinctionCount += 1;` |
| D63 | failCount | B50 | 174 | `failCount += 1;` |
| D64 | passCount | B50 | 176 | `passCount += 1;` |
| D65 | auditFlag | B56 | 197 | `auditFlag += 1;` |
| D66 | failCount | B58 | 201 | `failCount += auditFlag;` |
| D67 | passCount | B58 | 203 | `passCount += auditFlag;` |