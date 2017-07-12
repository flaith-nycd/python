# https://mingrammer.com/introduce-comprehension-of-python
subjects = ['math', 'history', 'english', 'computer engineering']
scores = [90, 80, 95, 100]
score_dict = {key: value for key, value in zip(subjects, scores)}
print(score_dict)

score_tuples = [('math', 90), ('history', 80), ('english', 95), ('computer engineering', 100)]
score_dict = {t[0]: t[1] for t in score_tuples}
print(score_dict)
