from tkinter import *
from tkinter import ttk
from datetime import datetime
from threading import *
from PIL import ImageTk, Image
from win32api import GetSystemMetrics
import socket, os, pytz, time

root = Tk()

root.title("Fusion Calculator")
root.geometry("700x400")
root.resizable(0, 0)
root.iconbitmap("resources/calculator.ico")

left_pane = Frame(root)
left_pane.pack(side=LEFT, expand=True, fill=BOTH)

hostname = socket.gethostname()
username = str(os.environ.get('USERNAME'))
ipaddress = socket.gethostbyname(hostname)

computer_name = Label(left_pane, text='Computer Name: ' + hostname, anchor=W)
computer_name.pack(fill=BOTH)
user_name = Label(left_pane, text='User Name: ' + username, anchor=W)
user_name.pack(fill=BOTH)
ip_address = Label(left_pane, text='IP Address: ' + ipaddress, anchor=W)
ip_address.pack(fill=BOTH)

left_pane_seperator_1 = ttk.Separator(left_pane, orient=HORIZONTAL)
left_pane_seperator_1.pack(fill=X)

date_and_time_now_entry = Label(left_pane, text='', font=("Arial", 10, "bold"))
date_and_time_now_entry.pack(pady=10)

sri_lankan_time = pytz.timezone("Asia/Colombo")


def update_time():
	date_and_time_now = datetime.now(sri_lankan_time)
	date_and_time_string = date_and_time_now.strftime("%m/%d/%Y %H:%M:%S")
	date_and_time_now_entry.config(text=date_and_time_string)
	date_and_time_now_entry.after(1000, update_time)


update_time()

scheduler_frame = LabelFrame(left_pane, text='Scheduler')
scheduler_frame.pack(fill=X, pady=10)

scheduler_top_frame = Frame(scheduler_frame)
scheduler_top_frame.pack(fill=X)

hours_label = Label(scheduler_top_frame, text="HH")
hours_label.grid(row=0, column=1, padx=10)

minutes_label = Label(scheduler_top_frame, text="MM")
minutes_label.grid(row=0, column=2, padx=10)

seconds_label = Label(scheduler_top_frame, text="SS")
seconds_label.grid(row=0, column=3, padx=10)

first_break_label = Label(scheduler_top_frame, text="1st Break:")
first_break_label.grid(row=1, column=0, pady=5)

second_break_label = Label(scheduler_top_frame, text="2nd Break:")
second_break_label.grid(row=2, column=0, pady=5)

meal_break_label = Label(scheduler_top_frame, text="Meal Break:")
meal_break_label.grid(row=3, column=0, pady=5)

logout_label = Label(scheduler_top_frame, text="Logout:")
logout_label.grid(row=4, column=0, pady=5)

hour_time_values = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
                    '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                    '20', '21', '22', '23')

other_time_values = ('00', '01', '02', '03', '04', '05', '06', '07', '08',
                     '09', '10', '11', '12', '13', '14', '15', '16', '17',
                     '18', '19', '20', '21', '22', '23', '24', '25', '26',
                     '27', '28', '29', '30', '31', '32', '33', '34', '35',
                     '36', '37', '38', '39', '40', '41', '42', '43', '44',
                     '45', '46', '47', '48', '49', '50', '51', '52', '53',
                     '54', '55', '56', '57', '58', '59')

first_break_hour_value = StringVar()
first_break_hour_drop = ttk.Combobox(scheduler_top_frame,
                                     width=2,
                                     textvariable=first_break_hour_value)
first_break_hour_drop['values'] = hour_time_values
first_break_hour_drop.grid(row=1, column=1)
first_break_hour_drop.current(0)
first_break_hour_drop.config(state='readonly')

first_break_minute_value = StringVar()
first_break_minute_drop = ttk.Combobox(scheduler_top_frame,
                                       width=2,
                                       textvariable=first_break_minute_value)
first_break_minute_drop['values'] = other_time_values
first_break_minute_drop.grid(row=1, column=2)
first_break_minute_drop.current(0)
first_break_minute_drop.config(state='readonly')

