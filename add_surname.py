#Title: Project-6b

def add_surname(first_name):
   last_name = [name+' Kardashian' for name in first_name if name[0]=='K']
   return last_name

first_name = ["Kiki", "Krystal", "Pavel", "Annie", "Koala"]

#print(add_surname(first_name))