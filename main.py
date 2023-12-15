from classroom import Classroom

duration = int(input("Enter a class duration in seconds (int): "))
class_name = input("Enter a class name: ")
subject = input("Enter a subject: ")

c = Classroom(class_name=class_name, class_duration=duration, subject=subject)
c.record_class()
c.create_class_notes()