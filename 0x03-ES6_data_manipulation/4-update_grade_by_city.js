export default function updateStudentGradeByCity(arr, city, newGrades) {
  return arr
    .filter((newArr) => newArr.location === city)
    .map((student) => {
      const grades = newGrades.filter((val) => val.studentId === student.id);
      const grade = grades.length ? grades[0].grade : 'N/A';
      return { ...student, grade };
    });
}
