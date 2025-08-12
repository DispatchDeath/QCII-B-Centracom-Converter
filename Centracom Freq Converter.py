##written with chat gpt 5 and a lot of prompting

import tkinter as tk
from tkinter import messagebox

# ===== TABLE 1 (embedded) =====
table1 = [
 ['11','13','31','23','21','45','55','51','0a','0b','0c','0d','0e','d1','eb','70'],
 ['16','12','33','19','25','46','57','53','0f','1a','1b','1c','1d','d2','ec','71'],
 ['32','34','39','35','37','47','02','82','1e','1f','b3','b4','b5','d3','ed','72'],
 ['24','10','36','14','17','48','04','84','2a','2b','2c','2d','2e','d4','ee','73'],
 ['22','26','38','18','15','49','06','86','2f','b6','3a','3b','3c','d5','ef','74'],
 ['40','41','42','43','44','20','08','88','30','3e','3f','4a','4b','d6','f0','75'],
 ['56','58','03','05','07','01','59','4c','4d','4e','4f','4f','5a','d7','f1','76'],
 ['52','54','83','85','87','89','50','81','5b','5c','50','5e','5f','d8','f2','77'],
 ['7c','7d','7e','7f','b9','8a','a9','aa','60','63','67','8b','8c','d9','f3','78'],
 ['80','8e','8f','ba','bb','bc','ab','ac','61','62','68','bd','be','da','f4','79'],
 ['bf','c0','c1','c2','c3','9a','ad','ae','65','66','64','9b','9c','db','f5','80'],
 ['9d','9e','9f','a0','a1','a2','af','b0','b7','6a','6b','6c','6d','dc','f6','90'],
 ['a3','a4','a5','a6','a7','a8','b1','b2','6e','6f','b8','7a','7b','dd','f7','00'],
 ['c4','c5','c6','c7','c8','c9','ca','cb','cc','cd','ce','cf','d0','97','91','92'],
 ['de','df','e0','e1','e2','e3','e4','e5','e6','e7','e8','e9','ea','93','98','95'],
 ['f8','f9','fa','fb','fc','fd','fe','ff','27','28','29','30','69','94','96','99']
]

# ===== TABLE 2 (embedded) =====
table2 = [
 ['330.5','569.1','1092.4','321.7','553.9','1122.5','1472.9','1930.2','682.5','652.5','667.5','1743.0','1220.0','358.9','371.5','346.7'],
 ['349.0','600.9','288.5','339.6','584.8','1153.4','1513.5','1989.0','592.5','607.5','712.5','1820.0','335.6','398.1','412.1','384.6'],
 ['368.5','634.5','296.5','358.6','617.4','1185.2','1555.2','2043.8','757.5','787.5','772.5','1901.0','350.5','441.6','457.1','426.6'],
 ['389.0','669.9','304.7','378.6','651.9','1217.8','1598.0','2094.5','802.5','832.5','817.5','1985.0','366.0','489.8','507.0','473.2'],
 ['410.8','707.3','313.0','399.8','688.3','1251.4','1642.0','2155.6','847.5','877.5','862.5','2073.0','382.0','543.3','562.3','524.8'],
 ['433.7','746.8','953.7','422.1','726.8','1285.8','1687.2','2212.2','892.5','922.5','907.5','2164.0','399.2','602.6','623.7','582.1'],
 ['457.9','788.5','979.9','445.7','767.4','1321.2','1733.7','2271.7','937.5','967.5','952.5','2260.0','416.9','668.3','691.8','645.7'],
 ['483.5','832.5','1006.9','470.5','810.2','1357.6','1781.5','2334.6','547.5','517.5','532.5','2361.0','435.3','741.3','767.4','716.1'],
 ['510.5','879.0','1034.7','496.8','855.5','1395.0','1830.5','2401.0','727.5','562.5','577.5','2465.0','454.6','822.2','851.1','794.3'],
 ['539.0','928.1','1063.2','524.6','903.2','1433.4','1181.0','2468.2','637.5','697.5','622.5','2575.0','474.8','912.0','944.1','881.0'],
 ['1500.0','2856.0','625.0','1110.0','900.0','799.0','1036.0','1344.0','1192.5','997.5','1087.5','2688.0','495.8','1011.6','1047.1','977.2'],
 ['1550.0','2856.0','1695.0','1026.0','643.0','834.0','1082.0','1403.0','472.5','1207.5','1102.5','2807.0','1120.0','1122.1','1161.4','1084.0'],
 ['1600.0','2440.0','1520.0','949.5','672.0','871.0','1130.0','1465.0','487.5','1027.5','1117.5','2932.0','540.7','1190.0','1400.0','312.6'],
 ['1650.0','2255.0','1405.0','735.0','701.0','910.0','1180.0','1530.0','502.5','1042.5','1132.5','3062.0','564.7','1265.0','1430.5','2250.0'],
 ['1800.0','2084.0','1299.0','825.0','732.0','1070.0','1232.0','1280.0','742.5','1057.5','1147.5','394.7','589.7','1291.4','1450.0','2610.0'],
 ['1950.0','1926.0','1201.0','749.0','765.0','922.0','1170.0','1669.0','982.5','1077.5','1177.5','307.8','615.8','1355.0','2100.0','0.0']
]
##was easier to embed the data since it will never change than to reference it in a csv or something. 
# ---------------------
# Helper (forward): given 4-hex code -> two frequencies
# ---------------------
def forward_lookup(code):
    code = code.strip().lower()
    if len(code) != 4 or not all(c in "0123456789abcdef" for c in code):
        raise ValueError("Please enter a 4-digit hex code (0-1, a-f).")
    first_two = code[:2]
    last_two = code[2:]
    # find first_two in table1 (case-insensitive)
    r_idx = c_idx = None
    for i, row in enumerate(table1):
        for j, val in enumerate(row):
            if val.lower() == first_two.lower():
                r_idx, c_idx = i, j
                break
        if r_idx is not None:
            break
    if r_idx is None:
        raise ValueError(f"{first_two} not found in Table 1.")
    # Correct mapping (matches your example):
    # Tone A = table2[group = third_digit][row = r_idx]
    # Tone B = table2[group = fourth_digit][row = c_idx]
    group_a = int(last_two[0], 16)
    group_b = int(last_two[1], 16)
    tone_a = table2[group_a][r_idx]
    tone_b = table2[group_b][c_idx]
    return tone_a, tone_b

