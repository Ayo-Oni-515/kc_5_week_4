# student class
class Student():
    """student class manages all student-related data"""
    In_memory: dict[str, dict] = {}

    def __init__(self,
                 name: str,
                 subjects: dict[str, float]):
        self.name = name
        self.subjects = subjects
        self.average = self.evaluate_average()
        self.grade = self.evaluate_grade()

        # json serializable representation
        self.json = {
            self.name: {
                "subjects": {**self.subjects},
                "average": self.average,
                "grade": self.grade
            }
        }

        # In memory storage
        self.In_memory.update(**self.json)
    
    def evaluate_average(self):
        """evaluates each student's average based on scores"""
        sum = 0
        for score in self.subjects.values():
            sum += score
        
        return (sum / (len(self.subjects)))

    def evaluate_grade(self):
        """Assigns a remark to the performance of each student based on
        avearge
        """
        if self.average < 50:
            return "Fail"
        elif self.average >= 50 and self.average <= 79:
            return "Pass"
        elif self.average >= 80:
            return "Excellent"
