def q0(self):
        query = '''
            SELECT * FROM students
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

    def q1(self):
        query = '''
            SELECT g.sid, c.year, c.semester, COUNT(*)
            FROM Grades g 
            JOIN Courses c ON g.cid = c.cid
            WHERE g.grade > 0 
            GROUP BY g.sid, c.year, c.semester 
            ORDER BY g.sid, c.year, c.semester 
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

    def q2(self):
        query = '''
            SELECT s.firstName, s.lastName, c.year, c.semester, COUNT(*)
            FROM Students s 
            JOIN Grades g ON s.sid = g.sid 
            JOIN Courses c ON g.cid = c.cid 
            WHERE g.grade > 0
            GROUP BY s.sid, c.year, c.semester
            HAVING COUNT(*) >= 2
            ORDER BY s.firstName, s.lastName, c.year, c.semester 
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

    def q3(self):
        query = '''
            SELECT firstName, lastName, ms, number
            FROM allgrades 
            WHERE grade = 0 AND ms = mc 
            ORDER BY firstName, lastName, ms, number 
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

    def q4(self):
        query = '''
            SELECT s.firstName, s.lastName, m.major, c.number
            FROM Students s
            JOIN Majors m ON s.sid = m.sid 
            JOIN Grades g ON s.sid = g.sid 
            JOIN Courses c ON g.cid = c.cid 
            WHERE g.grade = 0 AND m.major = c.major 
            ORDER BY s.firstName, s.lastName, m.major, c.number 
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

    def q5(self):
        query = '''
            SELECT c.professor, COUNT(*) AS success 
            FROM Courses c 
            JOIN Grades g ON c.cid = g.cid 
            WHERE g.grade >= 2
            GROUP BY c.professor 
            ORDER BY success DESC, c.professor ASC 
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

    def q6(self):
        query = '''
            SELECT 
                c.number AS course_number, 
                GROUP_CONCAT(s.firstName || ' ' || s.lastName, ', ') AS student_names, 
                AVG(g.grade) AS avg_grade
            FROM Courses c 
            JOIN Grades g ON c.cid = g.cid 
            JOIN Students s ON g.sid = s.sid 
            WHERE g.grade >= 2
            GROUP BY course_number 
            HAVING avg_grade > 3
            ORDER BY avg_grade DESC, student_names ASC, course_number ASC 
        '''
        self.cur.execute(query)
        all_rows = self.cur.fetchall()
        return all_rows

if __name__ == "__main__":
    task = Task("database.db", 'students.csv', 'grades.csv', 'courses.csv', 'majors.csv')
    rows = task.q0()
    print(rows)
    print()
    rows = task.q1()
    print(rows)
    print()
    rows = task.q2()
    print(rows)
    print()
    rows = task.q3()
    print(rows)
    print()
    rows = task.q4()
    print(rows)
    print()
    rows = task.q5()
    print(rows)
    print()
    rows = task.q6()
    print(rows)
    print()