first_break_second_value = StringVar()
first_break_second_drop = ttk.Combobox(scheduler_top_frame,
                                       width=2,
                                       textvariable=first_break_second_value)
first_break_second_drop['values'] = other_time_values
first_break_second_drop.grid(row=1, column=3)
first_break_second_drop.current(0)
first_break_second_drop.config(state='readonly')

second_break_hour_value = StringVar()
second_break_hour_drop = ttk.Combobox(scheduler_top_frame,
                                      width=2,
                                      textvariable=second_break_hour_value)
second_break_hour_drop['values'] = hour_time_values
second_break_hour_drop.grid(row=2, column=1)
second_break_hour_drop.current(0)
second_break_hour_drop.config(state='readonly')

second_break_minute_value = StringVar()
second_break_minute_drop = ttk.Combobox(scheduler_top_frame,
                                        width=2,
                                        textvariable=second_break_minute_value)
second_break_minute_drop['values'] = other_time_values
second_break_minute_drop.grid(row=2, column=2)
second_break_minute_drop.current(0)
second_break_minute_drop.config(state='readonly')

second_break_second_value = StringVar()
second_break_second_drop = ttk.Combobox(scheduler_top_frame,
                                        width=2,
                                        textvariable=second_break_second_value)
second_break_second_drop['values'] = other_time_values
second_break_second_drop.grid(row=2, column=3)
second_break_second_drop.current(0)
second_break_second_drop.config(state='readonly')

meal_break_hour_value = StringVar()
meal_break_hour_drop = ttk.Combobox(scheduler_top_frame,
                                    width=2,
                                    textvariable=meal_break_hour_value)
meal_break_hour_drop['values'] = hour_time_values
meal_break_hour_drop.grid(row=3, column=1)
meal_break_hour_drop.current(0)
meal_break_hour_drop.config(state='readonly')

meal_break_minute_value = StringVar()
meal_break_minute_drop = ttk.Combobox(scheduler_top_frame,
                                      width=2,
                                      textvariable=meal_break_minute_value)
meal_break_minute_drop['values'] = other_time_values
meal_break_minute_drop.grid(row=3, column=2)
meal_break_minute_drop.current(0)
meal_break_minute_drop.config(state='readonly')

meal_break_second_value = StringVar()
meal_break_second_drop = ttk.Combobox(scheduler_top_frame,
                                      width=2,
                                      textvariable=meal_break_second_value)
meal_break_second_drop['values'] = other_time_values
meal_break_second_drop.grid(row=3, column=3)
meal_break_second_drop.current(0)
meal_break_second_drop.config(state='readonly')

logout_hour_value = StringVar()
logout_hour_drop = ttk.Combobox(scheduler_top_frame,
                                width=2,
                                textvariable=logout_hour_value)
logout_hour_drop['values'] = hour_time_values
logout_hour_drop.grid(row=4, column=1)
logout_hour_drop.current(0)
logout_hour_drop.config(state='readonly')

logout_minute_value = StringVar()
logout_minute_drop = ttk.Combobox(scheduler_top_frame,
                                  width=2,
                                  textvariable=logout_minute_value)
logout_minute_drop['values'] = other_time_values
logout_minute_drop.grid(row=4, column=2)
logout_minute_drop.current(0)
logout_minute_drop.config(state='readonly')

logout_second_value = StringVar()
logout_second_drop = ttk.Combobox(scheduler_top_frame,
                                  width=2,
                                  textvariable=logout_second_value)
logout_second_drop['values'] = other_time_values
logout_second_drop.grid(row=4, column=3)
logout_second_drop.current(0)
logout_second_drop.config(state='readonly')

