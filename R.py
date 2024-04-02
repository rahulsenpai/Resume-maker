import tkinter
import jinja2
import pdfkit
from datetime import datetime


window = tkinter.Tk()
window.title("Project")
window.geometry('450x450')
window.configure(bg='#232627')
frame = tkinter.Frame(bg="#232627")


#render options in html file
def render():
    context = {
        "name": name_entry.get(),
        "bio": bio_entry.get(),
        "contactno": othername_entry.get(),
        "email": othernamepoint_entry.get(),
        "th": edu12th_entry.get(),
        "the": edu10th_entry.get(),
        "ts1s": ts1s_entry.get(),
        "ts2s": ts2s_entry.get(),
        "cs1s": cs1s_entry.get(),
        "cs2s": cs2s_entry.get()
    }
    
    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    html_template = 'name.html'
    template = template_env.get_template(html_template)
    output_text = template.render(context)

    pdfkit.from_string(output_text, "resume.pdf", css='name.css')


#first 2 entry
heading_label = tkinter.Label(frame, text="Welcome", bg="#232627", fg="white", font=("arial", 30))
name_label = tkinter.Label(frame, text="Your name", bg="#232627", fg="white", font=("arial", 20))
name_entry = tkinter.Entry(frame, font=("arial", 15))
bio_label = tkinter.Label(frame, text="Enter your bio", bg="#232627", fg="white", font=("arial", 20))
bio_entry = tkinter.Entry(frame, font=("arial", 15))

#to enter content information
headingother_label = tkinter.Label(frame, text="Enter Your contact information", bg="#232627", fg="white", font=("arial", 30))
othername_label = tkinter.Label(frame, text="Mobile No", bg="#232627", fg="white", font=("arial", 20))
othername_entry = tkinter.Entry(frame, font=("arial", 15))
othernamepoint_label = tkinter.Label(frame, text="Email", bg="#232627", fg="white", font=("arial", 20))
othernamepoint_entry = tkinter.Entry(frame, font=("arial", 15))

#for entering education detail
educationheading_label = tkinter.Label(frame, text="Enter Your education background", bg="#232627", fg="white", font=("arial", 30))
edu12th_label = tkinter.Label(frame, text="12th class details", bg="#232627", fg="white", font=("arial", 20))
edu12th_entry = tkinter.Entry(frame, font=("arial", 15))
edu10th_label = tkinter.Label(frame, text="10th class details", bg="#232627", fg="white", font=("arial", 20))
edu10th_entry = tkinter.Entry(frame, font=("arial", 15))

#for entering technical skills detail
ts_label = tkinter.Label(frame, text="Enter Your technical skills", bg="#232627", fg="white", font=("arial", 30))
ts1s_label = tkinter.Label(frame, text="----->", bg="#232627", fg="white", font=("arial", 20))
ts1s_entry = tkinter.Entry(frame, font=("arial", 15))
ts2s_label = tkinter.Label(frame, text="---->", bg="#232627", fg="white", font=("arial", 20))
ts2s_entry = tkinter.Entry(frame, font=("arial", 15))

#for entering hobbies detail
cs_label = tkinter.Label(frame, text="Enter Your communication skills", bg="#232627", fg="white", font=("arial", 30))
cs1s_label = tkinter.Label(frame, text="----->", bg="#232627", fg="white", font=("arial", 20))
cs1s_entry = tkinter.Entry(frame, font=("arial", 15))
cs2s_label = tkinter.Label(frame, text="---->", bg="#232627", fg="white", font=("arial", 20))
cs2s_entry = tkinter.Entry(frame, font=("arial", 15))

#this is submit button
submit1_button = tkinter.Button(frame, text="Submit", bg="#232627", fg="white", font=("arial", 20),command=render)

#position of first 2 entry
heading_label.grid(row=0 , column=0, columnspan=2, sticky="news")
name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=12,)
bio_label.grid(row=2, column=0)
bio_entry.grid(row=2, column=12,)

#position of content information entry
headingother_label.grid(row=4 , column=0, columnspan=4, sticky="news")
othername_label.grid(row=5, column=0)
othername_entry.grid(row=5, column=12)
othernamepoint_label.grid(row=6, column=0)
othernamepoint_entry.grid(row=6, column=12)

#position of education details entry
educationheading_label.grid(row=7 , column=0, columnspan=4, sticky="news")
edu12th_label.grid(row=8, column=0)
edu12th_entry.grid(row=8, column=12)
edu10th_label.grid(row=9, column=0)
edu10th_entry.grid(row=9, column=12)

#position of technical skills entry
ts_label.grid(row=10 , column=0, columnspan=4, sticky="news")
ts1s_label.grid(row=11, column=0)
ts1s_entry.grid(row=11, column=12)
ts2s_label.grid(row=12, column=0)
ts2s_entry.grid(row=12, column=12)

#position of hobbies entry
cs_label.grid(row=13 , column=0, columnspan=4, sticky="news")
cs1s_label.grid(row=14, column=0)
cs1s_entry.grid(row=14, column=12)
cs2s_label.grid(row=15, column=0)
cs2s_entry.grid(row=15, column=12)



submit1_button.grid(row=16, column=0, columnspan=2,pady=30)

frame.pack() 
window.mainloop()