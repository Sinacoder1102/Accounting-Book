import tkinter as tk
from tkinter import messagebox, filedialog

class AccountingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("حساب دفتری")
        self.root.geometry("800x500")  # تنظیم ابعاد پنجره

        # ایجاد فریم برای ورودی‌ها
        self.frame = tk.Frame(root, bg="#87CEEB", padx=20, pady=20)
        self.frame.pack(pady=10)

        # برچسب و ورودی نام مشتری
        self.label_name = tk.Label(self.frame, text="نام مشتری:", bg="#87CEEB", font=("Arial", 16, "bold"))
        self.label_name.grid(row=0, column=0, sticky="w", padx=5, pady=0)  # کاهش فاصله
        self.entry_name = tk.Entry(self.frame, width=50, font=("Arial", 16))  # افزایش طول
        self.entry_name.grid(row=0, column=1, padx=5, pady=0)  # کاهش فاصله عمودی

        # برچسب و ورودی میزان بدهی
        self.label_debt = tk.Label(self.frame, text="میزان بدهی:", bg="#87CEEB", font=("Arial", 16, "bold"))
        self.label_debt.grid(row=1, column=0, sticky="w", padx=5, pady=0)  # کاهش فاصله
        self.entry_debt = tk.Entry(self.frame, width=50, font=("Arial", 16))  # افزایش طول
        self.entry_debt.grid(row=1, column=1, padx=5, pady=0)  # کاهش فاصله عمودی

        # دکمه‌ها
        button_frame = tk.Frame(self.frame, bg="#87CEEB")
        button_frame.grid(row=2, columnspan=2, pady=10)

        # دکمه اضافه کردن
        self.button_add = tk.Button(button_frame, text="اضافه کردن", command=self.add_entry, bg="#c3e6c3", font=("Arial", 16, "bold"), height=2, width=10)
        self.button_add.pack(side=tk.LEFT, padx=5)

        # دکمه حذف
        self.button_delete = tk.Button(button_frame, text="حذف", command=self.delete_entry, bg="#f5c6cb", font=("Arial", 16, "bold"), height=2, width=10)
        self.button_delete.pack(side=tk.LEFT, padx=5)

        # دکمه بارگذاری نام‌ها
        self.button_load = tk.Button(button_frame, text="بارگذاری نام‌ها", command=self.load_names, bg="#c3e6c3", font=("Arial", 16, "bold"), height=2, width=10)
        self.button_load.pack(side=tk.LEFT, padx=5)

        # دکمه ذخیره
        self.button_save = tk.Button(button_frame, text="ذخیره", command=self.save_entries, bg="#c3e6c3", font=("Arial", 16, "bold"), height=2, width=10)
        self.button_save.pack(side=tk.LEFT, padx=5)

        # دکمه راهنما
        self.button_help = tk.Button(button_frame, text="راهنما", command=self.show_help, bg="#ffeeba", font=("Arial", 16, "bold"), height=2, width=10)
        self.button_help.pack(side=tk.LEFT, padx=5)

        # لیست برای نمایش اطلاعات
        self.listbox = tk.Listbox(root, width=70, height=15, font=("Arial", 16), bg="#fff3cd")
        self.listbox.pack(pady=10)

    def add_entry(self):
        name = self.entry_name.get()
        debt = self.entry_debt.get()

        if name and debt:
            self.listbox.insert(tk.END, f"{name}: {debt} تومان")
            self.entry_name.delete(0, tk.END)
            self.entry_debt.delete(0, tk.END)
        else:
            messagebox.showwarning("هشدار", "لطفا همه فیلدها را پر کنید.")

    def delete_entry(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_index)  # حذف نام انتخاب‌شده
        except IndexError:
            messagebox.showwarning("هشدار", "لطفا یک نام را انتخاب کنید.")

    def load_names(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        self.listbox.insert(tk.END, line.strip())
            except Exception as e:
                messagebox.showerror("خطا", f"بارگذاری نام‌ها با خطا مواجه شد: {e}")

    def save_entries(self):
        entries = []
        for item in self.listbox.get(0, tk.END):
            entries.append(item)  # ذخیره نام‌ها در لیست

        if entries:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as f:
                    for entry in entries:
                        f.write(entry + "\n")
                messagebox.showinfo("موفقیت", "اطلاعات با موفقیت ذخیره شد.")
        else:
            messagebox.showwarning("هشدار", "هیچ اطلاعاتی برای ذخیره وجود ندارد.")

    def show_help(self):
        help_message = (
            "راهنما:\n"
            "1. برای اضافه کردن نام و میزان بدهی، نام و بدهی را وارد کنید و روی 'اضافه کردن' کلیک کنید.\n"
            "2. برای حذف یک نام، آن را از لیست انتخاب کرده و روی 'حذف' کلیک کنید.\n"
            "3. برای بارگذاری نام‌ها از یک فایل متنی، روی 'بارگذاری نام‌ها' کلیک کنید.\n"
            "4. برای ذخیره اطلاعات به یک فایل متنی، روی 'ذخیره' کلیک کنید.\n"
            "توجه: قیمت‌ها به تومان هستند، نه به ریال."
        )
        messagebox.showinfo("راهنما", help_message)

# ایجاد پنجره اصلی
root = tk.Tk()
app = AccountingApp(root)

# اجرای حلقه اصلی
root.mainloop()
