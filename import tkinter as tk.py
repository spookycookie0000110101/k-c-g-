import tkinter as tk
from tkinter import messagebox

# --- Hàm xử lý Logic ---

def thap_phan_sang_nhi_phan():
    try:
        val = int(entry_dec.get())
        if val < 0:
            raise ValueError
        # bin() trả về chuỗi có tiền tố '0b', ta dùng [2:] để loại bỏ nó
        entry_bin.delete(0, tk.END)
        entry_bin.insert(0, bin(val)[2:])
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số thập phân nguyên dương hợp lệ!")

def nhi_phan_sang_thap_phan():
    try:
        val = entry_bin.get()
        # Chuyển đổi từ hệ 2 sang hệ 10
        dec_val = int(val, 2)
        entry_dec.delete(0, tk.END)
        entry_dec.insert(0, str(dec_val))
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số nhị phân hợp lệ (chỉ chứa 0 và 1)!")

def tinh_toan_nhi_phan(phep_tinh):
    try:
        num1_bin = entry_num1.get()
        num2_bin = entry_num2.get()
        
        # Chuyển đổi cả 2 số sang thập phân để tính toán cho chính xác
        num1_dec = int(num1_bin, 2)
        num2_dec = int(num2_bin, 2)
        
        if phep_tinh == "cong":
            ket_qua_dec = num1_dec + num2_dec
        elif phep_tinh == "nhan":
            ket_qua_dec = num1_dec * num2_dec
            
        # Chuyển kết quả ngược lại thành nhị phân
        entry_result.delete(0, tk.END)
        entry_result.insert(0, bin(ket_qua_dec)[2:])
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng kiểm tra lại dữ liệu nhập vào (phải là số nhị phân)!")

# --- Xây dựng giao diện đồ họa (GUI) ---

root = tk.Tk()
root.title("Ứng Dụng Chuyển Đổi & Tính Toán Nhị Phân")
root.geometry("450x400")
root.resizable(False, False)

# Phần 1: Chuyển đổi hệ cơ số
frame_convert = tk.LabelFrame(root, text=" Chuyển Đổi Hệ Cơ Số ", padx=10, pady=10)
frame_convert.pack(fill="x", padx=15, pady=10)

tk.Label(frame_convert, text="Thập phân (Base 10):").grid(row=0, column=0, sticky="w", pady=5)
entry_dec = tk.Entry(frame_convert, width=20)
entry_dec.grid(row=0, column=1, pady=5, padx=5)
btn_to_bin = tk.Button(frame_convert, text="Đổi sang Nhị phân ➔", command=thap_phan_sang_nhi_phan)
btn_to_bin.grid(row=0, column=2, pady=5)

tk.Label(frame_convert, text="Nhị phân (Base 2):").grid(row=1, column=0, sticky="w", pady=5)
entry_bin = tk.Entry(frame_convert, width=20)
entry_bin.grid(row=1, column=1, pady=5, padx=5)
btn_to_dec = tk.Button(frame_convert, text="➔ Đổi sang Thập phân", command=nhi_phan_sang_thap_phan)
btn_to_dec.grid(row=1, column=2, pady=5)


# Phần 2: Phép tính trên hệ nhị phân
frame_calc = tk.LabelFrame(root, text=" Phép Tính Hệ Nhị Phân ", padx=10, pady=10)
frame_calc.pack(fill="x", padx=15, pady=10)

tk.Label(frame_calc, text="Số nhị phân thứ 1:").grid(row=0, column=0, sticky="w", pady=5)
entry_num1 = tk.Entry(frame_calc, width=25)
entry_num1.grid(row=0, column=1, columnspan=2, pady=5)

tk.Label(frame_calc, text="Số nhị phân thứ 2:").grid(row=1, column=0, sticky="w", pady=5)
entry_num2 = tk.Entry(frame_calc, width=25)
entry_num2.grid(row=1, column=1, columnspan=2, pady=5)

btn_cong = tk.Button(frame_calc, text="Cộng (+)", width=10, command=lambda: tinh_toan_nhi_phan("cong"))
btn_cong.grid(row=2, column=1, pady=10, padx=5, sticky="e")

btn_nhan = tk.Button(frame_calc, text="Nhân (×)", width=10, command=lambda: tinh_toan_nhi_phan("nhan"))
btn_nhan.grid(row=2, column=2, pady=10, padx=5, sticky="w")

tk.Label(frame_calc, text="Kết quả (Nhị phân):", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=5)
entry_result = tk.Entry(frame_calc, width=25, font=("Arial", 10, "bold"), fg="blue")
entry_result.grid(row=3, column=1, columnspan=2, pady=5)

root.mainloop()
