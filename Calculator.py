from tkinter import *
from tkinter.messagebox import showerror

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

def delete_last(strvar: StringVar):
    current = strvar.get()
    if '=' in current:
        strvar.set('0')
    elif len(current) > 1:
        strvar.set(current[:-1])
    else:
        strvar.set('0')

def submit(strvar: StringVar):
    operation = strvar.get()
    if not operation or operation == '0' or '=' in operation:
        return
    try:
        result = eval(operation)
        # Format result to remove unnecessary decimals
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        strvar.set(f"{operation} = {result}")
    except:
        showerror('ข้อผิดพลาด', 'กรุณาป้อนสมการที่ถูกต้อง!')
        strvar.set('0')

# สร้าง GUI
root = Tk()
root.title("Calculator")
root.geometry('340x520')
root.resizable(0, 0)
root.configure(background='#f5f5f5')

# StringVar
entry_strvar = StringVar(root, value='0')

# หน้าจอแสดงผล
display_frame = Frame(root, bg='#2c3e50', bd=0)
display_frame.place(x=20, y=20, width=300, height=100)

display = Entry(
    display_frame,
    textvariable=entry_strvar,
    font=('Segoe UI', 24, 'bold'),
    bg='#2c3e50',
    fg='#ecf0f1',
    bd=0,
    justify=RIGHT,
    state='disabled',
    disabledforeground='#ecf0f1',
    disabledbackground='#2c3e50'
)
display.pack(expand=True, fill=BOTH, padx=15, pady=15)

# ฟังก์ชันสร้างปุ่ม
def create_button(parent, text, x, y, width, height, bg_color, fg_color, command):
    btn = Button(
        parent,
        text=text,
        font=('Segoe UI', 16, 'bold'),
        bg=bg_color,
        fg=fg_color,
        activebackground=bg_color,
        activeforeground=fg_color,
        bd=0,
        cursor='hand2',
        command=command
    )
    btn.place(x=x, y=y, width=width, height=height)
    
    # Hover effect
    def on_enter(e):
        btn['background'] = _adjust_color(bg_color, -20)
    
    def on_leave(e):
        btn['background'] = bg_color
    
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    
    return btn

def _adjust_color(color, amount):
    """ปรับความสว่างของสี"""
    color = color.lstrip('#')
    if len(color) == 6:
        r, g, b = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)
        r = max(0, min(255, r + amount))
        g = max(0, min(255, g + amount))
        b = max(0, min(255, b + amount))
        return f'#{r:02x}{g:02x}{b:02x}'
    return color

# สีที่ใช้
COLOR_NUM = '#ecf0f1'      # สีปุ่มตัวเลข - เทาอ่อน
COLOR_OP = '#3498db'       # สีปุ่มโอเปอเรเตอร์ - น้ำเงิน
COLOR_FUNC = '#95a5a6'     # สีปุ่มฟังก์ชัน - เทา
COLOR_CLEAR = '#e74c3c'    # สีปุ่มลบ - แดง
COLOR_EQUAL = '#27ae60'    # สีปุ่มเท่ากับ - เขียว
COLOR_TEXT = '#2c3e50'     # สีตัวอักษร - เทาเข้ม
COLOR_TEXT_WHITE = '#ffffff'  # สีตัวอักษรขาว

# กำหนดตำแหน่งปุ่ม
start_y = 140
btn_width = 65
btn_height = 60
gap = 10

# แถวที่ 1 - ฟังก์ชัน
create_button(root, 'C', 20, start_y, btn_width, btn_height, COLOR_CLEAR, COLOR_TEXT_WHITE, lambda: clear_text(entry_strvar))
create_button(root, '(', 95, start_y, btn_width, btn_height, COLOR_FUNC, COLOR_TEXT, lambda: add_text('(', entry_strvar))
create_button(root, ')', 170, start_y, btn_width, btn_height, COLOR_FUNC, COLOR_TEXT, lambda: add_text(')', entry_strvar))
create_button(root, '⌫', 245, start_y, btn_width, btn_height, COLOR_FUNC, COLOR_TEXT, lambda: delete_last(entry_strvar))

