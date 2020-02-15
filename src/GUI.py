# -*- coding: utf-8 -*-
# @package Data
# application frontend
# @author Pasquale De Marinis, Barile Roberto, Caputo Sergio

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem
from problog.learning.lfi import read_examples
from problog.program import SimpleProgram
from problog.program import PrologFile

from Data import PropertyMap, Property
from src.Query import DbmsQuery
from src.Query import CloudQuery
from Distribution import *


##
# Implements a class for GUI representation and operations' execution
class UiMainWindow(object):
    ## constructor
    # @param: main_window: main_window of the application
    def __init__(self, MainWindow):
        self.__cypher_data = None
        self.__sparql_data = None
        self.__problog_program = SimpleProgram()
        self.__examples = []

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(885, 635)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.__tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.__tabs.setGeometry(QtCore.QRect(20, 20, 851, 591))
        self.__tabs.setObjectName("__tabs")
        self.graph_db = QtWidgets.QWidget()
        self.graph_db.setObjectName("graph_db")
        self.layoutWidget = QtWidgets.QWidget(self.graph_db)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 801, 59))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.__parse_method_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__parse_method_label.setFont(font)
        self.__parse_method_label.setObjectName("__parse_method_label")
        self.gridLayout.addWidget(self.__parse_method_label, 1, 0, 1, 1)
        self.__execute_user_query = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__execute_user_query.setFont(font)
        self.__execute_user_query.setObjectName("__execute_user_query")
        self.gridLayout.addWidget(self.__execute_user_query, 0, 3, 1, 1)
        self.__user_query_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__user_query_label.setFont(font)
        self.__user_query_label.setObjectName("__user_query_label")
        self.gridLayout.addWidget(self.__user_query_label, 0, 0, 1, 1)
        self.__parse_method_combo = QtWidgets.QComboBox(self.layoutWidget)
        self.__parse_method_combo.setObjectName("__parse_method_combo")
        self.__parse_method_combo.addItem("")
        self.__parse_method_combo.addItem("")
        self.__parse_method_combo.addItem("")
        self.__parse_method_combo.addItem("")
        self.__parse_method_combo.addItem("")
        self.__parse_method_combo.addItem("")
        self.__parse_method_combo.addItem("")
        self.gridLayout.addWidget(self.__parse_method_combo, 1, 1, 1, 1)
        self.__user_query = QtWidgets.QLineEdit(self.layoutWidget)
        self.__user_query.setObjectName("__user_query")
        self.gridLayout.addWidget(self.__user_query, 0, 1, 1, 2)
        self.layoutWidget1 = QtWidgets.QWidget(self.graph_db)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 220, 801, 29))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.__nodes_and_relationships = QtWidgets.QPushButton(self.layoutWidget1)
        self.__nodes_and_relationships.setObjectName("__nodes_and_relationships")
        self.gridLayout_2.addWidget(self.__nodes_and_relationships, 0, 0, 1, 1)
        self.__relationships_without_properties = QtWidgets.QPushButton(self.layoutWidget1)
        self.__relationships_without_properties.setObjectName("__relationships_without_properties")
        self.gridLayout_2.addWidget(self.__relationships_without_properties, 0, 1, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.graph_db)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 292, 391, 251))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.__add_filter = QtWidgets.QPushButton(self.layoutWidget2)
        self.__add_filter.setObjectName("__add_filter")
        self.gridLayout_4.addWidget(self.__add_filter, 0, 1, 1, 1)
        self.__filter_nodes_label = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.__filter_nodes_label.setFont(font)
        self.__filter_nodes_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__filter_nodes_label.setObjectName("__filter_nodes_label")
        self.gridLayout_4.addWidget(self.__filter_nodes_label, 0, 0, 1, 1)
        self.__execute_property_filters_query = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__execute_property_filters_query.setFont(font)
        self.__execute_property_filters_query.setObjectName("__execute_property_filters_query")
        self.gridLayout_4.addWidget(self.__execute_property_filters_query, 3, 0, 1, 2)
        self.__property_filters_table = QtWidgets.QTableWidget(self.layoutWidget2)
        self.__property_filters_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.__property_filters_table.setRowCount(1)
        self.__property_filters_table.setObjectName("__property_filters_table")
        self.__property_filters_table.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.__property_filters_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.__property_filters_table.setHorizontalHeaderItem(1, item)
        self.__property_filters_table.horizontalHeader().setDefaultSectionSize(194)
        self.gridLayout_4.addWidget(self.__property_filters_table, 1, 0, 1, 2)
        self.__line = QtWidgets.QFrame(self.graph_db)
        self.__line.setGeometry(QtCore.QRect(-60, 90, 911, 20))
        self.__line.setFrameShape(QtWidgets.QFrame.HLine)
        self.__line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.__line.setObjectName("__line")
        self.__line_2 = QtWidgets.QFrame(self.graph_db)
        self.__line_2.setGeometry(QtCore.QRect(0, 190, 851, 16))
        self.__line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.__line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.__line_2.setObjectName("__line_2")
        self.__line_3 = QtWidgets.QFrame(self.graph_db)
        self.__line_3.setGeometry(QtCore.QRect(-10, 260, 851, 16))
        self.__line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.__line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.__line_3.setObjectName("__line_3")
        self.__line_4 = QtWidgets.QFrame(self.graph_db)
        self.__line_4.setGeometry(QtCore.QRect(425, 270, 20, 291))
        self.__line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.__line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.__line_4.setObjectName("__line_4")
        self.layoutWidget_4 = QtWidgets.QWidget(self.graph_db)
        self.layoutWidget_4.setGeometry(QtCore.QRect(20, 120, 801, 52))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_4)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.__closed_round_bracket_first_node = QtWidgets.QLabel(self.layoutWidget_4)
        self.__closed_round_bracket_first_node.setObjectName("__closed_round_bracket_first_node")
        self.gridLayout_3.addWidget(self.__closed_round_bracket_first_node, 1, 3, 1, 1)
        self.__open_round_bracket_first_node = QtWidgets.QLabel(self.layoutWidget_4)
        self.__open_round_bracket_first_node.setObjectName("__open_round_bracket_first_node")
        self.gridLayout_3.addWidget(self.__open_round_bracket_first_node, 1, 1, 1, 1)
        self.__open_round_bracket_second_node = QtWidgets.QLabel(self.layoutWidget_4)
        self.__open_round_bracket_second_node.setObjectName("__open_round_bracket_second_node")
        self.gridLayout_3.addWidget(self.__open_round_bracket_second_node, 1, 7, 1, 1)
        self.__second_node_type = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.__second_node_type.setObjectName("__second_node_type")
        self.gridLayout_3.addWidget(self.__second_node_type, 1, 8, 1, 1)
        self.__relationships_between_with_properties = QtWidgets.QPushButton(self.layoutWidget_4)
        self.__relationships_between_with_properties.setObjectName("__relationships_between_with_properties")
        self.gridLayout_3.addWidget(self.__relationships_between_with_properties, 1, 10, 1, 1)
        self.__relationship_type = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.__relationship_type.setObjectName("__relationship_type")
        self.gridLayout_3.addWidget(self.__relationship_type, 1, 5, 1, 1)
        self.__closed_square_bracket = QtWidgets.QLabel(self.layoutWidget_4)
        self.__closed_square_bracket.setObjectName("__closed_square_bracket")
        self.gridLayout_3.addWidget(self.__closed_square_bracket, 1, 6, 1, 1)
        self.__first_node_type = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.__first_node_type.setObjectName("__first_node_type")
        self.gridLayout_3.addWidget(self.__first_node_type, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.__relationships_between_without_properties = QtWidgets.QPushButton(self.layoutWidget_4)
        self.__relationships_between_without_properties.setObjectName("__relationships_between_without_properties")
        self.gridLayout_3.addWidget(self.__relationships_between_without_properties, 1, 11, 1, 1)
        self.__open_square_bracket = QtWidgets.QLabel(self.layoutWidget_4)
        self.__open_square_bracket.setObjectName("__open_square_bracket")
        self.gridLayout_3.addWidget(self.__open_square_bracket, 1, 4, 1, 1)
        self.__close_round_bracket_second_node = QtWidgets.QLabel(self.layoutWidget_4)
        self.__close_round_bracket_second_node.setObjectName("__close_round_bracket_second_node")
        self.gridLayout_3.addWidget(self.__close_round_bracket_second_node, 1, 9, 1, 1)
        self.__first_node_type_label = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__first_node_type_label.setFont(font)
        self.__first_node_type_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__first_node_type_label.setObjectName("__first_node_type_label")
        self.gridLayout_3.addWidget(self.__first_node_type_label, 0, 2, 1, 1)
        self.__second_node_type_label = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__second_node_type_label.setFont(font)
        self.__second_node_type_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__second_node_type_label.setObjectName("__second_node_type_label")
        self.gridLayout_3.addWidget(self.__second_node_type_label, 0, 8, 1, 1)
        self.__execute_label = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.__execute_label.setFont(font)
        self.__execute_label.setStyleSheet("")
        self.__execute_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__execute_label.setObjectName("__execute_label")
        self.gridLayout_3.addWidget(self.__execute_label, 0, 10, 1, 2)
        self.__relationship_type_label = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__relationship_type_label.setFont(font)
        self.__relationship_type_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__relationship_type_label.setObjectName("__relationship_type_label")
        self.gridLayout_3.addWidget(self.__relationship_type_label, 0, 5, 1, 1)
        self.layoutWidget3 = QtWidgets.QWidget(self.graph_db)
        self.layoutWidget3.setGeometry(QtCore.QRect(460, 290, 361, 251))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.__query_results_label = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.__query_results_label.setFont(font)
        self.__query_results_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__query_results_label.setObjectName("__query_results_label")
        self.gridLayout_7.addWidget(self.__query_results_label, 0, 0, 1, 1)
        self.__triples_table = QtWidgets.QTableWidget(self.layoutWidget3)
        self.__triples_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.__triples_table.setObjectName("__triples_table")
        self.__triples_table.setColumnCount(3)
        self.__triples_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.__triples_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.__triples_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.__triples_table.setHorizontalHeaderItem(2, item)
        self.__triples_table.horizontalHeader().setDefaultSectionSize(119)
        self.gridLayout_7.addWidget(self.__triples_table, 1, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("neo4j-database-meta-image-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.__tabs.addTab(self.graph_db, icon, "")
        self.sparql = QtWidgets.QWidget()
        self.sparql.setObjectName("sparql")
        self.layoutWidget4 = QtWidgets.QWidget(self.sparql)
        self.layoutWidget4.setGeometry(QtCore.QRect(20, 60, 801, 27))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.__sparql_user_query_label = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__sparql_user_query_label.setFont(font)
        self.__sparql_user_query_label.setObjectName("__sparql_user_query_label")
        self.gridLayout_5.addWidget(self.__sparql_user_query_label, 0, 0, 1, 1)
        self.__sparql_user_query = QtWidgets.QLineEdit(self.layoutWidget4)
        self.__sparql_user_query.setObjectName("__sparql_user_query")
        self.gridLayout_5.addWidget(self.__sparql_user_query, 0, 1, 1, 1)
        self.__sparql_execute_user_query = QtWidgets.QPushButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__sparql_execute_user_query.setFont(font)
        self.__sparql_execute_user_query.setObjectName("__sparql_execute_user_query")
        self.gridLayout_5.addWidget(self.__sparql_execute_user_query, 0, 2, 1, 1)
        self.layoutWidget_3 = QtWidgets.QWidget(self.sparql)
        self.layoutWidget_3.setGeometry(QtCore.QRect(20, 340, 801, 211))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.__sparql_triples_table = QtWidgets.QTableWidget(self.layoutWidget_3)
        self.__sparql_triples_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.__sparql_triples_table.setObjectName("__sparql_triples_table")
        self.__sparql_triples_table.setColumnCount(3)
        self.__sparql_triples_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.__sparql_triples_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.__sparql_triples_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.__sparql_triples_table.setHorizontalHeaderItem(2, item)
        self.__sparql_triples_table.horizontalHeader().setDefaultSectionSize(266)
        self.gridLayout_8.addWidget(self.__sparql_triples_table, 1, 0, 1, 1)
        self.__sparql_query_results_label = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.__sparql_query_results_label.setFont(font)
        self.__sparql_query_results_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__sparql_query_results_label.setObjectName("__sparql_query_results_label")
        self.gridLayout_8.addWidget(self.__sparql_query_results_label, 0, 0, 1, 1)
        self.__line_5 = QtWidgets.QFrame(self.sparql)
        self.__line_5.setGeometry(QtCore.QRect(0, 100, 851, 20))
        self.__line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.__line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.__line_5.setObjectName("__line_5")
        self.__line_6 = QtWidgets.QFrame(self.sparql)
        self.__line_6.setGeometry(QtCore.QRect(-10, 310, 891, 20))
        self.__line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.__line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.__line_6.setObjectName("__line_6")
        self.layoutWidget5 = QtWidgets.QWidget(self.sparql)
        self.layoutWidget5.setGeometry(QtCore.QRect(20, 20, 801, 27))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.layoutWidget5)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.__sparql_endpoint = QtWidgets.QLineEdit(self.layoutWidget5)
        self.__sparql_endpoint.setObjectName("__sparql_endpoint")
        self.gridLayout_9.addWidget(self.__sparql_endpoint, 0, 1, 1, 1)
        self.__sparql_endpoint_label = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__sparql_endpoint_label.setFont(font)
        self.__sparql_endpoint_label.setObjectName("__sparql_endpoint_label")
        self.gridLayout_9.addWidget(self.__sparql_endpoint_label, 0, 0, 1, 1)
        self.layoutWidget6 = QtWidgets.QWidget(self.sparql)
        self.layoutWidget6.setGeometry(QtCore.QRect(21, 131, 391, 171))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.__prefixs_label = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__prefixs_label.setFont(font)
        self.__prefixs_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__prefixs_label.setObjectName("__prefixs_label")
        self.gridLayout_6.addWidget(self.__prefixs_label, 0, 0, 1, 1)
        self.__sparql_add_prefix = QtWidgets.QPushButton(self.layoutWidget6)
        self.__sparql_add_prefix.setObjectName("__sparql_add_prefix")
        self.gridLayout_6.addWidget(self.__sparql_add_prefix, 0, 1, 1, 1)
        self.__prefixs_table = QtWidgets.QTableWidget(self.layoutWidget6)
        self.__prefixs_table.setRowCount(1)
        self.__prefixs_table.setObjectName("__prefixs_table")
        self.__prefixs_table.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.__prefixs_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.__prefixs_table.setHorizontalHeaderItem(1, item)
        self.__prefixs_table.horizontalHeader().setDefaultSectionSize(193)
        self.gridLayout_6.addWidget(self.__prefixs_table, 1, 0, 1, 2)
        self.layoutWidget7 = QtWidgets.QWidget(self.sparql)
        self.layoutWidget7.setGeometry(QtCore.QRect(430, 130, 391, 171))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.layoutWidget7)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.__sparql_filter_nodes_label = QtWidgets.QLabel(self.layoutWidget7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.__sparql_filter_nodes_label.setFont(font)
        self.__sparql_filter_nodes_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__sparql_filter_nodes_label.setObjectName("__sparql_filter_nodes_label")
        self.gridLayout_10.addWidget(self.__sparql_filter_nodes_label, 0, 0, 1, 1)
        self.__sparql_add_filter = QtWidgets.QPushButton(self.layoutWidget7)
        self.__sparql_add_filter.setObjectName("__sparql_add_filter")
        self.gridLayout_10.addWidget(self.__sparql_add_filter, 0, 1, 1, 1)
        self.__sparql_execute_property_filters_query = QtWidgets.QPushButton(self.layoutWidget7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__sparql_execute_property_filters_query.setFont(font)
        self.__sparql_execute_property_filters_query.setObjectName("__sparql_execute_property_filters_query")
        self.gridLayout_10.addWidget(self.__sparql_execute_property_filters_query, 2, 0, 1, 2)
        self.__sparql_property_filters_table = QtWidgets.QTableWidget(self.layoutWidget7)
        self.__sparql_property_filters_table.setRowCount(1)
        self.__sparql_property_filters_table.setObjectName("__sparql_property_filters_table")
        self.__sparql_property_filters_table.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.__sparql_property_filters_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.__sparql_property_filters_table.setHorizontalHeaderItem(1, item)
        self.__sparql_property_filters_table.horizontalHeader().setDefaultSectionSize(193)
        self.gridLayout_10.addWidget(self.__sparql_property_filters_table, 1, 0, 1, 2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("sparql-blog-1-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.__tabs.addTab(self.sparql, icon1, "")
        self.Problog = QtWidgets.QWidget()
        self.Problog.setObjectName("Problog")
        self.layoutWidget_2 = QtWidgets.QWidget(self.Problog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(620, 20, 211, 105))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.__evidence_label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__evidence_label.setFont(font)
        self.__evidence_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__evidence_label.setObjectName("__evidence_label")
        self.gridLayout_13.addWidget(self.__evidence_label, 0, 0, 1, 2)
        self.__evidence_cypher = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.__evidence_cypher.setFont(font)
        self.__evidence_cypher.setObjectName("__evidence_cypher")
        self.gridLayout_13.addWidget(self.__evidence_cypher, 1, 0, 1, 2)
        self.__evidence_sparql = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.__evidence_sparql.setFont(font)
        self.__evidence_sparql.setObjectName("__evidence_sparql")
        self.gridLayout_13.addWidget(self.__evidence_sparql, 2, 0, 1, 2)
        self.__evidence_file = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.__evidence_file.setFont(font)
        self.__evidence_file.setObjectName("__evidence_file")
        self.gridLayout_13.addWidget(self.__evidence_file, 3, 0, 1, 2)
        self.layoutWidget_5 = QtWidgets.QWidget(self.Problog)
        self.layoutWidget_5.setGeometry(QtCore.QRect(390, 310, 441, 151))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.layoutWidget_5)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.__sparql_prob_bgk_label = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__sparql_prob_bgk_label.setFont(font)
        self.__sparql_prob_bgk_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__sparql_prob_bgk_label.setObjectName("__sparql_prob_bgk_label")
        self.gridLayout_15.addWidget(self.__sparql_prob_bgk_label, 0, 0, 1, 1)
        self.__sparql_add_distribution = QtWidgets.QPushButton(self.layoutWidget_5)
        self.__sparql_add_distribution.setObjectName("__sparql_add_distribution")
        self.gridLayout_15.addWidget(self.__sparql_add_distribution, 0, 1, 1, 1)
        self.__sparql_prop_distr_table = QtWidgets.QTableWidget(self.layoutWidget_5)
        self.__sparql_prop_distr_table.setRowCount(1)
        self.__sparql_prop_distr_table.setObjectName("__sparql_prop_distr_table")
        self.__sparql_prop_distr_table.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.__sparql_prop_distr_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.__sparql_prop_distr_table.setHorizontalHeaderItem(1, item)
        self.__sparql_prop_distr_table.horizontalHeader().setDefaultSectionSize(218)
        self.gridLayout_15.addWidget(self.__sparql_prop_distr_table, 1, 0, 1, 2)
        self.__sparql_distr_learning = QtWidgets.QPushButton(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__sparql_distr_learning.setFont(font)
        self.__sparql_distr_learning.setObjectName("__sparql_distr_learning")
        self.gridLayout_15.addWidget(self.__sparql_distr_learning, 2, 0, 1, 2)
        self.layoutWidget_6 = QtWidgets.QWidget(self.Problog)
        self.layoutWidget_6.setGeometry(QtCore.QRect(390, 140, 441, 151))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.layoutWidget_6)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.__prob_bgk_label = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__prob_bgk_label.setFont(font)
        self.__prob_bgk_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__prob_bgk_label.setObjectName("__prob_bgk_label")
        self.gridLayout_16.addWidget(self.__prob_bgk_label, 0, 0, 1, 1)
        self.__prop_distr_table = QtWidgets.QTableWidget(self.layoutWidget_6)
        self.__prop_distr_table.setRowCount(1)
        self.__prop_distr_table.setObjectName("__prop_distr_table")
        self.__prop_distr_table.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.__prop_distr_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.__prop_distr_table.setHorizontalHeaderItem(1, item)
        self.__prop_distr_table.horizontalHeader().setDefaultSectionSize(218)
        self.gridLayout_16.addWidget(self.__prop_distr_table, 1, 0, 1, 2)
        self.__distr_learning = QtWidgets.QPushButton(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__distr_learning.setFont(font)
        self.__distr_learning.setObjectName("__distr_learning")
        self.gridLayout_16.addWidget(self.__distr_learning, 2, 0, 1, 2)
        self.__add_distribution = QtWidgets.QPushButton(self.layoutWidget_6)
        self.__add_distribution.setObjectName("__add_distribution")
        self.gridLayout_16.addWidget(self.__add_distribution, 0, 1, 1, 1)
        self.layoutWidget8 = QtWidgets.QWidget(self.Problog)
        self.layoutWidget8.setGeometry(QtCore.QRect(20, 20, 341, 441))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.layoutWidget8)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.__examples_table = QtWidgets.QTableWidget(self.layoutWidget8)
        self.__examples_table.setObjectName("__examples_table")
        self.__examples_table.setColumnCount(2)
        self.__examples_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.__examples_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.__examples_table.setHorizontalHeaderItem(1, item)
        self.gridLayout_11.addWidget(self.__examples_table, 3, 0, 1, 1)
        self.__problog_clauses_label = QtWidgets.QLabel(self.layoutWidget8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__problog_clauses_label.setFont(font)
        self.__problog_clauses_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__problog_clauses_label.setObjectName("__problog_clauses_label")
        self.gridLayout_11.addWidget(self.__problog_clauses_label, 0, 0, 1, 1)
        self.__execute_program = QtWidgets.QPushButton(self.layoutWidget8)
        self.__execute_program.setObjectName("__execute_program")
        self.gridLayout_11.addWidget(self.__execute_program, 4, 0, 1, 1)
        self.__problog_clauses_table = QtWidgets.QTableWidget(self.layoutWidget8)
        self.__problog_clauses_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.__problog_clauses_table.setObjectName("__problog_clauses_table")
        self.__problog_clauses_table.setColumnCount(1)
        self.__problog_clauses_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.__problog_clauses_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.__problog_clauses_table.setHorizontalHeaderItem(1, item)
        self.__problog_clauses_table.horizontalHeader().setCascadingSectionResizes(False)
        self.__problog_clauses_table.horizontalHeader().setDefaultSectionSize(168)
        self.gridLayout_11.addWidget(self.__problog_clauses_table, 1, 0, 1, 1)
        self.__examples_label = QtWidgets.QLabel(self.layoutWidget8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__examples_label.setFont(font)
        self.__examples_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__examples_label.setObjectName("__examples_label")
        self.gridLayout_11.addWidget(self.__examples_label, 2, 0, 1, 1)
        self.layoutWidget9 = QtWidgets.QWidget(self.Problog)
        self.layoutWidget9.setGeometry(QtCore.QRect(390, 20, 211, 105))
        self.layoutWidget9.setObjectName("layoutWidget9")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.layoutWidget9)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.__background_knowledge_label = QtWidgets.QLabel(self.layoutWidget9)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__background_knowledge_label.setFont(font)
        self.__background_knowledge_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__background_knowledge_label.setObjectName("__background_knowledge_label")
        self.gridLayout_12.addWidget(self.__background_knowledge_label, 0, 0, 1, 2)
        self.__bgk_cypher = QtWidgets.QPushButton(self.layoutWidget9)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.__bgk_cypher.setFont(font)
        self.__bgk_cypher.setObjectName("__bgk_cypher")
        self.gridLayout_12.addWidget(self.__bgk_cypher, 1, 0, 1, 2)
        self.__bgk_sparql = QtWidgets.QPushButton(self.layoutWidget9)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.__bgk_sparql.setFont(font)
        self.__bgk_sparql.setObjectName("__bgk_sparql")
        self.gridLayout_12.addWidget(self.__bgk_sparql, 2, 0, 1, 2)
        self.__bgk_file = QtWidgets.QPushButton(self.layoutWidget9)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.__bgk_file.setFont(font)
        self.__bgk_file.setObjectName("__bgk_file")
        self.gridLayout_12.addWidget(self.__bgk_file, 3, 0, 1, 2)
        self.layoutWidget10 = QtWidgets.QWidget(self.Problog)
        self.layoutWidget10.setGeometry(QtCore.QRect(20, 470, 811, 83))
        self.layoutWidget10.setObjectName("layoutWidget10")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.layoutWidget10)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.__beam_size = QtWidgets.QLineEdit(self.layoutWidget10)
        self.__beam_size.setObjectName("__beam_size")
        self.gridLayout_14.addWidget(self.__beam_size, 2, 3, 1, 2)
        self.__length = QtWidgets.QLineEdit(self.layoutWidget10)
        self.__length.setObjectName("__length")
        self.gridLayout_14.addWidget(self.__length, 2, 6, 1, 1)
        self.__mestimate = QtWidgets.QLineEdit(self.layoutWidget10)
        self.__mestimate.setObjectName("__mestimate")
        self.gridLayout_14.addWidget(self.__mestimate, 2, 2, 1, 1)
        self.__mestimate_label = QtWidgets.QLabel(self.layoutWidget10)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__mestimate_label.setFont(font)
        self.__mestimate_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__mestimate_label.setObjectName("__mestimate_label")
        self.gridLayout_14.addWidget(self.__mestimate_label, 1, 2, 1, 1)
        self.__deterministic_combo = QtWidgets.QComboBox(self.layoutWidget10)
        self.__deterministic_combo.setObjectName("__deterministic_combo")
        self.__deterministic_combo.addItem("")
        self.__deterministic_combo.addItem("")
        self.gridLayout_14.addWidget(self.__deterministic_combo, 2, 0, 1, 2)
        self.__deterministic_label = QtWidgets.QLabel(self.layoutWidget10)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__deterministic_label.setFont(font)
        self.__deterministic_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__deterministic_label.setObjectName("__deterministic_label")
        self.gridLayout_14.addWidget(self.__deterministic_label, 1, 0, 1, 2)
        self.__seed = QtWidgets.QLineEdit(self.layoutWidget10)
        self.__seed.setObjectName("__seed")
        self.gridLayout_14.addWidget(self.__seed, 2, 7, 1, 1)
        self.__beam_size_label = QtWidgets.QLabel(self.layoutWidget10)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__beam_size_label.setFont(font)
        self.__beam_size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__beam_size_label.setObjectName("__beam_size_label")
        self.gridLayout_14.addWidget(self.__beam_size_label, 1, 3, 1, 2)
        self.__seed_label = QtWidgets.QLabel(self.layoutWidget10)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__seed_label.setFont(font)
        self.__seed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__seed_label.setObjectName("__seed_label")
        self.gridLayout_14.addWidget(self.__seed_label, 1, 7, 1, 1)
        self.__probfoil_parameters_label = QtWidgets.QLabel(self.layoutWidget10)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.__probfoil_parameters_label.setFont(font)
        self.__probfoil_parameters_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__probfoil_parameters_label.setObjectName("__probfoil_parameters_label")
        self.gridLayout_14.addWidget(self.__probfoil_parameters_label, 0, 0, 1, 10)
        self.__length_label = QtWidgets.QLabel(self.layoutWidget10)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__length_label.setFont(font)
        self.__length_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__length_label.setObjectName("__length_label")
        self.gridLayout_14.addWidget(self.__length_label, 1, 6, 1, 1)
        self.__significance = QtWidgets.QLineEdit(self.layoutWidget10)
        self.__significance.setObjectName("__significance")
        self.gridLayout_14.addWidget(self.__significance, 2, 5, 1, 1)
        self.__significance_label = QtWidgets.QLabel(self.layoutWidget10)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__significance_label.setFont(font)
        self.__significance_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__significance_label.setObjectName("__significance_label")
        self.gridLayout_14.addWidget(self.__significance_label, 1, 5, 1, 1)
        self.__probfoil_execute = QtWidgets.QPushButton(self.layoutWidget10)
        self.__probfoil_execute.setObjectName("__probfoil_execute")
        self.gridLayout_14.addWidget(self.__probfoil_execute, 2, 8, 1, 1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("e6302100-9781-11e9-9e2d-f0b2848a9ad9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.__tabs.addTab(self.Problog, icon2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.__retranslate_ui(MainWindow)
        self.__tabs.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    ## define label text, table headers and other GUI parameters
    # @param: main_window: main_window of the application
    def __retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.__parse_method_label.setText(_translate("MainWindow", "Select parse method"))
        self.__execute_user_query.setText(_translate("MainWindow", "Execute"))
        self.__user_query_label.setText(_translate("MainWindow", "Query"))
        self.__parse_method_combo.setItemText(0, _translate("MainWindow", "parse_props_array"))
        self.__parse_method_combo.setItemText(1, _translate("MainWindow", "parse_node"))
        self.__parse_method_combo.setItemText(2, _translate("MainWindow", "parse_property_map"))
        self.__parse_method_combo.setItemText(3, _translate("MainWindow", "parse_node_rels_with_props"))
        self.__parse_method_combo.setItemText(4, _translate("MainWindow", "parse_node_rels_with_props_map"))
        self.__parse_method_combo.setItemText(5, _translate("MainWindow", "parse_node_rels"))
        self.__parse_method_combo.setItemText(6, _translate("MainWindow", "parse_node_rels_with_props_array"))
        self.__nodes_and_relationships.setText(_translate("MainWindow", "Get all nodes and relationship"))
        self.__relationships_without_properties.setText(
            _translate("MainWindow", "Get all nodes\' relationship without node properties"))
        self.__add_filter.setText(_translate("MainWindow", "Add filter"))
        self.__filter_nodes_label.setText(_translate("MainWindow", "Filter nodes by properties"))
        self.__execute_property_filters_query.setText(_translate("MainWindow", "Execute"))
        item = self.__property_filters_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Property name"))
        item = self.__property_filters_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Property value"))
        self.__closed_round_bracket_first_node.setText(_translate("MainWindow", ")"))
        self.__open_round_bracket_first_node.setText(_translate("MainWindow", "("))
        self.__open_round_bracket_second_node.setText(_translate("MainWindow", "("))
        self.__relationships_between_with_properties.setText(_translate("MainWindow", "With properties"))
        self.__closed_square_bracket.setText(_translate("MainWindow", "]->"))
        self.__relationships_between_without_properties.setText(_translate("MainWindow", "Without properties"))
        self.__open_square_bracket.setText(_translate("MainWindow", "-["))
        self.__close_round_bracket_second_node.setText(_translate("MainWindow", ")"))
        self.__first_node_type_label.setText(_translate("MainWindow", "First node label"))
        self.__second_node_type_label.setText(_translate("MainWindow", "Second node label"))
        self.__execute_label.setText(_translate("MainWindow", "<html><head/><body><p>Execute</p></body></html>"))
        self.__relationship_type_label.setText(_translate("MainWindow", "Relationship"))
        self.__query_results_label.setText(_translate("MainWindow", "QUERY RESULTS"))
        item = self.__triples_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Individual"))
        item = self.__triples_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Property"))
        item = self.__triples_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Value"))
        self.__tabs.setTabText(self.__tabs.indexOf(self.graph_db), _translate("MainWindow", "Graph DB"))
        self.__sparql_user_query_label.setText(_translate("MainWindow", "Query"))
        self.__sparql_execute_user_query.setText(_translate("MainWindow", "Execute"))
        item = self.__sparql_triples_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Individual"))
        item = self.__sparql_triples_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Property"))
        item = self.__sparql_triples_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Value"))
        self.__sparql_query_results_label.setText(_translate("MainWindow", "QUERY RESULTS"))
        self.__sparql_endpoint_label.setText(_translate("MainWindow", "SPARQL endpoint"))
        self.__prefixs_label.setText(_translate("MainWindow", "Specify PREFIXs"))
        self.__sparql_add_prefix.setText(_translate("MainWindow", "Add prefix"))
        item = self.__prefixs_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "URL"))
        item = self.__prefixs_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "alias"))
        self.__sparql_filter_nodes_label.setText(_translate("MainWindow", "Filter nodes by properties"))
        self.__sparql_add_filter.setText(_translate("MainWindow", "Add filter"))
        self.__sparql_execute_property_filters_query.setText(_translate("MainWindow", "Execute"))
        item = self.__sparql_property_filters_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "property name"))
        item = self.__sparql_property_filters_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "property value"))
        self.__tabs.setTabText(self.__tabs.indexOf(self.sparql), _translate("MainWindow", "SPARQL endpoint"))
        self.__evidence_label.setText(_translate("MainWindow", "Evidences"))
        self.__evidence_cypher.setText(_translate("MainWindow", "Add cypher result "))
        self.__evidence_sparql.setText(_translate("MainWindow", "Add SPARQL result "))
        self.__evidence_file.setText(_translate("MainWindow", "Load from file"))
        self.__sparql_prob_bgk_label.setText(_translate("MainWindow", "Learn probabilities on SPARQL results,\n"
                                                                      " and use them as background knowledge"))
        self.__sparql_add_distribution.setText(_translate("MainWindow", "Add distribution"))
        item = self.__sparql_prop_distr_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "property"))
        item = self.__sparql_prop_distr_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "distribution to learn"))
        self.__sparql_distr_learning.setText(_translate("MainWindow", "Execute"))
        self.__prob_bgk_label.setText(_translate("MainWindow", "Learn probabilities on cypher results,\n"
                                                               " and use them as background knowledge"))
        item = self.__prop_distr_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "property"))
        item = self.__prop_distr_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "distribution to learn"))
        self.__distr_learning.setText(_translate("MainWindow", "Execute"))
        self.__add_distribution.setText(_translate("MainWindow", "Add distribution"))
        item = self.__examples_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Property"))
        item = self.__examples_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Truth"))
        self.__problog_clauses_label.setText(_translate("MainWindow", "Problog clauses"))
        self.__execute_program.setText(_translate("MainWindow", "Execute program"))
        item = self.__problog_clauses_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Clause"))
        self.__examples_label.setText(_translate("MainWindow", "Examples"))
        self.__background_knowledge_label.setText(_translate("MainWindow", "Background knowledge"))
        self.__bgk_cypher.setText(_translate("MainWindow", "Add cypher result "))
        self.__bgk_sparql.setText(_translate("MainWindow", "Add SPARQL result "))
        self.__bgk_file.setText(_translate("MainWindow", "Load from file"))
        self.__mestimate_label.setText(_translate("MainWindow", "m-estimate"))
        self.__deterministic_combo.setItemText(0, _translate("MainWindow", "deterministic rules"))
        self.__deterministic_combo.setItemText(1, _translate("MainWindow", "non deterministic rules"))
        self.__deterministic_label.setText(_translate("MainWindow", " learn deterministic rules "))
        self.__beam_size_label.setText(_translate("MainWindow", "beam size"))
        self.__seed_label.setText(_translate("MainWindow", "seed"))
        self.__probfoil_parameters_label.setText(_translate("MainWindow", "Probfoil parameters"))
        self.__length_label.setText(_translate("MainWindow", "length"))
        self.__significance_label.setText(_translate("MainWindow", "significance"))
        self.__probfoil_execute.setText(_translate("MainWindow", "Execute and \n"
                                                                 "save to file"))
        self.__tabs.setTabText(self.__tabs.indexOf(self.Problog), _translate("MainWindow", "Problog"))

    ## initialize (add first row, set measures) to some GUI tables
    def initialize_tables(self):
        property_name = QtWidgets.QLineEdit(self.layoutWidget)
        property_value = QtWidgets.QLineEdit(self.layoutWidget)

        self.__property_filters_table.setCellWidget(0, 0, property_name)
        self.__property_filters_table.setCellWidget(0, 1, property_value)

        property_name = QtWidgets.QLineEdit(self.layoutWidget)
        property_value = QtWidgets.QLineEdit(self.layoutWidget)

        self.__sparql_property_filters_table.setCellWidget(0, 0, property_name)
        self.__sparql_property_filters_table.setCellWidget(0, 1, property_value)

        url = QtWidgets.QLineEdit(self.layoutWidget)
        alias = QtWidgets.QLineEdit(self.layoutWidget)

        self.__prefixs_table.setCellWidget(0, 0, url)
        self.__prefixs_table.setCellWidget(0, 1, alias)

        property = QtWidgets.QLineEdit(self.layoutWidget)
        distribution = QtWidgets.QComboBox(self.layoutWidget)
        distribution.addItem("Normal")
        distribution.addItem("Multinomial")
        distribution.addItem("Interspersed")

        self.__prop_distr_table.setCellWidget(0, 0, property)
        self.__prop_distr_table.setCellWidget(0, 1, distribution)

        property = QtWidgets.QLineEdit(self.layoutWidget)
        distribution = QtWidgets.QComboBox(self.layoutWidget)
        distribution.addItem("Normal")
        distribution.addItem("Multinomial")
        distribution.addItem("Interspersed")

        self.__sparql_prop_distr_table.setCellWidget(0, 0, property)
        self.__sparql_prop_distr_table.setCellWidget(0, 1, distribution)

        self.__problog_clauses_table.setColumnWidth(0, 340)

        self.__examples_table.setColumnWidth(0, 168)
        self.__examples_table.setColumnWidth(1, 168)

    ## define method to call when buttons are clicked
    def setup_signals(self):
        self.__execute_user_query.clicked.connect(
            lambda: self.execute_user_query())

        self.__add_filter.clicked.connect(
            lambda: self.add_filter(self.__property_filters_table))

        self.__sparql_add_filter.clicked.connect(
            lambda: self.add_filter(self.__sparql_property_filters_table))

        self.__nodes_and_relationships.clicked.connect(
            lambda: self.nodes_and_relationships())

        self.__relationships_without_properties.clicked.connect(
            lambda: self.relationships_without_properties())

        self.__relationships_between_with_properties.clicked.connect(
            lambda: self.relationships_between_with_properties())

        self.__relationships_between_without_properties.clicked.connect(
            lambda: self.relationships_between_without_properties())

        self.__execute_property_filters_query.clicked.connect(
            lambda: self.execute_property_filters_query())

        self.__sparql_execute_user_query.clicked.connect(
            lambda: self.sparql_execute_user_query())

        self.__sparql_execute_property_filters_query.clicked.connect(
            lambda: self.sparql_execute_property_filters_query())

        self.__sparql_add_prefix.clicked.connect(
            lambda: self.add_filter(self.__prefixs_table))

        self.__add_distribution.clicked.connect(
            lambda: self.add_distribution(self.__prop_distr_table))

        self.__sparql_add_distribution.clicked.connect(
            lambda: self.add_distribution(self.__sparql_prop_distr_table))

        self.__bgk_cypher.clicked.connect(
            lambda: self.bgk_cypher())

        self.__bgk_sparql.clicked.connect(
            lambda: self.bgk_sparql())

        self.__bgk_file.clicked.connect(
            lambda: self.bgk_file())

        self.__evidence_cypher.clicked.connect(
            lambda: self.evidence_cypher())

        self.__evidence_sparql.clicked.connect(
            lambda: self.evidence_sparql())

        self.__evidence_file.clicked.connect(
            lambda: self.evidence_file())

        self.__distr_learning.clicked.connect(
            lambda: self.distr_learning())

    ## method related to __bgk_sparql, add sparql query results as background knowledge
    def bgk_sparql(self):
        problog_program = self.__sparql_data.parse(self.__problog_program)
        self.write_clauses(problog_program)

    ## method related to __bgk_cypher, add cypher query results as background knowledge
    def bgk_cypher(self):
        problog_program = self.__cypher_data.parse(self.__problog_program)
        self.write_clauses(problog_program)

    ## method related to __bgk_file, add file clauses as background knowledge
    def bgk_file(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', "D:", "All Files (*);;Prolog files (*.pl);;Text files (*.txt)")

        problog_program = PrologFile(file_name)
        self.write_clauses(problog_program)
        programs_merge(self.__problog_program, problog_program)

    ## method related to __evidence_cypher, add cypher query results as training examples
    def evidence_cypher(self):
        examples = self.__cypher_data.to_examples(self.__examples)
        self.write_examples(examples)

    ## method related to __evidence_sparql, add sparql query results as training examples
    def evidence_sparql(self):
        examples = self.__sparql_data.to_examples(self.__examples)
        self.write_examples(examples)

    ## method related to __evidence_file, add file with evidence clauses as training examples
    def evidence_file(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', "D:", "All Files (*);;Prolog files (*.pl);;Text files (*.txt)")

        examples = list(read_examples(file_name))
        self.write_examples(examples)
        self.__examples.extend(examples)

    ## method related to __distr_learning, learn proeprty values distributions and use annotated clauses as background knowkledge
    def distr_learning(self):
        property_map = PropertyMap()

        for i in range(0, self.__prop_distr_table.rowCount()):
            distr = self.__prop_distr_table.cellWidget(i, 1).currentText()
            if self.__prop_distr_table.cellWidget(i, 0).text() == "":
                continue
            if distr == "Normal":
                distr_obj = Normal()
            elif distr == "Interspersed":
                distr_obj = Interspersed()
            else:
                distr_obj = Multinomial()

            property_map[self.__prop_distr_table.cellWidget(i, 0).text()] = Property(self.__prop_distr_table.cellWidget(i, 0).text(), distr_obj)

        property_map = self.__cypher_data.learn_distributions(property_map)
        problog_program = property_map.to_simple_program()
        self.write_clauses(problog_program)
        programs_merge(self.__problog_program, problog_program)

    ## method related to __execute_user_query button
    def execute_user_query(self):
        dbms_query = DbmsQuery(self.__user_query.text(), self.__parse_method_combo.currentText())
        self.__cypher_data = dbms_query.run_query()
        write_results(self.__triples_table, self.__cypher_data)

    ## method related to __add_filter or sparql_add_filer, add a row in a filter table
    # @param: table: in which table the filter should be added
    def add_filter(self, table):
        row_count = table.rowCount()
        table.insertRow(row_count)

        property_name = QtWidgets.QLineEdit(self.layoutWidget)
        property_value = QtWidgets.QLineEdit(self.layoutWidget)

        table.setCellWidget(row_count, 0, property_name)
        table.setCellWidget(row_count, 1, property_value)

    ## method related to __add_filter or sparql_add_filer, add a row in a distribution table
    # @param: table: in which table the distribution should be added
    def add_distribution(self, table):
        row_count = table.rowCount()
        table.insertRow(row_count)

        property = QtWidgets.QLineEdit(self.layoutWidget)
        distribution = QtWidgets.QComboBox(self.layoutWidget)
        distribution.addItem("Normal")
        distribution.addItem("Multinomial")
        distribution.addItem("Interspersed")

        table.setCellWidget(row_count, 0, property)
        table.setCellWidget(row_count, 1, distribution)

    ## method related to __nodes_and_relationships, execute cypher query that retrieves all nodes (with properties) and relationships between them
    def nodes_and_relationships(self):
        dbms_query = DbmsQuery(
            "MATCH (n) OPTIONAL MATCH (n)-[r]-(m) RETURN ID(n), properties(n), TYPE(r), ID(m), properties(m)",
            "parse_node_rels_with_props_map")
        self.__cypher_data = dbms_query.run_query()
        write_results(self.__triples_table, self.__cypher_data)

    ## method related to __relationships_without_properties, execute cypher query that retrieves all relationships between nodes
    def relationships_without_properties(self):
        dbms_query = DbmsQuery("MATCH (n)-[r]-(m) RETURN ID(n), TYPE(r), ID(m)", "parse_node_rels")
        self.__cypher_data = dbms_query.run_query()
        write_results(self.__triples_table, self.__cypher_data)

    ## add : before filter for non empty filters
    def __add_dots_to_filter(self):
        first_node_label_text = ""
        second_node_label_text = ""
        relationship_text = ""

        if self.__first_node_type.text() != "":
            first_node_label_text = ":" + self.__first_node_type.text()

        if self.__second_node_type.text() != "":
            second_node_label_text = ":" + self.__second_node_type.text()

        if self.__relationship_type.text() != "":
            relationship_text = ":" + self.__relationship_type.text()

        return first_node_label_text, second_node_label_text, relationship_text

    ## method related to __relationships_between_with_properties
    ## retrieves relationships, eventually of a specified type, between nodes, eventually of a specified type (both for first and second node); also node properties are retrieved
    def relationships_between_with_properties(self):
        first_node_label_text, second_node_label_text, relationship_text = self.__add_dots_to_filter()
        dbms_query = DbmsQuery(
            "MATCH (n" + first_node_label_text + ")-[r" + relationship_text + "]-(m" + second_node_label_text + ") RETURN ID(n), properties(n), TYPE(r), ID(m), properties(m)",
            "parse_node_rels_with_props_map")

        self.__cypher_data = dbms_query.run_query()
        write_results(self.__triples_table, self.__cypher_data)

    ## method related to __relationships_between_without_properties
    ## relationships, eventually of a specified type, between nodes, eventually of a specified type (both for first and second node); ndoe properties are not retrieved
    def relationships_between_without_properties(self):
        first_node_label_text, second_node_label_text, relationship_text = self.__add_dots_to_filter()

        dbms_query = DbmsQuery(
            "MATCH (n" + first_node_label_text + ")-[r" + relationship_text + "]-(m" + second_node_label_text + ") RETURN ID(n), TYPE(r), ID(m)",
            "parse_node_rels")
        self.__cypher_data = dbms_query.run_query()
        write_results(self.__triples_table, self.__cypher_data)

    ## method related to __execute_property_filters_query
    ## all nodes that have the specified values for the specified properties, retrieves all nodes if nothing is specified
    def execute_property_filters_query(self):
        query = "MATCH(n) "
        query_where = " AND ".join(
            [(("n." + self.__property_filters_table.cellWidget(i, 0).text() + "=" +
               (str(self.__property_filters_table.cellWidget(i, 1).text())
                if self.__property_filters_table.cellWidget(i, 1).text().isdecimal() else ("'" + self.__property_filters_table.cellWidget(i, 1).text()) + "'"))
              if self.__property_filters_table.cellWidget(i, 0).text() != "" and self.__property_filters_table.cellWidget(i, 1).text() != "" else '')
             for i in range(0, self.__property_filters_table.rowCount())])

        if query_where != "":
            query += "WHERE " + query_where
        query += " RETURN ID(n), properties(n)"

        dbms_query = DbmsQuery(query, "parse_property_map")
        self.__cypher_data = dbms_query.run_query()
        write_results(self.__triples_table, self.__cypher_data)

    ## method related to __sparql_execute_user_query
    def sparql_execute_user_query(self):
        cloud_query = CloudQuery(self.__sparql_user_query.text(), self.__sparql_endpoint.text())
        self.__sparql_data = cloud_query.run_query()
        write_results(self.__sparql_triples_table, self.__sparql_data)

    ## method related to __sparql_execute_property_filters_query
    ## all nodes that have the specified values for the specified properties,
    ## if a prefix is used in a property name or a property value that prefix should be specified in the prefix table
    def sparql_execute_property_filters_query(self):
        query = "\n".join(
            [("PREFIX " + self.__prefixs_table.cellWidget(i, 1).text() + ': <' + self.__prefixs_table.cellWidget(i,
                                                                                                                 0).text() + '>'
              if self.__prefixs_table.cellWidget(i, 0).text() != "" and self.__prefixs_table.cellWidget(i,
                                                                                                        1).text() != "" else '')
             for i in range(0, self.__prefixs_table.rowCount())])

        query += "\nSELECT * "
        query_where = " . ".join(
            [("?subject " + self.__sparql_property_filters_table.cellWidget(i, 0).text() + " " + str(
                self.__sparql_property_filters_table.cellWidget(i, 1).text())
              if self.__sparql_property_filters_table.cellWidget(i, 0).text() != "" and self.__sparql_property_filters_table.cellWidget(i, 1).text() != "" else '')
             for i in range(0, self.__sparql_property_filters_table.rowCount())])

        if query_where != "":
            query += "WHERE {" + query_where + ". }"

        cloud_query = CloudQuery(query, self.__sparql_endpoint.text())

        self.__sparql_data = cloud_query.run_query()
        write_results(self.__triples_table, self.__sparql_data)

    ## show problog program clauses in table
    def write_clauses(self, program):
        for clause in program:
            row_count = self.__problog_clauses_table.rowCount()
            self.__problog_clauses_table.insertRow(row_count)
            self.__problog_clauses_table.setItem(row_count, 0, QTableWidgetItem(str(clause)))

    ## show examples in table
    def write_examples(self, examples):
        for possible_world in examples:
            splitter = "------------------------------"
            row_count = self.__examples_table.rowCount()
            self.__examples_table.insertRow(row_count)
            self.__examples_table.setItem(row_count, 0, QTableWidgetItem(splitter))
            self.__examples_table.setItem(row_count, 1, QTableWidgetItem(splitter))
            for example in possible_world:
                row_count = self.__examples_table.rowCount()
                self.__examples_table.insertRow(row_count)
                self.__examples_table.setItem(row_count, 0, QTableWidgetItem(str(example[0])))
                self.__examples_table.setItem(row_count, 1, QTableWidgetItem(str(example[1])))


## function to write triples in a specified three column table
# @param: table: in which table the triples should be added
# @param: triples: triples to add
def write_results(table, data_obj):
    table.setRowCount(0)
    for possible_world in data_obj.get_data():
        splitter = "----------------------"
        row_count = table.rowCount()
        table.insertRow(row_count)
        table.setItem(row_count, 0, QTableWidgetItem(splitter))
        table.setItem(row_count, 1, QTableWidgetItem(splitter))
        table.setItem(row_count, 2, QTableWidgetItem(splitter))
        for triple in possible_world:
            row_count = table.rowCount()
            table.insertRow(row_count)
            table.setItem(row_count, 0, QTableWidgetItem(str(triple[0])))
            table.setItem(row_count, 1, QTableWidgetItem(str(triple[1])))
            table.setItem(row_count, 2, QTableWidgetItem(str(triple[2])))


def programs_merge(first_program, second_program):
    for clause in second_program:
        first_program += clause


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow(MainWindow)
    ui.initialize_tables()
    ui.setup_signals()
    MainWindow.show()
    sys.exit(app.exec_())