def show_time():
	global popup_widget
	if check_show_time_checkbox.get() == 1:
		popup_widget = Toplevel(root)
		popup_widget.geometry("120x50")
		popup_widget.config(bg="black")
		popup_widget.resizable(0, 0)
		popup_widget.overrideredirect(1)
		popup_widget.wm_attributes("-topmost", 1)

		def start_move(event):
			global lastx, lasty
			lastx = event.x_root
			lasty = event.y_root

		def move_popup(event):
			global lastx, lasty
			deltax = event.x_root - lastx
			deltay = event.y_root - lasty
			x = popup_widget.winfo_x() + deltax
			y = popup_widget.winfo_y() + deltay
			popup_widget.geometry("+%s+%s" % (x, y))
			lastx = event.x_root
			lasty = event.y_root

		popup_widget.bind('<ButtonPress-1>', start_move)
		popup_widget.bind('<B1-Motion>', move_popup)

		popup_time = Label(popup_widget,
		                   text='',
		                   font=("Arial", 12, "bold"),
		                   fg='white',
		                   bg='black')
		popup_time.pack()
		popup_date = Label(popup_widget,
		                   text='',
		                   font=("Arial", 10, "bold"),
		                   fg='white',
		                   bg='black')
		popup_date.pack()

		def update_popup_time():
			popup_time_and_date_now = datetime.now(sri_lankan_time)
			popup_time_string = popup_time_and_date_now.strftime("%H:%M:%S")
			popup_date_string = popup_time_and_date_now.strftime("%m/%d/%Y")
			popup_time.config(text=popup_time_string)
			popup_date.config(text=popup_date_string)
			popup_date.after(1000, update_popup_time)

		update_popup_time()

	elif check_show_time_checkbox.get() == 0:
		popup_widget.destroy()


check_show_time_checkbox = IntVar()

scheduler_bottom_frame = Frame(scheduler_frame)
scheduler_bottom_frame.pack(expand=True, fill=BOTH)

show_time_checkbox = ttk.Checkbutton(scheduler_bottom_frame,
                                 text="Show Time",
                                 command=show_time,
                                 variable=check_show_time_checkbox)
show_time_checkbox.pack(side=LEFT)

loop_active = False  # global variable set to false

break_list = {1: None, 2: None, 3: None, 4: None}


def check_breaks():
	set_breaks()
	root.after(1000, check_breaks)


def update_breaks():  # new loop function that runs set_breaks and reschedules

	first_break_time = f'{first_break_hour_value.get()}:{first_break_minute_value.get()}:{first_break_second_value.get()}'

	second_break_time = f'{second_break_hour_value.get()}:{second_break_minute_value.get()}:{second_break_second_value.get()}'

	meal_break_time = f'{meal_break_hour_value.get()}:{meal_break_minute_value.get()}:{meal_break_second_value.get()}'

	logout_time = f'{logout_hour_value.get()}:{logout_minute_value.get()}:{logout_second_value.get()}'

	break_list[1] = first_break_time
	break_list[2] = second_break_time
	break_list[3] = meal_break_time
	break_list[4] = logout_time

	set_breaks()


