import sys
from PySide6.QtWidgets import QApplication, QSlider, QStyleOptionSlider, QStyle
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt

class TestSlider(QSlider):
    def paintEvent(self, event):
        opt = QStyleOptionSlider()
        self.initStyleOption(opt)
        
        painter = QPainter(self)
        
        # Draw groove only
        opt.subControls = QStyle.SubControl.SC_SliderGroove
        self.style().drawComplexControl(QStyle.ComplexControl.CC_Slider, opt, painter, self)
        
        # Draw red rect over center
        gr = self.style().subControlRect(QStyle.ComplexControl.CC_Slider, opt, QStyle.SubControl.SC_SliderGroove, self)
        painter.fillRect(gr.x() + 20, gr.y(), 100, gr.height(), QColor("red"))
        
        # Draw handle
        opt.subControls = QStyle.SubControl.SC_SliderHandle
        self.style().drawComplexControl(QStyle.ComplexControl.CC_Slider, opt, painter, self)

app = QApplication(sys.argv)
s = TestSlider(Qt.Orientation.Horizontal)
s.show()
s.setValue(50)
print("showing UI...")
sys.exit(0)
