

def parse_text(text):
    new_text = text.replace("\n", "")
    question = new_text.split("Question")[1:]
    list_questions = [elt.split("1/")[0] for elt in question]
    list_answers = ["1/" + elt.split("1/")[1] for elt in question]
    return list_questions, list_answers

def parse_answers(list_answers):
    new_list = [answers.split("/") for answers in list_answers]
    final = [[answers[1][:-1], answers[2][:-1], answers[3][:-1], answers[4][:-1], answers[5]] for answers in new_list]
    return final

def parse_questions(list_questions):
    i = 0
    new_list = []
    for question in list_questions:
        new_question = question.strip()
        while new_question[i].isdigit():
            i += 1
        new_list.append(new_question[i:])
        i = 0
    return new_list

def parse_solution(text):
    new_text = text.replace("\n", "")
    solution = new_text.split("Question")[1:]
    for i, elt in enumerate(solution):
        tmp = elt.strip()
        if tmp[0] == '0':
            solution[i] = tmp[1:].replace(" ", "")
        else:
            solution[i] = tmp.replace(" ", "")
    return solution

def text_to_js(questions, answers, solution):
    for index_question, question in enumerate(questions):
        print("{")
        index_question2, index_solution = solution[index_question].split(":")
        print(f"\'{question}\':[")
        if index_solution != 1:
            answers[index_question][0], answers[index_question][int(index_solution) - 1] =  answers[index_question][int(index_solution) - 1], answers[index_question][0]
            for answer in answers[index_question]:
                print(f"\'{answer}\',")
        print("],")
        print("},")




with open('iae.txt', 'r') as f:
    with open('answer.txt', 'r') as f2:
        list_questions, list_answers = parse_text(f.read())
        questions = parse_questions(list_questions)
        answers = parse_answers(list_answers)
        solution = parse_solution(f2.read())

        text_to_js(questions, answers, solution)