def set_breaks():
	sri_lankan_time = pytz.timezone("Asia/Colombo")
	check_break = datetime.now(sri_lankan_time).strftime("%H:%M:%S")
	
	screen_width = int(GetSystemMetrics(0))
	popup_position_x = str(int((screen_width-600)/2))
	screen_height = int(GetSystemMetrics(1))
	popup_position_y = str(int((screen_height-300)/2))

	if check_break == break_list[1]:
		popup_first_break = Toplevel(root)
		popup_first_break.geometry(f'600x300+{popup_position_x}+{popup_position_y}')
		popup_first_break.overrideredirect(True)
		popup_first_break.wm_attributes("-topmost", 1)
		popup_first_break_image = ImageTk.PhotoImage(Image.open("resources/official_break_1.png"))
		popup_first_break_image_label = Label(popup_first_break, image = popup_first_break_image)
		popup_first_break_image_label.photo = popup_first_break_image
		popup_first_break_image_label.pack(side=LEFT)
		popup_first_break_title_bar = Label(popup_first_break,
		                                    text='OFFICIAL BREAK',
		                                    fg='Red')
		popup_first_break_title_bar.config(font=('Calibri', 32, 'bold'))
		popup_first_break_title_bar.pack(pady=10)
		popup_first_break_description = Label(popup_first_break
			, text = 'After hard working time you have got a time to relax\nyourself. Forget about the rush and work for a little\nbit of time, have a glass of water, close your eyes and\nmake your mind free...')
		popup_first_break_description.pack()
		def destroy_popup():
			popup_first_break.destroy()
		popup_first_break_exit = ttk.Button(popup_first_break, text='Exit', command=destroy_popup)
		popup_first_break_exit.pack(pady=50)
	elif check_break == break_list[2]:
		popup_second_break = Toplevel(root)
		popup_second_break.geometry(f'600x300+{popup_position_x}+{popup_position_y}')
		popup_second_break.overrideredirect(True)
		popup_second_break.wm_attributes("-topmost", 1)
		popup_second_break_image = ImageTk.PhotoImage(Image.open("resources/official_break_2.png"))
		popup_second_break_image_label = Label(popup_second_break, image = popup_second_break_image)
		popup_second_break_image_label.photo = popup_second_break_image
		popup_second_break_image_label.pack(side=LEFT)
		popup_second_break_title_bar = Label(popup_second_break,
		                                     text='OFFICIAL BREAK',
		                                     fg='Red')
		popup_second_break_title_bar.config(font=('Calibri', 32, 'bold'))
		popup_second_break_title_bar.pack()
		popup_second_break_description = Label(popup_second_break
			, text = 'After hard working time you have got a time to relax\nyourself. Forget about the rush and work for a little\nbit of time, have a glass of water, close your eyes and\nmake your mind free...')
		popup_second_break_description.pack()
		def destroy_popup():
			popup_second_break.destroy()
		popup_second_break_exit = ttk.Button(popup_second_break, text='Exit', command=destroy_popup)
		popup_second_break_exit.pack(pady=50)
	elif check_break == break_list[3]:
		popup_meal_break = Toplevel(root)
		popup_meal_break.title('Meal Break')
		popup_meal_break.geometry(f'600x300+{popup_position_x}+{popup_position_y}')
		popup_meal_break.overrideredirect(True)
		popup_meal_break.wm_attributes("-topmost", 1)
		popup_meal_break_image = ImageTk.PhotoImage(Image.open("resources/meal_break.png"))
		popup_meal_break_image_label = Label(popup_meal_break, image = popup_meal_break_image)
		popup_meal_break_image_label.photo = popup_meal_break_image
		popup_meal_break_image_label.pack(side=LEFT)
		popup_meal_break_title_bar = Label(popup_meal_break,
		                                   text='MEAL BREAK',
		                                   fg='Red')
		popup_meal_break_title_bar.config(font=('Calibri', 32, 'bold'))
		popup_meal_break_title_bar.pack()
		popup_meal_break_description = Label(popup_meal_break, text = 'I know you are hungry, because you have handled a lot\nof calls till now. I hope that your meals are ready, so go\nand have them. As well as have a little bit of a\nlong break...')
		popup_meal_break_description.pack()
		def destroy_popup():
			popup_meal_break.destroy()
		popup_meal_break_exit = ttk.Button(popup_meal_break, text='Exit', command=destroy_popup)
		popup_meal_break_exit.pack(pady=50)
	elif check_break == break_list[4]:
		popup_logout = Toplevel(root)
		popup_logout.title('Logout')
		popup_logout.geometry(f'600x300+{popup_position_x}+{popup_position_y}')
		popup_logout.overrideredirect(True)
		popup_logout.wm_attributes("-topmost", 1)
		popup_logout_image = ImageTk.PhotoImage(Image.open("resources/logout.png"))
		popup_logout_image_label = Label(popup_logout, image = popup_logout_image)
		popup_logout_image_label.photo = popup_logout_image
		popup_logout_image_label.pack(side=LEFT)
		popup_logout_title_bar = Label(popup_logout, text='LOGOUT', fg='Red')
		popup_logout_title_bar.config(font=('Calibri', 32, 'bold'))
		popup_logout_title_bar.pack()
		popup_logout_description = Label(popup_logout, text='Your hard time is over now. You are supposed to logout.\nPlease logout and go')
		popup_logout_description.pack()
		def destroy_popup():
			popup_logout.destroy()
		popup_logout_exit = ttk.Button(popup_logout, text='Exit', command=destroy_popup)
		popup_logout_exit.pack(pady=50)
	else:
		pass
	global loop_active
	if not loop_active:
		loop_active = True
		check_breaks()


set_breaks_button = ttk.Button(scheduler_bottom_frame,
                           text='Set',
                           command=update_breaks)
