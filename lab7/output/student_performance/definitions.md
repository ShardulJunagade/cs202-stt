| Definition ID | Variable | Block | Line | Statement |
|---------------|----------|-------|------|-----------|
| D1 | students | B0 | 2 | `int students = 120` |
| D2 | subjects | B0 | 3 | `int subjects = 6` |
| D3 | assessments | B0 | 4 | `int assessments = 5` |
| D4 | scores | B0 | 5 | `int scores[120][6][5]` |
| D5 | weights | B0 | 6 | `int weights[6][5]` |
| D6 | gradeThresholds | B0 | 7 | `int gradeThresholds[6]` |
| D7 | passCount | B0 | 8 | `int passCount = 0` |
| D8 | failCount | B0 | 9 | `int failCount = 0` |
| D9 | distinctionCount | B0 | 10 | `int distinctionCount = 0` |
| D10 | auditFlag | B0 | 11 | `int auditFlag = 0` |
| D11 | studentIndex | B0 | 12 | `int studentIndex = 0` |
| D12 | subjectIndex | B0 | 13 | `int subjectIndex = 0` |
| D13 | assessmentIndex | B0 | 14 | `int assessmentIndex = 0` |
| D14 | totalScore | B0 | 15 | `int totalScore = 0` |
| D15 | totalWeightedScore | B0 | 16 | `int totalWeightedScore = 0` |
| D16 | highestScore | B0 | 17 | `int highestScore = 0` |
| D17 | lowestScore | B0 | 18 | `int lowestScore = 0` |
| D18 | subjectTopper | B0 | 19 | `int subjectTopper[6]` |
| D19 | subjectLowest | B0 | 20 | `int subjectLowest[6]` |
| D20 | improvementStreak | B0 | 21 | `int improvementStreak[120]` |
| D21 | declineStreak | B0 | 22 | `int declineStreak[120]` |
| D22 | consistentStreak | B0 | 23 | `int consistentStreak[120]` |
| D23 | bestImprovement | B0 | 24 | `int bestImprovement = 0` |
| D24 | bestDecline | B0 | 25 | `int bestDecline = 0` |
| D25 | consistentPerformers | B0 | 26 | `int consistentPerformers = 0` |
| D26 | irregularPerformers | B0 | 27 | `int irregularPerformers = 0` |
| D27 | gradeDistribution | B0 | 28 | `int gradeDistribution[6]` |
| D28 | warningIssued | B0 | 29 | `int warningIssued[120]` |
| D29 | excellenceAward | B0 | 30 | `int excellenceAward[120]` |
| D30 | remedialPlan | B0 | 31 | `int remedialPlan[120]` |
| D31 | classAverage | B0 | 32 | `int classAverage[6]` |
| D32 | classVariance | B0 | 33 | `int classVariance[6]` |
| D33 | deviationAccumulator | B0 | 34 | `int deviationAccumulator = 0` |
| D34 | subjectDeviation | B0 | 35 | `int subjectDeviation = 0` |
| D35 | attendance | B0 | 36 | `int attendance[120]` |
| D36 | attendanceWarning | B0 | 37 | `int attendanceWarning = 0` |
| D37 | extraCredits | B0 | 38 | `int extraCredits[120]` |
| D38 | projectScores | B0 | 39 | `int projectScores[120]` |
| D39 | participation | B0 | 40 | `int participation[120]` |
| D40 | subjectIndex | B0 | 42 | `subjectIndex = 0` |
| D41 | gradeThresholds | B4 | 43 | `gradeThresholds[subjectIndex] = 200` |
| D42 | gradeDistribution | B4 | 44 | `gradeDistribution[subjectIndex] = 0` |
| D43 | subjectTopper | B4 | 45 | `subjectTopper[subjectIndex] = 0` |
| D44 | subjectLowest | B4 | 46 | `subjectLowest[subjectIndex] = 10000` |
| D45 | classAverage | B4 | 47 | `classAverage[subjectIndex] = 0` |
| D46 | classVariance | B4 | 48 | `classVariance[subjectIndex] = 0` |
| D47 | assessmentIndex | B4 | 49 | `assessmentIndex = 0` |
| D48 | weights | B8 | 50 | `weights[subjectIndex][assessmentIndex] = 20 + (assessmentIndex * 5)` |
| D49 | assessmentIndex | B7 | 49 | `assessmentIndex++` |
| D50 | subjectIndex | B3 | 42 | `subjectIndex++` |
| D51 | studentIndex | B2 | 54 | `studentIndex = 0` |
| D52 | improvementStreak | B12 | 55 | `improvementStreak[studentIndex] = 0` |
| D53 | declineStreak | B12 | 56 | `declineStreak[studentIndex] = 0` |
| D54 | consistentStreak | B12 | 57 | `consistentStreak[studentIndex] = 0` |
| D55 | warningIssued | B12 | 58 | `warningIssued[studentIndex] = 0` |
| D56 | excellenceAward | B12 | 59 | `excellenceAward[studentIndex] = 0` |
| D57 | remedialPlan | B12 | 60 | `remedialPlan[studentIndex] = 0` |
| D58 | attendance | B12 | 61 | `attendance[studentIndex] = 80 + (studentIndex % 20)` |
| D59 | extraCredits | B12 | 62 | `extraCredits[studentIndex] = studentIndex % 5` |
| D60 | projectScores | B12 | 63 | `projectScores[studentIndex] = 70 + (studentIndex % 30)` |
| D61 | participation | B12 | 64 | `participation[studentIndex] = 50 + (studentIndex % 40)` |
| D62 | studentIndex | B11 | 54 | `studentIndex++` |
| D63 | studentIndex | B10 | 67 | `studentIndex = 0` |
| D64 | subjectIndex | B16 | 68 | `subjectIndex = 0` |
| D65 | totalScore | B20 | 69 | `totalScore = 0` |
| D66 | totalWeightedScore | B20 | 70 | `totalWeightedScore = 0` |
| D67 | assessmentIndex | B20 | 71 | `assessmentIndex = 0` |
| D68 | scores | B24 | 72 | `scores[studentIndex][subjectIndex][assessmentIndex] = (((studentIndex * 7) + (subjectIndex * 9)) + (assessmentIndex * 11)) % 101` |
| D69 | totalScore | B24 | 73 | `totalScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| D70 | totalWeightedScore | B24 | 74 | `totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex]` |
| D71 | assessmentIndex | B23 | 71 | `assessmentIndex++` |
| D72 | subjectTopper | B26 | 78 | `subjectTopper[subjectIndex] = totalScore` |
| D73 | subjectLowest | B29 | 81 | `subjectLowest[subjectIndex] = totalScore` |
| D74 | classAverage | B30 | 84 | `classAverage[subjectIndex] += totalScore` |
| D75 | passCount | B32 | 86 | `passCount += 1` |
| D76 | gradeDistribution | B32 | 87 | `gradeDistribution[subjectIndex] += 1` |
| D77 | distinctionCount | B34 | 89 | `distinctionCount += 1` |
| D78 | excellenceAward | B34 | 90 | `excellenceAward[studentIndex] += 1` |
| D79 | failCount | B37 | 93 | `failCount += 1` |
| D80 | remedialPlan | B37 | 94 | `remedialPlan[studentIndex] += 1` |
| D81 | improvementStreak | B39 | 98 | `improvementStreak[studentIndex] += 1` |
| D82 | declineStreak | B39 | 99 | `declineStreak[studentIndex] = 0` |
| D83 | declineStreak | B43 | 101 | `declineStreak[studentIndex] += 1` |
| D84 | improvementStreak | B43 | 102 | `improvementStreak[studentIndex] = 0` |
| D85 | consistentStreak | B45 | 104 | `consistentStreak[studentIndex] += 1` |
| D86 | bestImprovement | B47 | 108 | `bestImprovement = improvementStreak[studentIndex]` |
| D87 | bestDecline | B50 | 111 | `bestDecline = declineStreak[studentIndex]` |
| D88 | deviationAccumulator | B51 | 114 | `deviationAccumulator = totalScore - gradeThresholds[subjectIndex]` |
| D89 | subjectDeviation | B51 | 115 | `subjectDeviation += deviationAccumulator * deviationAccumulator` |
| D90 | subjectIndex | B19 | 68 | `subjectIndex++` |
| D91 | attendanceWarning | B53 | 119 | `attendanceWarning += 1` |
| D92 | warningIssued | B53 | 120 | `warningIssued[studentIndex] += 1` |
| D93 | excellenceAward | B56 | 124 | `excellenceAward[studentIndex] += extraCredits[studentIndex]` |
| D94 | remedialPlan | B60 | 126 | `remedialPlan[studentIndex] += projectScores[studentIndex] / 10` |
| D95 | consistentStreak | B62 | 128 | `consistentStreak[studentIndex] += participation[studentIndex] / 10` |
| D96 | consistentPerformers | B64 | 132 | `consistentPerformers += 1` |
| D97 | irregularPerformers | B68 | 134 | `irregularPerformers += 1` |
| D98 | auditFlag | B71 | 138 | `auditFlag += 1` |
| D99 | studentIndex | B15 | 67 | `studentIndex++` |
| D100 | subjectIndex | B14 | 142 | `subjectIndex = 0` |
| D101 | classAverage | B76 | 143 | `classAverage[subjectIndex] = classAverage[subjectIndex] / students` |
| D102 | subjectIndex | B75 | 142 | `subjectIndex++` |
| D103 | subjectIndex | B74 | 146 | `subjectIndex = 0` |
| D104 | varianceAccumulator | B80 | 147 | `int varianceAccumulator = 0` |
| D105 | studentIndex | B80 | 148 | `studentIndex = 0` |
| D106 | totalSubjectScore | B84 | 149 | `int totalSubjectScore = 0` |
| D107 | assessmentIndex | B84 | 150 | `assessmentIndex = 0` |
| D108 | totalSubjectScore | B88 | 151 | `totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex]` |
| D109 | assessmentIndex | B87 | 150 | `assessmentIndex++` |
| D110 | diff | B86 | 153 | `int diff = totalSubjectScore - classAverage[subjectIndex]` |
| D111 | varianceAccumulator | B86 | 154 | `varianceAccumulator += diff * diff` |
| D112 | excellenceAward | B90 | 156 | `excellenceAward[studentIndex] += 1` |
| D113 | remedialPlan | B94 | 158 | `remedialPlan[studentIndex] += 1` |
| D114 | studentIndex | B83 | 148 | `studentIndex++` |
| D115 | classVariance | B82 | 161 | `classVariance[subjectIndex] = varianceAccumulator / students` |
| D116 | auditFlag | B97 | 163 | `auditFlag += 1` |
| D117 | subjectIndex | B79 | 146 | `subjectIndex++` |
| D118 | studentIndex | B78 | 167 | `studentIndex = 0` |
| D119 | attendanceWarning | B104 | 169 | `attendanceWarning += 1` |
| D120 | distinctionCount | B107 | 172 | `distinctionCount += 1` |
| D121 | failCount | B111 | 174 | `failCount += 1` |
| D122 | passCount | B113 | 176 | `passCount += 1` |
| D123 | studentIndex | B101 | 167 | `studentIndex++` |
| D124 | gradeDistribution | B115 | 181 | `gradeDistribution[0] += consistentPerformers` |
| D125 | gradeDistribution | B119 | 183 | `gradeDistribution[1] += irregularPerformers` |
| D126 | gradeDistribution | B121 | 185 | `gradeDistribution[2] += consistentPerformers` |
| D127 | gradeDistribution | B123 | 189 | `gradeDistribution[3] += bestImprovement` |
| D128 | gradeDistribution | B127 | 191 | `gradeDistribution[4] += bestDecline` |
| D129 | gradeDistribution | B129 | 193 | `gradeDistribution[5] += bestImprovement` |
| D130 | auditFlag | B131 | 197 | `auditFlag += 1` |
| D131 | failCount | B134 | 201 | `failCount += auditFlag` |
| D132 | passCount | B136 | 203 | `passCount += auditFlag` |