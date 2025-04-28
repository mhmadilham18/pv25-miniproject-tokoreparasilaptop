from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap

class CardWidget(QWidget):
    def __init__(self, title, value, icon_path=None):
        super().__init__()
        self.title = title
        self.value = value
        self.icon_path = icon_path
        self.init_ui()

    def init_ui(self):

        main_layout = QHBoxLayout()
        main_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)


        container = QWidget()
        container_layout = QHBoxLayout()
        container.setObjectName("mainContainer")
        container_layout.setAlignment(Qt.AlignLeft)
        container.setLayout(container_layout)
        container.setFixedWidth(450)



        # Icon
        self.icon_label = QLabel()
        if self.icon_path:
            pixmap = QPixmap(self.icon_path)
            pixmap = pixmap.scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.icon_label.setPixmap(pixmap)
        self.icon_label.setFixedSize(48, 48)
        self.icon_label.setAlignment(Qt.AlignCenter)

        # Text (Title + Value)
        text_layout = QVBoxLayout()
        text_layout.setAlignment(Qt.AlignVCenter)
        text_layout.setSpacing(5)

        self.title_label = QLabel(self.title)
        self.title_label.setFont(QFont('Arial', 8))
        self.title_label.setAlignment(Qt.AlignLeft)
        self.title_label.setContentsMargins(0, 0, 40, 0)

        self.value_label = QLabel(self.value)
        self.value_label.setFont(QFont('Arial', 16, QFont.Bold))
        self.value_label.setAlignment(Qt.AlignLeft)
        self.value_label.setContentsMargins(0, 0, 40, 0)

        text_layout.addWidget(self.title_label)
        text_layout.addWidget(self.value_label)



        container_layout.addWidget(self.icon_label)
        container_layout.addSpacing(10)
        container_layout.addLayout(text_layout)

        # === Tambahkan container ke main layout ===
        main_layout.addWidget(container)
        # Set StyleSheet untuk container
        self.setStyleSheet("""
                            #mainContainer {
                                background-color: #FFFFFF;
                                border: 2px solid #2980B9;
                                border-radius: 10px;
                                
                                
                            }

                        """)

        self.setLayout(main_layout)

    def update_value(self, new_value):
        self.value = new_value
        self.value_label.setText(new_value)
