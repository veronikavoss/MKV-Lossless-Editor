import sys
from PySide6.QtWidgets import QApplication, QSlider, QStyleOptionSlider, QStyle
from PySide6.QtGui import QPainter, QColor, QImage, QPen
from PySide6.QtCore import Qt, QRectF
from PySide6.QtSvg import QSvgRenderer

class TestSlider(QSlider):
    def paintEvent(self, event):
        print("paintEvent called")
        try:
            val_range = self.maximum() - self.minimum()
            painter = QPainter(self)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)

            opt = QStyleOptionSlider()
            self.initStyleOption(opt)
            
            opt.subControls = QStyle.SubControl.SC_SliderGroove
            self.style().drawComplexControl(QStyle.ComplexControl.CC_Slider, opt, painter, self)

            print("Groove drawn")
            path = "d:/Coding/Gemini/mkvsplitter/assets/start_check_point.svg"
            renderer = QSvgRenderer(path)
            if renderer.isValid():
                print("Renderer valid")
                icon_size = 14
                img = QImage(icon_size, icon_size, QImage.Format.Format_ARGB32_Premultiplied)
                img.fill(Qt.GlobalColor.transparent)
                
                p2 = QPainter(img)
                p2.setRenderHint(QPainter.RenderHint.Antialiasing)
                renderer.render(p2, QRectF(0, 0, icon_size, icon_size))
                
                print("Setting composition mode")
                p2.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
                p2.fillRect(img.rect(), Qt.GlobalColor.white)
                p2.end()
                
                target_rect = QRectF(10, 10, icon_size, icon_size)
                painter.drawImage(target_rect, img)
            
            opt.subControls = QStyle.SubControl.SC_SliderHandle
            self.style().drawComplexControl(QStyle.ComplexControl.CC_Slider, opt, painter, self)
            print("Finished paintEvent successfully")
        except Exception as e:
            print(f"Exception in paintEvent: {e}")

app = QApplication(sys.argv)
s = TestSlider(Qt.Orientation.Horizontal)
s.show()
s.setValue(50)
sys.exit(app.exec())
