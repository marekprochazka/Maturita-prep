import tkinter as tk
from tkinter import ttk


def get_data():
    with open("listek.txt", "r") as f:
        data = f.readlines()
        return [{"currency": line[0:3], "number_units":float(line[6:9].strip()), "price_sell":float(line[14:21].strip().replace(",", ".")), "price_buy":float(line[24:30].strip().replace(",", "."))} for line in data]


def get_options(data):
    buy_options = [
        f"{line['currency']} - {line['price_buy']} (nákup) za {line['number_units']} mincí" for line in data]
    sell_options = [
        f"{line['currency']} - {line['price_sell']} (prodej) za {line['number_units']} mincí" for line in data]
    return buy_options, sell_options


def do_buy(data, currency, ammount):
    print(currency)
    for line in data:
        if line["currency"] == currency:
            currency_data = line
    price_czk = (ammount/currency_data["number_units"]
                 ) * (currency_data["price_buy"]) * 1.05
    return price_czk


def main():
    root = tk.Tk()
    root.wm_geometry("800x400")

    data = get_data()
    print(data)
    buy_options, sell_options = get_options(data)

    label_title = tk.Label(root, text="Směnárna")

    label_buyTitle = tk.Label(root, text="Nákup")
    combobox_buy = ttk.Combobox(root, values=buy_options)
    entry_buyAmmount = tk.Entry(root)
    button_buy = tk.Button(root, text="Koupit")

    label_sellTitle = tk.Label(root, text="Prodej")
    combobox_sell = ttk.Combobox(root, values=sell_options)
    entry_sellAmmount = tk.Entry(root)
    button_sell = tk.Button(root, text="Prodat")

    label_tradeResult = tk.Label(root, text="Výsledek")

    button_buy.configure(command=lambda: label_tradeResult.configure(
        text=do_buy(data, combobox_buy.get()[0:3], float(entry_buyAmmount.get()))))

    label_title.grid(row=0, column=0, columnspan=2)

    label_buyTitle.grid(row=1, column=0)
    combobox_buy.grid(row=2, column=0)
    entry_buyAmmount.grid(row=3, column=0)
    button_buy.grid(row=4, column=0)

    label_sellTitle.grid(row=1, column=1)
    combobox_sell.grid(row=2, column=1)
    entry_sellAmmount.grid(row=3, column=1)
    button_sell.grid(row=4, column=1)

    label_tradeResult.grid(row=5, column=0, columnspan=2)

    root.mainloop()


if __name__ == "__main__":
    main()
