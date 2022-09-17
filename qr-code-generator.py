#bitte im python editor ausführen

import qrcode

img = qrcode.make("https://htmlpreview.github.io/?https://github.com/Optimus-IT-Dienstleistungen/pdf-maker/blob/main/menu-karte.html#menu")
img.save("menu-karte.jpg")