set_breaks_button.pack(side=RIGHT, fill=BOTH)

created_by_label = Label(left_pane, text="Created by Muneeb Asmone", anchor=SW)
created_by_label.pack(fill=X)


right_pane = Frame(root)
right_pane.pack(side=LEFT, expand=True, fill=BOTH)

tab_control = ttk.Notebook(right_pane, width=370)

ticket_tab = ttk.Frame(tab_control)

tab_control.add(ticket_tab, text="Tickets")

tab_control.pack(expand=1, fill=BOTH)

ticket_tab_up = Frame(ticket_tab)
ticket_tab_up.pack(side=TOP, expand=True, fill=BOTH)


def show_ticket():
	try:
		slr_tab.pack(side=TOP, expand=True, fill=BOTH)
	except:
		pass


selected_radio = StringVar()

slr_radio = ttk.Radiobutton(ticket_tab_up,
                            text="SLR",
                            value="Value 1",
                            variable=selected_radio,
                            command=show_ticket)
slr_radio.pack()
slr_radio.invoke()

slr_tab = Frame(ticket_tab)

slr_tab_up = LabelFrame(slr_tab, text="Enter Details...")
slr_tab_up.pack(side=TOP, expand=True, fill=BOTH)

left_slr_tab_up = Frame(slr_tab_up)
left_slr_tab_up.pack(side=LEFT, expand=True, fill=BOTH)

show_ticket()

def calculation():
	if int(no_of_tickets_spinbox.get()) >=5:
		no_of_tickets_spinbox.set("5")

	no_of_tickets_calculation = int(no_of_tickets_spinbox.get())
	price_of_one_ticket_calculation = float(price_of_one_ticket_spinbox.get())

	ticket_price_calculation = "{0:,.2f}".format(price_of_one_ticket_calculation *
	                                             no_of_tickets_calculation)
	ticket_price_entry.config(state=NORMAL)
	ticket_price_entry.delete(0, END)
	ticket_price_entry.insert(END, ticket_price_calculation)
	ticket_price_entry.config(state='readonly')

	reservation_charge_calculation = "{0:,.2f}".format(
	 float(ticket_price_calculation.replace(',', '')) * 0.25)
	reservation_charge_entry.config(state=NORMAL)
	reservation_charge_entry.delete(0, END)
	reservation_charge_entry.insert(END, reservation_charge_calculation)
	reservation_charge_entry.config(state='readonly')

	total_ticket_price_calculation = "{0:,.2f}".format(
	 float(ticket_price_calculation.replace(',', '')) +
	 float(reservation_charge_calculation.replace(',', '')))
	total_ticket_price_entry.config(state=NORMAL)
	total_ticket_price_entry.delete(0, END)
	total_ticket_price_entry.insert(END, total_ticket_price_calculation)
	total_ticket_price_entry.config(state='readonly')

	other_commission_calculation = "{0:,.2f}".format(
	 float(ticket_price_calculation.replace(',', '')) * (5 / 100))
	other_commission_entry.config(state=NORMAL)
	other_commission_entry.delete(0, END)
	other_commission_entry.insert(END, other_commission_calculation)
	other_commission_entry.config(state='readonly')

	dialog_commission_calculation = "{0:,.2f}".format(
	 float(ticket_price_calculation.replace(',', '')) * (12 / 100))
	dialog_commission_entry.config(state=NORMAL)
	dialog_commission_entry.delete(0, END)
	dialog_commission_entry.insert(END, dialog_commission_calculation)
	dialog_commission_entry.config(state='readonly')

	tax_amount_calculation = "{0:,.2f}".format(
	 float(ticket_price_calculation.replace(',', '')) * (3.05 / 100))
	tax_amount_entry.config(state=NORMAL)
	tax_amount_entry.delete(0, END)
	tax_amount_entry.insert(END, tax_amount_calculation)
	tax_amount_entry.config(state='readonly')

	dialog_commission_inclusive_taxes_calculation = "{0:,.2f}".format(
	 float(dialog_commission_calculation.replace(',', '')) +
	 float(tax_amount_calculation.replace(',', '')))
	dialog_commission_inclusive_taxes_entry.config(state=NORMAL)
	dialog_commission_inclusive_taxes_entry.delete(0, END)
	dialog_commission_inclusive_taxes_entry.insert(
	 END, dialog_commission_inclusive_taxes_calculation)
	dialog_commission_inclusive_taxes_entry.config(state='readonly')

	reservation_charge_inclusive_taxes_calculation = "{0:,.2f}".format(
	 float(dialog_commission_inclusive_taxes_calculation.replace(',', '')) +
	 float(other_commission_calculation.replace(',', '')))
	reservation_charge_inclusive_taxes_entry.config(state=NORMAL)
	reservation_charge_inclusive_taxes_entry.delete(0, END)
	reservation_charge_inclusive_taxes_entry.insert(
	 END, reservation_charge_inclusive_taxes_calculation)
	reservation_charge_inclusive_taxes_entry.config(state='readonly')

	total_to_be_billed_calculation = "{0:,.2f}".format(
	 float(ticket_price_calculation.replace(',', '')) +
	 float(reservation_charge_inclusive_taxes_calculation.replace(',', '')))
	total_to_be_billed_entry.config(state=NORMAL)
	total_to_be_billed_entry.delete(0, END)
	total_to_be_billed_entry.insert(END, total_to_be_billed_calculation)
	total_to_be_billed_entry.config(state='readonly')

