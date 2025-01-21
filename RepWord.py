my_text = "i love pakistan"
def replace_words():
   entery = input("enter word")
   new_word = input("enter new word")
   if entery in  my_text:
     print(my_text.replace(entery,new_word))

replace_words()