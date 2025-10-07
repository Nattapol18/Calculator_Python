from tkinter import *
from tkinter.messagebox import showerror
import math

# Memory storage
memory = 0

def add_text(text, strvar: StringVar):
    current = strvar.get()
    if current == '0' and text.isdigit():
        strvar.set(text)
    elif '=' in current:
        strvar.set(text)
    else:
        strvar.set(f'{current}{text}')

def clear_text(strvar: StringVar):
    strvar.set('0')

def clear_entry(strvar: StringVar):
    strvar.set('0')

def delete_last(strvar: StringVar):
    current = strvar.get()
    if '=' in current:
        strvar.set('0')
    elif len(current) > 1:
        strvar.set(current[:-1])
    else:
        strvar.set('0')

def percentage(strvar: StringVar):
    try:
        current = strvar.get()
        if '=' in current:
            return
        result = eval(current) / 100
        strvar.set(str(result))
    except:
        pass

def reciprocal(strvar: StringVar):
    try:
        current = strvar.get()
        if '=' in current:
            current = current.split('=')[1].strip()
        result = 1 / eval(current)
        strvar.set(str(result))
    except:
        showerror('ข้อผิดพลาด', 'ไม่สามารถหารด้วย 0 ได้!')

def square(strvar: StringVar):
    try:
        current = strvar.get()
        if '=' in current:
            current = current.split('=')[1].strip()
        result = eval(current) ** 2
        strvar.set(str(result))
    except:
        pass

def square_root(strvar: StringVar):
    try:
        current = strvar.get()
        if '=' in current:
            current = current.split('=')[1].strip()
        result = math.sqrt(eval(current))
        strvar.set(str(result))
    except:
        showerror('ข้อผิดพลาด', 'ไม่สามารถหารากที่สองของจำนวนลบได้!')

def negate(strvar: StringVar):
    try:
        current = strvar.get()
        if '=' in current:
            current = current.split('=')[1].strip()
        result = -eval(current)
        strvar.set(str(result))
    except:
        pass

def memory_clear():
    global memory
    memory = 0

def memory_recall(strvar: StringVar):
    global memory
    strvar.set(str(memory))

def memory_add(strvar: StringVar):
    global memory
    try:
        current = strvar.get()
        if '=' in current:
            current = current.split('=')[1].strip()
        memory += eval(current)
    except:
        pass

def memory_subtract(strvar: StringVar):
    global memory
    try:
        current = strvar.get()
        if '=' in current:
            current = current.split('=')[1].strip()
        memory -= eval(current)
    except:
        pass

def memory_store(strvar: StringVar):
    global memory
    try:
        current = strvar.get()
        if '=' in current:
            current = current.split('=')[1].strip()
        memory = eval(current)
    except:
        pass

def submit(strvar: StringVar):
    operation = strvar.get()
    if not operation or operation == '0' or '=' in operation:
        return
    try:
        result = eval(operation)
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        strvar.set(str(result))
    except:
        showerror('ข้อผิดพลาด', 'กรุณาป้อนสมการที่ถูกต้อง!')
        strvar.set('0')

# สร้าง GUI
root = Tk()
root.title("Calculator")
root.geometry('410x650')
root.resizable(0, 0)
root.configure(background='#f3f3f3')

# StringVar
entry_strvar = StringVar(root, value='0')

# Header frame
header_frame = Frame(root, bg='#f3f3f3', height=80)
header_frame.pack(fill=X)

Label(header_frame, text='☰  Standard', font=('Segoe UI', 12), bg='#f3f3f3', fg='#000000').place(x=10, y=20)
Label(header_frame, text='⟲', font=('Segoe UI', 16), bg='#f3f3f3', fg='#000000').place(x=370, y=18)

# หน้าจอแสดงผล
display_frame = Frame(root, bg='#f3f3f3', bd=0, height=100)
display_frame.pack(fill=X, padx=0, pady=0)

display = Entry(
    display_frame,
    textvariable=entry_strvar,
    font=('Segoe UI', 48, 'bold'),
    bg='#f3f3f3',
    fg='#000000',
    bd=0,
    justify=RIGHT,
    state='disabled',
    disabledforeground='#000000',
    disabledbackground='#f3f3f3'
)
display.pack(expand=True, fill=BOTH, padx=20, pady=10)

# Separator line
separator = Frame(root, bg='#e5e5e5', height=1)
separator.pack(fill=X)

# ฟังก์ชันสร้างปุ่ม
def create_button(parent, text, row, col, bg_color, fg_color, command, font_size=16, colspan=1):
    btn = Button(
        parent,
        text=text,
        font=('Segoe UI', font_size),
        bg=bg_color,
        fg=fg_color,
        activebackground=bg_color,
        activeforeground=fg_color,
        bd=0,
        relief=FLAT,
        cursor='hand2',
        command=command
    )
    
    if colspan > 1:
        btn.grid(row=row, column=col, columnspan=colspan, sticky='nsew', padx=1, pady=1)
    else:
        btn.grid(row=row, column=col, sticky='nsew', padx=1, pady=1)
    
    # Hover effect
    def on_enter(e):
        if bg_color == '#f3f3f3':
            btn['background'] = '#e5e5e5'
        elif bg_color == '#0078d4':
            btn['background'] = '#005a9e'
    
    def on_leave(e):
        btn['background'] = bg_color
    
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    
    return btn

