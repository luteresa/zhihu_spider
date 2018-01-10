import docx
file = docx.Document()

file.add_picture('t3.jpg',width=1000,height=1000)
file.save('t2.docx')