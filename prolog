% courses in departmentdept_course(comp_dept,dsa).

dept_course(comp_dept,ppl).
dept_course(comp_dept,dsa).
dept_course(comp_dept,dsgt).
dept_course(math_dept,dld).
dept_course(math_dept,la).
dept_course(math_dept,ode).
dept_course(math_dept,mvc).


% departments having students

dept_student(comp_dept,snb).
dept_student(math_dept,snb).
dept_student(comp_dept,sag).
dept_student(math_dept,sag).
dept_student(comp_dept,opb).
dept_student(math_dept,opb).
dept_student(comp_dept,msd).
dept_student(math_dept,msd).


% faculty teaches these courses

faculty_course(vkk,ppl).
faculty_course(asm,dsa).
faculty_course(rys,dsgt).
faculty_course(jrw,dld).
faculty_course(dng,la).
faculty_course(jtm,ode).
faculty_course(jtm,mvc).


% faculties in department
dept_faculty(D,F):-dept_course(Z,C),faculty_course(D,S).


% courses taken by students
student_course(S,C):-dept_student(Z,S),dept_course(Z,C).


% faculty teaches these students
faculty_student(F,S):-dept_student(Z,S),dept_course(Z,C),faculty_course(F,C).