# Button frame
button_frame = Frame(root, bg='#f3f3f3')
button_frame.pack(expand=True, fill=BOTH, padx=2, pady=2)

# Configure grid
for i in range(7):
    button_frame.rowconfigure(i, weight=1, minsize=60)
for i in range(4):
    button_frame.columnconfigure(i, weight=1, minsize=100)

# สีที่ใช้
BG_LIGHT = '#f3f3f3'
BG_BLUE = '#0078d4'
FG_BLACK = '#000000'
FG_WHITE = '#ffffff'

# แถวที่ 1 - Memory
create_button(button_frame, 'MC', 0, 0, BG_LIGHT, FG_BLACK, memory_clear, 14)
create_button(button_frame, 'MR', 0, 1, BG_LIGHT, FG_BLACK, lambda: memory_recall(entry_strvar), 14)
create_button(button_frame, 'M+', 0, 2, BG_LIGHT, FG_BLACK, lambda: memory_add(entry_strvar), 14)
create_button(button_frame, 'M-', 0, 3, BG_LIGHT, FG_BLACK, lambda: memory_subtract(entry_strvar), 14)

# แถวที่ 2
create_button(button_frame, '%', 1, 0, BG_LIGHT, FG_BLACK, lambda: percentage(entry_strvar))
create_button(button_frame, 'CE', 1, 1, BG_LIGHT, FG_BLACK, lambda: clear_entry(entry_strvar))
create_button(button_frame, 'C', 1, 2, BG_LIGHT, FG_BLACK, lambda: clear_text(entry_strvar))
create_button(button_frame, '⌫', 1, 3, BG_LIGHT, FG_BLACK, lambda: delete_last(entry_strvar))

# แถวที่ 3
create_button(button_frame, '¹/x', 2, 0, BG_LIGHT, FG_BLACK, lambda: reciprocal(entry_strvar))
create_button(button_frame, 'x²', 2, 1, BG_LIGHT, FG_BLACK, lambda: square(entry_strvar))
create_button(button_frame, '²√x', 2, 2, BG_LIGHT, FG_BLACK, lambda: square_root(entry_strvar))
create_button(button_frame, '÷', 2, 3, BG_LIGHT, FG_BLACK, lambda: add_text('/', entry_strvar))

# แถวที่ 4
create_button(button_frame, '7', 3, 0, '#fafafa', FG_BLACK, lambda: add_text('7', entry_strvar), 18)
create_button(button_frame, '8', 3, 1, '#fafafa', FG_BLACK, lambda: add_text('8', entry_strvar), 18)
create_button(button_frame, '9', 3, 2, '#fafafa', FG_BLACK, lambda: add_text('9', entry_strvar), 18)
create_button(button_frame, '×', 3, 3, BG_LIGHT, FG_BLACK, lambda: add_text('*', entry_strvar))

# แถวที่ 5
create_button(button_frame, '4', 4, 0, '#fafafa', FG_BLACK, lambda: add_text('4', entry_strvar), 18)
create_button(button_frame, '5', 4, 1, '#fafafa', FG_BLACK, lambda: add_text('5', entry_strvar), 18)
create_button(button_frame, '6', 4, 2, '#fafafa', FG_BLACK, lambda: add_text('6', entry_strvar), 18)
create_button(button_frame, '−', 4, 3, BG_LIGHT, FG_BLACK, lambda: add_text('-', entry_strvar))

# แถวที่ 6
create_button(button_frame, '1', 5, 0, '#fafafa', FG_BLACK, lambda: add_text('1', entry_strvar), 18)
create_button(button_frame, '2', 5, 1, '#fafafa', FG_BLACK, lambda: add_text('2', entry_strvar), 18)
create_button(button_frame, '3', 5, 2, '#fafafa', FG_BLACK, lambda: add_text('3', entry_strvar), 18)
create_button(button_frame, '+', 5, 3, BG_LIGHT, FG_BLACK, lambda: add_text('+', entry_strvar))

# แถวที่ 7
create_button(button_frame, '±', 6, 0, '#fafafa', FG_BLACK, lambda: negate(entry_strvar), 18)
create_button(button_frame, '0', 6, 1, '#fafafa', FG_BLACK, lambda: add_text('0', entry_strvar), 18)
create_button(button_frame, '.', 6, 2, '#fafafa', FG_BLACK, lambda: add_text('.', entry_strvar), 18)
create_button(button_frame, '=', 6, 3, BG_BLUE, FG_WHITE, lambda: submit(entry_strvar))

# Keyboard bindings
def key_press(event):
    key = event.char
    if key.isdigit():
        add_text(key, entry_strvar)
    elif key in ['+', '-', '*', '/', '.']:
        add_text(key, entry_strvar)
    elif event.keysym == 'Return':
        submit(entry_strvar)
    elif event.keysym == 'BackSpace':
        delete_last(entry_strvar)
    elif event.keysym == 'Escape':
        clear_text(entry_strvar)
    elif event.keysym == 'Delete':
        clear_entry(entry_strvar)

root.bind('<Key>', key_press)

# เริ่มโปรแกรม
root.mainloop()