def do_calculations(event):

	calculation()


no_of_tickets_label = Label(left_slr_tab_up,
                            text="No of Tickets:",
                            justify=LEFT)
no_of_tickets_label.grid(sticky=W, row=0, column=0)

default_no_of_tickets = IntVar()
default_no_of_tickets.set(1)
no_of_tickets_spinbox = ttk.Spinbox(left_slr_tab_up,
                                    from_=1,
                                    to=5,
                                    increment=1, textvariable=default_no_of_tickets)
no_of_tickets_spinbox.grid(row=0, column=1)

no_of_tickets_spinbox.bind('<Tab>', do_calculations)
no_of_tickets_spinbox.bind('<Return>', do_calculations)
no_of_tickets_spinbox.bind('<FocusOut>', do_calculations)


price_of_one_ticket_label = Label(left_slr_tab_up,
                                  text="Price of One Ticket (LKR):")
price_of_one_ticket_label.grid(sticky=W, row=1, column=0)

default_price_of_one_ticket = StringVar()
default_price_of_one_ticket.set('1.00')
price_of_one_ticket_spinbox = ttk.Spinbox(left_slr_tab_up,
                                          from_=1.00,
                                          to=100000.00,
                                          increment=1,
                                          textvariable=default_price_of_one_ticket,
                                          format="%.2f")
price_of_one_ticket_spinbox.grid(row=1, column=1)

price_of_one_ticket_spinbox.bind('<Tab>', do_calculations)
price_of_one_ticket_spinbox.bind('<Return>', do_calculations)
price_of_one_ticket_spinbox.bind('<FocusOut>', do_calculations)

right_slr_tab_up = Frame(slr_tab_up)
right_slr_tab_up.pack(side=LEFT, expand=True, fill=BOTH)

calculate_button = ttk.Button(right_slr_tab_up,
                          text="Calculate",
                          command=calculation)
calculate_button.pack(side=BOTTOM, expand=True, fill=X)

slr_tab_down = LabelFrame(slr_tab, text="Calculated Details...")
slr_tab_down.pack(side=TOP, expand=True, fill=BOTH)

ticket_price_label = Label(slr_tab_down, text="Ticket Price:", justify=LEFT)
ticket_price_label.grid(sticky=W, row=0, column=0)
ticket_price_entry = Entry(slr_tab_down, justify=RIGHT)
ticket_price_entry.insert(END, "1.00")
ticket_price_entry.config(state='readonly')
ticket_price_entry.grid(sticky=E, row=0, column=1)

reservation_charge_label = Label(
 slr_tab_down, text="Reservation Charges: (Ticket Price * 25%)", justify=LEFT)
