function gradingStudents(grades) {
    return grades.map(n => calcGrade(n))
}

function calcGrade(grade){
    if (grade < 38) return grade
    var remainder = grade % 5;
    if (remainder < 3) return grade
    return grade +5- remainder
}

const numbs = [73,67,38,33]
console.log(gradingStudents(numbs))