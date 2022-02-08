export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
    if (typeof name !== 'string') throw Error('name must be a String');
    if (typeof length !== 'number') throw Error('length must be a Number');
    if (!Array.isArray(students)) throw Error('students must be an Array');
    for (const arr of students) {
      if (typeof arr !== 'string') throw Error('student must be a Sting');
    }
  }

  set name(name) {
    if (typeof name !== 'string') throw Error('name must be a String');
    this._name = name;
  }

  get name() {
    return this._name;
  }

  set length(length) {
    if (typeof length !== 'number') throw Error('length must be a Number');
    this._length = length;
  }

  get length() {
    return this._length;
  }

  set students(students) {
    if (!Array.isArray(students)) throw Error('students must be an Array');
    for (const arr of students) {
      if (typeof arr !== 'string') throw Error('student must be a Sting');
      this._students = students;
    }
  }

  get students() {
    return this._students;
  }
}