reservation_charge_label.grid(sticky=W, row=1, column=0)
reservation_charge_entry = Entry(slr_tab_down, justify=RIGHT)
reservation_charge_entry.insert(END, "0.25")
reservation_charge_entry.config(state='readonly')
reservation_charge_entry.grid(sticky=E, row=1, column=1)

total_ticket_price_label = Label(slr_tab_down,
                                 text="Total Ticket Price:",
                                 justify=LEFT)
total_ticket_price_label.grid(sticky=W, row=2, column=0)
total_ticket_price_entry = Entry(slr_tab_down, justify=RIGHT)
total_ticket_price_entry.insert(END, "1.25")
total_ticket_price_entry.config(state='readonly')
total_ticket_price_entry.grid(sticky=E, row=2, column=1)

other_commission_label = Label(slr_tab_down,
                               text="Other Commission:",
                               justify=LEFT)
other_commission_label.grid(sticky=W, row=3, column=0)
other_commission_entry = Entry(slr_tab_down, justify=RIGHT)
other_commission_entry.insert(END, "0.05")
other_commission_entry.config(state='readonly')
other_commission_entry.grid(sticky=E, row=3, column=1)

dialog_commission_label = Label(slr_tab_down,
                                text="Dialog Commission:",
                                justify=LEFT)
dialog_commission_label.grid(sticky=W, row=4, column=0)
dialog_commission_entry = Entry(slr_tab_down, justify=RIGHT)
dialog_commission_entry.insert(END, "0.12")
dialog_commission_entry.config(state='readonly')
dialog_commission_entry.grid(sticky=E, row=4, column=1)

tax_amount_label = Label(slr_tab_down, text="Tax Amount:", justify=LEFT)
tax_amount_label.grid(sticky=W, row=5, column=0)
tax_amount_entry = Entry(slr_tab_down, justify=RIGHT)
tax_amount_entry.insert(END, "0.03")
tax_amount_entry.config(state='readonly')
tax_amount_entry.grid(sticky=E, row=5, column=1)

dialog_commission_inclusive_taxes_label = Label(
 slr_tab_down, text="Dialog Commission Inclusive Taxes:", justify=LEFT)
dialog_commission_inclusive_taxes_label.grid(sticky=W, row=6, column=0)
dialog_commission_inclusive_taxes_entry = Entry(slr_tab_down, justify=RIGHT)
dialog_commission_inclusive_taxes_entry.insert(END, "0.15")
dialog_commission_inclusive_taxes_entry.config(state='readonly')
dialog_commission_inclusive_taxes_entry.grid(sticky=E, row=6, column=1)

dialog_commission_inclusive_taxes_definition_label = Label(
 slr_tab_down, text="(Dialog Commission + Tax Amount)", justify=LEFT)
dialog_commission_inclusive_taxes_definition_label.grid(sticky=W,
                                                        row=7,
                                                        column=0)

reservation_charge_inclusive_taxes_label = Label(
 slr_tab_down, text="Reservation Charge Inclusive Taxes:", justify=LEFT)
reservation_charge_inclusive_taxes_label.grid(sticky=W, row=8, column=0)
reservation_charge_inclusive_taxes_entry = Entry(slr_tab_down, justify=RIGHT)
reservation_charge_inclusive_taxes_entry.insert(END, "0.20")
reservation_charge_inclusive_taxes_entry.config(state='readonly')
reservation_charge_inclusive_taxes_entry.grid(sticky=E, row=8, column=1)
reservation_charge_inclusive_taxes_definition_label = Label(
 slr_tab_down,
 text="(Dialog Commission Inclusive Taxes + Other Commision)",
 justify=LEFT)

reservation_charge_inclusive_taxes_definition_label.grid(sticky=W,
                                                         row=9,
                                                         column=0,
                                                         columnspan=2)

total_to_be_billed_label = Label(slr_tab_down,
                                 text="Total to be Billed:",
                                 justify=LEFT)
total_to_be_billed_label.grid(sticky=W, row=10, column=0)
total_to_be_billed_entry = Entry(slr_tab_down, justify=RIGHT)
total_to_be_billed_entry.insert(END, "1.20")
total_to_be_billed_entry.config(state='readonly')
total_to_be_billed_entry.grid(sticky=E, row=10, column=1)

root.mainloop()
