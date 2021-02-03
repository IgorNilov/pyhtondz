#import json

subj = {}
with open('text_6.txt', 'r', encoding="utf-8") as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = (lecture) + (practice) + (lab)
    print(f'Общее количество часов по предмету - \n {subj}')
