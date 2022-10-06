from PIL import Image, ImageTk
import tkinter
import os
from tkintermapview import TkinterMapView

# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{1000}x{700}")
root_tk.title("ERZURUM ŞEHİR MERKEZİ")

# create map widget
map_widget = TkinterMapView(root_tk, width=1000, height=700, corner_radius=0)
map_widget.pack(fill="both", expand=True)
map_widget.set_position(39.9063235, 41.2731902) 

# load images in PhotoImage object
cifte_image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "cifte.jpg")).resize((300, 200)))
yakutiye_image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "yakutiye.jpg")).resize((300, 200)))
uckumbet_image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "uckumbetler.jpg")).resize((300, 200)))

def click_marker_event(marker):
    print("marker clicked:", marker.text)
    if marker.image_hidden is True:
        marker.hide_image(False)
    else:
        marker.hide_image(True)


marker_1 = map_widget.set_marker(39.9058055,41.2761686, text="Çifte Minareli Medrese", image=cifte_image, image_zoom_visibility=(0, float("inf")), command=click_marker_event)
marker_1.hide_image(True)

marker_2 = map_widget.set_marker(39.9064712,41.2711494, text="Yakutiye Medresesi", image=yakutiye_image, image_zoom_visibility=(0, float("inf")), command=click_marker_event)

marker_2.hide_image(True)

marker_3 = map_widget.set_marker(39.9039897,41.277434, text="Üç Kümbetler", image=uckumbet_image, image_zoom_visibility=(0, float("inf")), command=click_marker_event)
marker_3.hide_image(True)

map_widget.set_zoom(17)

root_tk.mainloop()