class Grade:

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math


    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.sum() / 3

    def get_grade(self):
        score = int(self.avg())
        grade = ''
        if score >= 90:
            grade = 'A학점'
        elif score >= 80:
            grade = 'B학점'
        elif score >= 70:
            grade = 'C학점'
        elif score >= 60:
            grade = 'D학점'
        elif score >= 50:
            grade = 'E학점'
        else:
            grade = 'F학점'

        return grade


    @staticmethod
    def main():
        g = Grade(int(input('국어점수: ')), int(input('영어점수: ')), int(input('수학점수: ')))
        print(f'총점: {g.sum()}')
        print(f'평균: {g.avg()}')
        print(f'학점: {g.get_grade()}')

Grade.main()