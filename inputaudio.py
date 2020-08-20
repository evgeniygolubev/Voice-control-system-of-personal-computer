import speech_recognition as sr
from tkinter import *
import tkinter
from tkinter import scrolledtext
from tkinter.filedialog import askdirectory
import pickle


def add_id():

    with open('indexaudio.pickle', 'wb') as f:
        index_microphone = id1
        pickle.dump(index_microphone, f)  # помещаем объект в файл



root_allaudio = Tk()
root_allaudio.geometry('500x500')
root_allaudio.configure(bg='gray22')
root_allaudio.title('Все аудиоустройства')
idd = IntVar()
id = Entry(root_allaudio, textvariable=idd)
id.place(x=400, y=475, height=25, width=100)
id.configure(font=('Castellar', 12))
id1 = id.get()

st = scrolledtext.ScrolledText(root_allaudio)
st.configure(font=('Castellar', 12))
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    audio = ("Имя \"{1}\" (Индекс={0})`\n".format(index, name))
    st.insert(INSERT, '{0}\n'.format(audio)
              )
st.configure(bg='white')
st.place(x=0, y=0, height=475, width=500)

but1_entry = Button(root_allaudio, text='Добавить id микрофона', command=add_id)
but1_entry.configure(bd=1, font=('Castellar', 12), bg='white')
but1_entry.place(x=0, y=475, height=25, width=400)
root_allaudio.mainloop()

