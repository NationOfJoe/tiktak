import random

class answer_type():
    def __init__(self, answer, log):
        self.answer = answer
        self.log = log

class numbers_game():
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target


    def solve(self):
        answers = []
        best_answer = answer_type(0, '')
        k = 0
        while best_answer.answer != self.target or k >40:
            k += 1
            for i in range(5000):
                random.shuffle(self.numbers)
                my_try, log = self.one_try(self.numbers)
                answers.append(answer_type(answer=my_try, log = log))
            best_answer = self.check_answers(answers)
        new_best_answer = self.log_corrector(best_answer)
        return new_best_answer

    def log_corrector(self, my_result):
        '''
        :param answer_type my_result: 
        :return: 
        '''
        new_log = my_result.log.replace('addition', '+').replace('reduction', '-').replace('multiply', '*').replace('division', '/')
        return answer_type(my_result.answer, new_log)

    def check_answers(self, answers):
        best_answer = None
        min_to_goal = self.target
        for ans in answers:
            if abs(self.target-ans.answer) < min_to_goal:
                min_to_goal = abs(self.target-ans.answer)
                best_answer = ans
        return best_answer

    def one_try(self, numbers):
        allowed_ops = [self.addition, self.reduction, self.multiply, self.division]
        my_try = 0
        log = ''
        for i,n in enumerate(numbers):
            action = random.choice(allowed_ops)
            if my_try == 0:
                my_try = n
                log = str (n)
            else:
                my_try = action(my_try, n)
                log += ' {0} {1}'.format(action.__name__ , str(n))
        return my_try, log


    def addition(self, numa, numb):
        return numa + numb

    def reduction(self,numa, numb):
        return numa - numb

    def multiply(self, numa, numb):
        return numa * numb

    def division(self,numa, numb):
        return numa / numb
