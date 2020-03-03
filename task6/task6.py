"""Module for menu and notebook modules exploration."""
import notebook

my_note = notebook.Note("Today was a good day.",
                        "life events, secrets, exploration")
print(f"An instance of Note class my_note with {my_note.memo} and {my_note.tags} attributes initialized.")

print('\n' + '#' * 12, "Attributes and Methods of my_note", "#" * 13)
print(my_note.__doc__)
print("my_diary object has next attributes and methods:", dir(my_note))
print("isinstance(class, my_note):", isinstance(my_note, object))
print("It belongs to", my_note.__class__, "class (obviously).")
print("It has next values of the attributes, in particular:", my_note.__dict__)
print("Here's one of them:", my_note.memo)

print('\n' + '#' * 12, "Demonstration of the methods of my_note", '#' * 13)
print("my_note.match('bad'):", my_note.match("bad"))
print("my_note.match('good'):", my_note.match("good"))

my_diary = notebook.Notebook()
print(f"An instance of Notebook class my_note with {my_note} attribute initialized.")

print('\n' + '#' * 12, "Attributes and Methods of my_diary", "#" * 13)
print(my_diary.__doc__)
print("my_diary object has next attributes and methods:", dir(my_diary))
print("isinstance(class, my_note):", isinstance(my_diary, object))
print("It belongs to", my_diary.__class__, "class (obviously).")
print("It has next values of the attributes, in particular:",
      my_diary.__dict__)
print("As you see, there are currently no notes.")

print('\n' + '#' * 12, "Demonstration of the methods of my_diary", '#' * 13)
my_diary.new_note(my_note)
print("New note (my_note) added.")
bad_note = notebook.Note("Today, unfortunately, was a bad day.")
my_diary.new_note(bad_note)
print("And another one.")
print("That's all!")
