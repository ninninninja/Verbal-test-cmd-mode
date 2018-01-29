import csv
import random
import json

class read_file:
    default_path = r'C:\Users\sfaaz007\Desktop\大惟'
    default_file = r'\vocabulary.csv'
    
    def __init__(self, path=default_path+default_file):
        self.path = path
        
    def OpenFile(self):
        tmplist = []
        with open(self.path, 'r', encoding='utf8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                tmplist.append(row)
        
        return tmplist
    
    def CSVtoJson(self, input_list):
        
        for ind, row in enumerate(input_list):
            yield {
                    'id':ind,
                    'verbal':row[0],
                    'partofspeech':row[1],
                    'meaning':row[2],
                   }
        

class verbal_test:
    
    counts = 0
    
    def __init__(self, data_generator):
        self.data = data_generator
    
    def RandomTest(self):
        pass
    
    def OrderedTest(self):
        pass
    
    def ReviewMode(self, data):
        ctrl = True
        while ctrl:
            try:
                ele = next(data)
                self.counts += 1
                ans = ''
                while ans != ele['verbal']:
                    question = 'Q{0}: {1} {2} {3}\n'.format(self.counts,
                                ele['verbal'],
                                ele['partofspeech'],
                                ele['meaning'])
                    ans = input(question)
                    if ans == 'sToP':
                        ctrl = False
                        break
            except:
                ctrl = False
                
    
    def UserInterface(self):
        ModeSelect = input(
                'Select mode: \n' +
                '1) Random \n' +
                '2) Ordered \n' + 
                '3) Review \n' + 
                'Plz enter the corresponding number:')
        
        if ModeSelect == '1':
            pass
        elif ModeSelect == '2':
            pass
        elif ModeSelect == '3':
            self.ReviewMode(self.data)


class RecordClass:
    path = read_file.path
    def __init__(self, value):
        self.classname = 'Here is AttachClass'
        self.value = 0
        
    def RecordFile(self, path):
        absolute_path = path + r'\verbal_record.json'
        with open(absolute_path) as file:
            rec = json.load(file)
            if rec:
                pass
        
            new_rec = {
                        'Score':pass,
                        'Wrong':pass,
                        'Date':pass,
                        'Learned':pass,
                       }
        with open(absolute_path, 'w') as file:
            json.dump(new_rec, file)
    
    def __call__(self, func):
        def wrap():
            
            ans = func() + self.value
            return ans
        return wrap


if __name__=='__main__':
    x = read_file()
    res_list = x.OpenFile()
    res_json = x.CSVtoJson(res_list)
    y = verbal_test(res_json)
    y.UserInterface()