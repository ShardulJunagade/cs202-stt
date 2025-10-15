int main() {
    int students = 120;
    int subjects = 6;
    int assessments = 5;
    int scores[120][6][5];
    int weights[6][5];
    int gradeThresholds[6];
    int passCount = 0;
    int failCount = 0;
    int distinctionCount = 0;
    int auditFlag = 0;
    int studentIndex = 0;
    int subjectIndex = 0;
    int assessmentIndex = 0;
    int totalScore = 0;
    int totalWeightedScore = 0;
    int highestScore = 0;
    int lowestScore = 0;
    int subjectTopper[6];
    int subjectLowest[6];
    int improvementStreak[120];
    int declineStreak[120];
    int consistentStreak[120];
    int bestImprovement = 0;
    int bestDecline = 0;
    int consistentPerformers = 0;
    int irregularPerformers = 0;
    int gradeDistribution[6];
    int warningIssued[120];
    int excellenceAward[120];
    int remedialPlan[120];
    int classAverage[6];
    int classVariance[6];
    int deviationAccumulator = 0;
    int subjectDeviation = 0;
    int attendance[120];
    int attendanceWarning = 0;
    int extraCredits[120];
    int projectScores[120];
    int participation[120];

    for (subjectIndex = 0; subjectIndex < subjects; subjectIndex++) {
        gradeThresholds[subjectIndex] = 200;
        gradeDistribution[subjectIndex] = 0;
        subjectTopper[subjectIndex] = 0;
        subjectLowest[subjectIndex] = 10000;
        classAverage[subjectIndex] = 0;
        classVariance[subjectIndex] = 0;
        for (assessmentIndex = 0; assessmentIndex < assessments; assessmentIndex++) {
            weights[subjectIndex][assessmentIndex] = 20 + assessmentIndex * 5;
        }
    }

    for (studentIndex = 0; studentIndex < students; studentIndex++) {
        improvementStreak[studentIndex] = 0;
        declineStreak[studentIndex] = 0;
        consistentStreak[studentIndex] = 0;
        warningIssued[studentIndex] = 0;
        excellenceAward[studentIndex] = 0;
        remedialPlan[studentIndex] = 0;
        attendance[studentIndex] = 80 + (studentIndex % 20);
        extraCredits[studentIndex] = studentIndex % 5;
        projectScores[studentIndex] = 70 + (studentIndex % 30);
        participation[studentIndex] = 50 + (studentIndex % 40);
    }

    for (studentIndex = 0; studentIndex < students; studentIndex++) {
        for (subjectIndex = 0; subjectIndex < subjects; subjectIndex++) {
            totalScore = 0;
            totalWeightedScore = 0;
            for (assessmentIndex = 0; assessmentIndex < assessments; assessmentIndex++) {
                scores[studentIndex][subjectIndex][assessmentIndex] = (studentIndex * 7 + subjectIndex * 9 + assessmentIndex * 11) % 101;
                totalScore += scores[studentIndex][subjectIndex][assessmentIndex];
                totalWeightedScore += scores[studentIndex][subjectIndex][assessmentIndex] * weights[subjectIndex][assessmentIndex];
            }

            if (totalScore > subjectTopper[subjectIndex]) {
                subjectTopper[subjectIndex] = totalScore;
            }
            if (totalScore < subjectLowest[subjectIndex]) {
                subjectLowest[subjectIndex] = totalScore;
            }

            classAverage[subjectIndex] += totalScore;
            if (totalScore >= gradeThresholds[subjectIndex]) {
                passCount += 1;
                gradeDistribution[subjectIndex] += 1;
                if (totalScore >= gradeThresholds[subjectIndex] + 60) {
                    distinctionCount += 1;
                    excellenceAward[studentIndex] += 1;
                }
            } else {
                failCount += 1;
                remedialPlan[studentIndex] += 1;
            }

            if (totalScore >= subjectTopper[subjectIndex] - 5) {
                improvementStreak[studentIndex] += 1;
                declineStreak[studentIndex] = 0;
            } else if (totalScore <= subjectLowest[subjectIndex] + 5) {
                declineStreak[studentIndex] += 1;
                improvementStreak[studentIndex] = 0;
            } else {
                consistentStreak[studentIndex] += 1;
            }

            if (improvementStreak[studentIndex] > bestImprovement) {
                bestImprovement = improvementStreak[studentIndex];
            }
            if (declineStreak[studentIndex] > bestDecline) {
                bestDecline = declineStreak[studentIndex];
            }

            deviationAccumulator = totalScore - gradeThresholds[subjectIndex];
            subjectDeviation += deviationAccumulator * deviationAccumulator;
        }

        if (attendance[studentIndex] < 90) {
            attendanceWarning += 1;
            warningIssued[studentIndex] += 1;
        }

        if (improvementStreak[studentIndex] > declineStreak[studentIndex]) {
            excellenceAward[studentIndex] += extraCredits[studentIndex];
        } else if (improvementStreak[studentIndex] < declineStreak[studentIndex]) {
            remedialPlan[studentIndex] += projectScores[studentIndex] / 10;
        } else {
            consistentStreak[studentIndex] += participation[studentIndex] / 10;
        }

        if (improvementStreak[studentIndex] >= 3 && attendance[studentIndex] >= 95) {
            consistentPerformers += 1;
        } else if (declineStreak[studentIndex] >= 3 || attendance[studentIndex] < 85) {
            irregularPerformers += 1;
        }

        if (excellenceAward[studentIndex] > 5) {
            auditFlag += 1;
        }
    }

    for (subjectIndex = 0; subjectIndex < subjects; subjectIndex++) {
        classAverage[subjectIndex] = classAverage[subjectIndex] / students;
    }

    for (subjectIndex = 0; subjectIndex < subjects; subjectIndex++) {
        int varianceAccumulator = 0;
        for (studentIndex = 0; studentIndex < students; studentIndex++) {
            int totalSubjectScore = 0;
            for (assessmentIndex = 0; assessmentIndex < assessments; assessmentIndex++) {
                totalSubjectScore += scores[studentIndex][subjectIndex][assessmentIndex];
            }
            int diff = totalSubjectScore - classAverage[subjectIndex];
            varianceAccumulator += diff * diff;
            if (totalSubjectScore >= classAverage[subjectIndex] + 30) {
                excellenceAward[studentIndex] += 1;
            } else if (totalSubjectScore <= classAverage[subjectIndex] - 30) {
                remedialPlan[studentIndex] += 1;
            }
        }
        classVariance[subjectIndex] = varianceAccumulator / students;
        if (classVariance[subjectIndex] > subjectDeviation) {
            auditFlag += 1;
        }
    }

    for (studentIndex = 0; studentIndex < students; studentIndex++) {
        if (warningIssued[studentIndex] > 2) {
            attendanceWarning += 1;
        }
        if (excellenceAward[studentIndex] > remedialPlan[studentIndex]) {
            distinctionCount += 1;
        } else if (excellenceAward[studentIndex] < remedialPlan[studentIndex]) {
            failCount += 1;
        } else {
            passCount += 1;
        }
    }

    if (consistentPerformers > irregularPerformers) {
        gradeDistribution[0] += consistentPerformers;
    } else if (consistentPerformers < irregularPerformers) {
        gradeDistribution[1] += irregularPerformers;
    } else {
        gradeDistribution[2] += consistentPerformers;
    }

    if (bestImprovement > bestDecline) {
        gradeDistribution[3] += bestImprovement;
    } else if (bestImprovement < bestDecline) {
        gradeDistribution[4] += bestDecline;
    } else {
        gradeDistribution[5] += bestImprovement;
    }

    if (attendanceWarning > students / 4) {
        auditFlag += 1;
    }

    if (auditFlag > subjects) {
        failCount += auditFlag;
    } else {
        passCount += auditFlag;
    }

    return passCount + failCount + distinctionCount + auditFlag + consistentPerformers + irregularPerformers + attendanceWarning + gradeDistribution[0] + gradeDistribution[1] + gradeDistribution[2] + gradeDistribution[3] + gradeDistribution[4] + gradeDistribution[5];
}