# แถวที่ 2
y = start_y + btn_height + gap
create_button(root, '7', 20, y, btn_width, btn_height, COLOR_NUM, COLOR_TEXT, lambda: add_text('7', entry_strvar))
create_button(root, '8', 95, y, btn_width, btn_height, COLOR_NUM, COLOR_TEXT, lambda: add_text('8', entry_strvar))
create_button(root, '9', 170, y, btn_width, btn_height, COLOR_NUM, COLOR_TEXT, lambda: add_text('9', entry_strvar))
create_button(root, '÷', 245, y, btn_width, btn_height, COLOR_OP, COLOR_TEXT_WHITE, lambda: add_text('/', entry_strvar))

# แถวที่ 3
y = start_y + (btn_height + gap) * 2
create_button(root, '4', 20, y, btn_width, btn_height, COLOR_NUM, COLOR_TEXT, lambda: add_text('4', entry_strvar))
create_button(root, '5', 95, y, btn_width, btn_height, COLOR_NUM, COLOR_TEXT, lambda: add_text('5', entry_strvar))
create_button(root, '6', 170, y, btn_width, btn_height, COLOR_NUM, COLOR_TEXT, lambda: add_text('6', entry_strvar))
create_button(root, '×', 245, y, btn_width, btn_height, COLOR_OP, COLOR_TEXT_WHITE, lambda: add_text('*', entry_strvar))

# แถวที่ 4
y = start_y + (btn_height + gap) * 3
create_button(root, '1', 20, y, btn_width, btn_height, COLOR_NUM, COLOR_TEXT, lambda: add_text('1', entry_strvar))
create_button(root, '2', 95, y, btn_width, btn_height, COLOR_NUM, COLOR_TEXT, lambda: add_text('2', entry_strvar))
create_button(root, '3', 170, y, btn_width, btn_height, COLOR_NUM, COLOR_TEXT, lambda: add_text('3', entry_strvar))
create_button(root, '−', 245, y, btn_width, btn_height, COLOR_OP, COLOR_TEXT_WHITE, lambda: add_text('-', entry_strvar))

# แถวที่ 5
y = start_y + (btn_height + gap) * 4
create_button(root, '0', 20, y, btn_width, btn_height, COLOR_NUM, COLOR_TEXT, lambda: add_text('0', entry_strvar))
create_button(root, '.', 95, y, btn_width, btn_height, COLOR_NUM, COLOR_TEXT, lambda: add_text('.', entry_strvar))
create_button(root, '^', 170, y, btn_width, btn_height, COLOR_OP, COLOR_TEXT_WHITE, lambda: add_text('**', entry_strvar))
create_button(root, '+', 245, y, btn_width, btn_height, COLOR_OP, COLOR_TEXT_WHITE, lambda: add_text('+', entry_strvar))

# ปุ่มเท่ากับ (ใหญ่กว่า)
y = start_y + (btn_height + gap) * 5
create_button(root, '=', 20, y, 290, btn_height, COLOR_EQUAL, COLOR_TEXT_WHITE, lambda: submit(entry_strvar))

# Keyboard bindings
def key_press(event):
    key = event.char
    if key.isdigit():
        add_text(key, entry_strvar)
    elif key in ['+', '-', '*', '/', '.', '(', ')']:
        add_text(key, entry_strvar)
    elif key == '^':
        add_text('**', entry_strvar)
    elif event.keysym == 'Return':
        submit(entry_strvar)
    elif event.keysym == 'BackSpace':
        delete_last(entry_strvar)
    elif event.keysym == 'Escape':
        clear_text(entry_strvar)

root.bind('<Key>', key_press)

# เริ่มโปรแกรม
root.mainloop()