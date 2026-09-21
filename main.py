import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from app.ui.dashboard import DashboardPage
from app.ui.key_management_page import KeyManagementPage
from app.ui.encryption import EncryptionPage
from app.ui.decryption import DecryptionPage
from app.ui.digital_signatures import DigitalSignaturesPage
from app.ui.steganography import SteganographyPage
from app.ui.vault import VaultPage
from app.ui.logs_reports import LogsReportsPage
from app.ui.malware_scanner import MalwareScannerPage
from app.ui.settings import SettingsPage
from app.database.db import initialize_database


class CryptoraWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Cryptora - Secure Communication & Data Protection"
        )

        self.resize(1200, 750)

        self.setup_ui()

    def setup_ui(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(260)

        sidebar_outer_layout = QVBoxLayout(sidebar)
        sidebar_outer_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_outer_layout.setSpacing(0)

        header_widget = QWidget()
        header_layout = QVBoxLayout(header_widget)
        header_layout.setContentsMargins(22, 28, 22, 10)
        header_layout.setSpacing(8)

        logo = QLabel("CRYPTORA")
        logo.setObjectName("logo")

        tagline = QLabel(
            "Secure Communication\n"
            "& Data Protection"
        )
        tagline.setObjectName("tagline")

        header_layout.addWidget(logo)
        header_layout.addWidget(tagline)

        sidebar_outer_layout.addWidget(header_widget)

        sidebar_scroll = QScrollArea()
        sidebar_scroll.setWidgetResizable(True)
        sidebar_scroll.setFrameShape(QFrame.NoFrame)
        sidebar_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        sidebar_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        sidebar_scroll.setObjectName("sidebarScroll")

        sidebar_content = QWidget()
        sidebar_content.setObjectName("sidebarContent")

        sidebar_layout = QVBoxLayout(sidebar_content)
        sidebar_layout.setContentsMargins(22, 10, 22, 22)
        sidebar_layout.setSpacing(8)

        navigation_label = QLabel("MAIN MENU")
        navigation_label.setObjectName("sectionLabel")

        sidebar_layout.addWidget(navigation_label)
        sidebar_layout.addSpacing(5)

        self.dashboard_button = self.create_nav_button("⌂    Dashboard")
        self.key_button = self.create_nav_button("🔑    Key Management")
        self.encrypt_button = self.create_nav_button("🔒    Encrypt Data")
        self.decrypt_button = self.create_nav_button("🔓    Decrypt Data")
        self.signature_button = self.create_nav_button("✍    Digital Signatures")
        self.stego_button = self.create_nav_button("▣    Hide Data in Media")
        self.vault_button = self.create_nav_button("▤    Encrypted Vault")
        self.logs_button = self.create_nav_button("☷    Activity Logs & Reports")
        self.malware_button = self.create_nav_button("🛡    Malware Scanner")

        navigation_buttons = [
            self.dashboard_button,
            self.key_button,
            self.encrypt_button,
            self.decrypt_button,
            self.signature_button,
            self.stego_button,
            self.vault_button,
            self.logs_button,
            self.malware_button,
        ]

        for button in navigation_buttons:
            sidebar_layout.addWidget(button)

        sidebar_layout.addSpacing(18)

        settings_label = QLabel("SYSTEM")
        settings_label.setObjectName("sectionLabel")

        sidebar_layout.addWidget(settings_label)

        self.settings_button = self.create_nav_button("⚙    Settings")
        sidebar_layout.addWidget(self.settings_button)

        sidebar_layout.addStretch()

        sidebar_scroll.setWidget(sidebar_content)
        sidebar_outer_layout.addWidget(sidebar_scroll, 1)

        self.pages = QStackedWidget()

        self.dashboard_page = DashboardPage()
        self.key_page = KeyManagementPage()
        self.encrypt_page = EncryptionPage()
        self.decrypt_page = DecryptionPage()
        self.signature_page = DigitalSignaturesPage()
        self.stego_page = SteganographyPage()
        self.vault_page = VaultPage()
        self.logs_page = LogsReportsPage()
        self.malware_page = MalwareScannerPage()
        self.settings_page = SettingsPage()

        self.pages.addWidget(self.dashboard_page)
        self.pages.addWidget(self.key_page)
        self.pages.addWidget(self.encrypt_page)
        self.pages.addWidget(self.decrypt_page)
        self.pages.addWidget(self.signature_page)
        self.pages.addWidget(self.stego_page)
        self.pages.addWidget(self.vault_page)
        self.pages.addWidget(self.logs_page)
        self.pages.addWidget(self.malware_page)
        self.pages.addWidget(self.settings_page)

        self.dashboard_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.dashboard_page)
        )
        self.key_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.key_page)
        )
        self.encrypt_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.encrypt_page)
        )
        self.decrypt_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.decrypt_page)
        )
        self.signature_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.signature_page)
        )
        self.stego_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.stego_page)
        )
        self.vault_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.vault_page)
        )
        self.logs_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.logs_page)
        )
        self.malware_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.malware_page)
        )
        self.settings_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.settings_page)
        )

        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.pages)

        self.pages.setCurrentWidget(self.dashboard_page)

        self.setStyleSheet("""
            QMainWindow {
                background: #0b1120;
            }

            QWidget {
                font-family: "Segoe UI";
                color: #e5e7eb;
            }

            #sidebar {
                background: #111827;
                border-right: 1px solid #1f2937;
            }

            QScrollArea#sidebarScroll {
                background: transparent;
                border: none;
            }

            QWidget#sidebarContent {
                background: transparent;
            }

            #logo {
                font-size: 27px;
                font-weight: 800;
                letter-spacing: 2px;
                color: #f8fafc;
            }

            #tagline {
                font-size: 12px;
                color: #94a3b8;
            }

            #sectionLabel {
                font-size: 10px;
                font-weight: 700;
                color: #64748b;
                letter-spacing: 1.5px;
            }

            #navButton {
                background: transparent;
                color: #cbd5e1;
                border: none;
                border-radius: 9px;
                padding: 11px 12px;
                text-align: left;
                font-size: 13px;
            }

            #navButton:hover {
                background: #1e293b;
                color: #f8fafc;
            }

            #navButton:pressed {
                background: #243047;
            }
        """)

    def create_nav_button(self, text):
        button = QPushButton(text)
        button.setObjectName("navButton")
        button.setCursor(Qt.PointingHandCursor)
        return button


def main():

    app = QApplication(sys.argv)
    initialize_database()
    app.setStyle("Fusion")

    app.setStyleSheet("""
        QMessageBox {
            background-color: #111827;
            color: #f8fafc;
        }

        QMessageBox QLabel {
            color: #f8fafc;
            font-size: 13px;
            padding: 8px;
        }

        QMessageBox QPushButton {
            background-color: #2563eb;
            color: #ffffff;
            border: none;
            border-radius: 7px;
            padding: 8px 22px;
            min-width: 70px;
            font-weight: 600;
        }

        QMessageBox QPushButton:hover {
            background-color: #1d4ed8;
        }

        QMessageBox QPushButton:pressed {
            background-color: #1e40af;
        }
    """)

    app.setFont(QFont("Segoe UI", 10))

    window = CryptoraWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()