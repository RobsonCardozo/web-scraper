import tkinter as tk

def display_data_in_gui(data):
    # Create a Tkinter window to display the data
    window = tk.Tk()
    window.title("Wikipedia Categories")
    window.geometry("600x400")

    # Create labels to display the data
    title_label = tk.Label(window, text=f"Title: {data['title']}", font=("Arial", 14))
    title_label.pack(pady=10)

    description_label = tk.Label(window, text=f"Description: {data['description']}", font=("Arial", 12), wraplength=500, justify="left")
    description_label.pack(pady=10)

    categories_label = tk.Label(window, text=f"Categories: {', '.join(data['categories'])}", font=("Arial", 12), wraplength=500, justify="left")
    categories_label.pack(pady=10)

    images_label = tk.Label(window, text=f"Images: {', '.join(data['images'])}", font=("Arial", 12), wraplength=500, justify="left")
    images_label.pack(pady=10)

    external_links_label = tk.Label(window, text=f"External Links: {', '.join(data['external_links'])}", font=("Arial", 12), wraplength=500, justify="left")
    external_links_label.pack(pady=10)

    # Create a button to close the window
    close_button = tk.Button(window, text="Close", command=window.destroy)
    close_button.pack(pady=10)

    window.mainloop()
