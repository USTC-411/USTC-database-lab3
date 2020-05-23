from .. import models

def getAuthority(operation, target, identity, target_id, identity_id):
  return True
  if target == 'Campus':
    if operation == 'add':
      return False
    elif operation == 'delete':
      return False
    elif operation == 'query':
      return True
    elif operation == 'modify':
      return False

  elif target == 'Major':
    if operation == 'add':
      return False
    elif operation == 'delete':
      return False
    elif operation == 'query':
      return True
    elif operation == 'modify':
      return False

  elif target == 'Class':
    if operation == 'add':
      return False
    elif operation == 'delete':
      return False
    elif operation == 'query':
      return True
    elif operation == 'modify':
      return False

  elif target == 'Teacher':
    return True
    if operation == 'add':
      return False
    elif operation == 'delete':
      return False
    elif operation == 'query':
      return True
    elif operation == 'modify':
      if identity == 'Teacher':
        if target_id == identity_id:
          return True
        else:
          return False
      elif identity == 'Student':
        return False

  elif target == 'Student':
    if operation == 'add':
      if identity == 'Teacher':
        student = models.Student.objects.get(student_id=target_id) # 找到对应的学生
        teacher = models.Teacher.objects.get(teacher_id=identity_id) # 找到对应老师
        teacher_students = teacher.HostClass.students # 找到该老师担任班主任的班级中的学生们
        if student in teacher_students:
          return True
        else:
          return False
      return False
    elif operation == 'delete':
      if identity == 'Teacher':
        student = models.Student.objects.get(student_id=target_id) # 找到对应的学生
        teacher = models.Teacher.objects.get(teacher_id=identity_id) # 找到对应老师
        teacher_students = teacher.HostClass.students # 找到该老师担任班主任的班级中的学生们
        if student in teacher_students:
          return True
        else:
          return False
      return False
    elif operation == 'query':
      if identity == 'Teacher':
        student = models.Student.objects.get(student_id=target_id) # 找到对应的学生
        teacher = models.Teacher.objects.get(teacher_id=identity_id) # 找到对应老师
        teacher_students = teacher.HostClass.students # 找到该老师担任班主任的班级中的学生们
        if student in teacher_students:
          return True
        else:
          return False
      elif identity == 'Student':
        if identity_id == target_id:
          return True
      return False
    elif operation == 'modify':
      if identity == 'Teacher':
        student = models.Student.objects.get(student_id=target_id) # 找到对应的学生
        teacher = models.Teacher.objects.get(teacher_id=identity_id) # 找到对应老师
        teacher_students = teacher.HostClass.students # 找到该老师担任班主任的班级中的学生们
        if student in teacher_students:
          return True
        else:
          return False
      return False

  elif target == 'MajorTransfer':
    return True
    if operation == 'add':
      if identity == 'Teacher':
        student = models.Student.objects.get(student_id=target_id) # 找到对应的学生
        teacher = models.Teacher.objects.get(teacher_id=identity_id) # 找到对应老师
        print(student, teacher)
        teacher_students = teacher.HostClass # 找到该老师担任班主任的班级中的学生们
        print(teacher_students)
        teacher_students = teacher_students.students # 找到该老师担任班主任的班级中的学生们
        if student in teacher_students:
          return True
        else:
          return False
      elif identity == 'Student':
        if identity_id == target_id:
          return True
      return False
    elif operation == 'delete':
      return False
    elif operation == 'query':
      if identity == 'Teacher':
        student = models.Student.objects.get(student_id=target_id) # 找到对应的学生
        teacher = models.Teacher.objects.get(teacher_id=identity_id) # 找到对应老师
        teacher_students = teacher.HostClass.students # 找到该老师担任班主任的班级中的学生们
        if student in teacher_students:
          return True
        else:
          return False
      elif identity == 'Student':
        if identity_id == target_id:
          return True
      return False
    elif operation == 'modify':
      return False

  elif target == 'GradeTransfer':
    if operation == 'add':
      if identity == 'Teacher':
        student = models.Student.objects.get(student_id=target_id) # 找到对应的学生
        teacher = models.Teacher.objects.get(teacher_id=identity_id) # 找到对应老师
        teacher_students = teacher.HostClass.students # 找到该老师担任班主任的班级中的学生们
        if student in teacher_students:
          return True
        else:
          return False
      elif identity == 'Student':
        if identity_id == target_id:
          return True
      return False
    elif operation == 'delete':
      return False
    elif operation == 'query':
      if identity == 'Teacher':
        student = models.Student.objects.get(student_id=target_id) # 找到对应的学生
        teacher = models.Teacher.objects.get(teacher_id=identity_id) # 找到对应老师
        teacher_students = teacher.HostClass.students # 找到该老师担任班主任的班级中的学生们
        if student in teacher_students:
          return True
        else:
          return False
      elif identity == 'Student':
        if identity_id == target_id:
          return True
      return False
    elif operation == 'modify':
      return False
    
  elif target == 'Lesson':
    if operation == 'add':
      if identity == 'Teacher':
        return True
      return False
    elif operation == 'delete':
      return False
    elif operation == 'query':
      return True
    elif operation == 'modify':
      return False

  elif target == 'ValidLesson':
    if operation == 'add':
      if identity == 'Teacher':
        teacher = models.Teacher.objects.get(teacher_id=identity_id)
        lesson = models.Lesson.objects.get(id=target_id)
        valid_lesson = teacher.ValidLesson
        if lesson in valid_lesson:
          return True
        else:
          return False
      return False
    elif operation == 'delete':
      if identity == 'Teacher':
        teacher = models.Teacher.objects.get(teacher_id=identity_id)
        lesson = models.Lesson.objects.get(id=target_id)
        valid_lesson = teacher.ValidLesson
        if lesson in valid_lesson:
          return True
        else:
          return False
      return False
    elif operation == 'query':
      if identity == 'Teacher':
        teacher = models.Teacher.objects.get(teacher_id=identity_id)
        lesson = models.Lesson.objects.get(id=target_id)
        valid_lesson = teacher.ValidLesson
        if lesson in valid_lesson:
          return True
        else:
          return False
      return False
    elif operation == 'modify':
      if identity == 'Teacher':
        teacher = models.Teacher.objects.get(teacher_id=identity_id)
        lesson = models.Lesson.objects.get(id=target_id)
        valid_lesson = teacher.ValidLesson
        if lesson in valid_lesson:
          return True
        else:
          return False
      return False

  elif target == 'LessonSelect':
    if operation == 'add':
      if identity == 'Teacher':
        student = models.Student.objects.get(student_id=target_id) # 找到对应的学生
        teacher = models.Teacher.objects.get(teacher_id=identity_id) # 找到对应老师
        teacher_students = teacher.HostClass.students # 找到该老师担任班主任的班级中的学生们
        if student in teacher_students:
          return True
        else:
          return False
      elif identity == 'Student':
        if identity_id == target_id:
          return True
        else:
          return False
    elif operation == 'delete':
      if identity == 'Teacher':
        student = models.Student.objects.get(student_id=target_id) # 找到对应的学生
        teacher = models.Teacher.objects.get(teacher_id=identity_id) # 找到对应老师
        teacher_students = teacher.HostClass.students # 找到该老师担任班主任的班级中的学生们
        if student in teacher_students:
          return True
        else:
          return False
      elif identity == 'Student':
        if identity_id == target_id:
          return True
        else:
          return False
    elif operation == 'query':
      if identity == 'Teacher':
        student = models.Student.objects.get(student_id=target_id) # 找到对应的学生
        teacher = models.Teacher.objects.get(teacher_id=identity_id) # 找到对应老师
        teacher_students = teacher.HostClass.students # 找到该老师担任班主任的班级中的学生们
        if student in teacher_students:
          return True
        else:
          return False
      elif identity == 'Student':
        if identity_id == target_id:
          return True
        else:
          return False
    elif operation == 'modify':
      if identity == 'Teacher':
        student = models.Student.objects.get(student_id=target_id) # 找到对应的学生
        teacher = models.Teacher.objects.get(teacher_id=identity_id) # 找到对应老师
        teacher_students = teacher.HostClass.students # 找到该老师担任班主任的班级中的学生们
        if student in teacher_students:
          return True
        else:
          return False
      elif identity == 'Student':
        if identity_id == target_id:
          return True
        else:
          return False