# ---------------------
# Helper (reverse): given two freqs -> original 4-hex code
# ---------------------
def reverse_lookup(freq_a, freq_b, tol=1e-6):
    # find positions in table2 (first try exact string, then numeric tolerance)
    def find_pos(freq):
        # exact string match first
        for g, row in enumerate(table2):
            for r, val in enumerate(row):
                if val == freq:
                    return g, r
        # numeric tolerance match
        try:
            fval = float(freq)
        except:
            return None
        for g, row in enumerate(table2):
            for r, val in enumerate(row):
                try:
                    if abs(float(val) - fval) <= tol:
                        return g, r
                except:
                    continue
        return None

    pos_a = find_pos(freq_a)
    pos_b = find_pos(freq_b)
    if (not pos_a) or (not pos_b):
        raise ValueError("One or both frequencies not found in Table 2.")
    group_a, row_a = pos_a  # group_a -> third digit, row_a -> r_idx (first digit)
    group_b, row_b = pos_b  # group_b -> fourth digit, row_b -> c_idx (second digit)
    # original hex pair is table1[row_a][row_b]
    try:
        original_hex = table1[row_a][row_b]
    except IndexError:
        raise ValueError("Reverse lookup produced invalid table indexes.")
    last_two = f"{format(group_a, 'x')}{format(group_b, 'x')}"
    return (original_hex + last_two).lower()

# ---------------------
# GUI (Tkinter)
# ---------------------
root = tk.Tk()
root.title("Code ↔ Frequency Lookup (embedded tables)")

tk.Label(root, text="4-Digit Cap Code:").grid(row=0, column=0, sticky="e")
entry_code = tk.Entry(root)
entry_code.grid(row=0, column=1)
def on_forward():
    try:
        tone_a, tone_b = forward_lookup(entry_code.get())
        output_var.set(f"Tone A: {tone_a}    Tone B: {tone_b}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
tk.Button(root, text="Code → Freqs", command=on_forward).grid(row=0, column=2, padx=5)

tk.Label(root, text="Frequency A:").grid(row=1, column=0, sticky="e")
entry_freq_a = tk.Entry(root)
entry_freq_a.grid(row=1, column=1)
tk.Label(root, text="Frequency B:").grid(row=2, column=0, sticky="e")
entry_freq_b = tk.Entry(root)
entry_freq_b.grid(row=2, column=1)

def on_reverse():
    try:
        code = reverse_lookup(entry_freq_a.get().strip(), entry_freq_b.get().strip(), tol=1e-3)
        output_var.set(f"Cap Code: {code}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

tk.Button(root, text="Freqs → Code", command=on_reverse).grid(row=2, column=2, padx=5)

output_var = tk.StringVar()
tk.Label(root, textvariable=output_var, fg="blue", font=("Arial", 12, "bold")).grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()
