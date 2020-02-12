# -*- coding: utf-8 -*-
# @package Data
# application frontend
# @author Pasquale De Marinis, Barile Roberto, Caputo Sergio

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from src.Query import DbmsQuery
from src.Query import CloudQuery


##
# Implements a class for GUI representation and operations' execution
class UiMainWindow(object):
    ## constructor
    # @param: main_window: main_window of the application
    def __init__(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(892, 566)
        self.__centralwidget = QtWidgets.QWidget(main_window)
        self.__centralwidget.setObjectName("centralwidget")
        self.__tabs = QtWidgets.QTabWidget(self.__centralwidget)
        self.__tabs.setGeometry(QtCore.QRect(20, 20, 851, 511))
        self.__tabs.setObjectName("tabs")
        self.__graph_db = QtWidgets.QWidget()
        self.__graph_db.setObjectName("graph_db")
        self.__layoutWidget = QtWidgets.QWidget(self.__graph_db)
        self.__layoutWidget.setGeometry(QtCore.QRect(20, 20, 801, 59))
        self.__layoutWidget.setObjectName("layoutWidget")
        self.__gridLayout = QtWidgets.QGridLayout(self.__layoutWidget)
        self.__gridLayout.setContentsMargins(0, 0, 0, 0)
        self.__gridLayout.setObjectName("gridLayout")
        self.__parse_method_label = QtWidgets.QLabel(self.__layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__parse_method_label.setFont(font)
        self.__parse_method_label.setObjectName("parse_method_label")
        self.__gridLayout.addWidget(self.__parse_method_label, 1, 0, 1, 1)
        self.__execute_user_query = QtWidgets.QPushButton(self.__layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__execute_user_query.setFont(font)
        self.__execute_user_query.setObjectName("execute_user_query")
        self.__gridLayout.addWidget(self.__execute_user_query, 0, 3, 1, 1)
        self.__user_query_label = QtWidgets.QLabel(self.__layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__user_query_label.setFont(font)
        self.__user_query_label.setObjectName("user_query_label")
        self.__gridLayout.addWidget(self.__user_query_label, 0, 0, 1, 1)
        self.__parse_method_combo = QtWidgets.QComboBox(self.__layoutWidget)
        self.__parse_method_combo.setObjectName("parse_method_combo")
        self.__parse_method_combo.addItem("")
        self.__parse_method_combo.addItem("")
        self.__parse_method_combo.addItem("")
        self.__parse_method_combo.addItem("")
        self.__parse_method_combo.addItem("")
        self.__parse_method_combo.addItem("")
        self.__parse_method_combo.addItem("")
        self.__gridLayout.addWidget(self.__parse_method_combo, 1, 1, 1, 1)
        self.__user_query = QtWidgets.QLineEdit(self.__layoutWidget)
        self.__user_query.setObjectName("user_query")
        self.__gridLayout.addWidget(self.__user_query, 0, 1, 1, 2)
        self.__layoutWidget1 = QtWidgets.QWidget(self.__graph_db)
        self.__layoutWidget1.setGeometry(QtCore.QRect(20, 220, 801, 29))
        self.__layoutWidget1.setObjectName("layoutWidget1")
        self.__gridLayout_2 = QtWidgets.QGridLayout(self.__layoutWidget1)
        self.__gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.__gridLayout_2.setObjectName("gridLayout_2")
        self.__nodes_and_relationships = QtWidgets.QPushButton(self.__layoutWidget1)
        self.__nodes_and_relationships.setObjectName("nodes_and_relationships")
        self.__gridLayout_2.addWidget(self.__nodes_and_relationships, 0, 0, 1, 1)
        self.__relationships_without_properties = QtWidgets.QPushButton(self.__layoutWidget1)
        self.__relationships_without_properties.setObjectName("relationships_without_properties")
        self.__gridLayout_2.addWidget(self.__relationships_without_properties, 0, 1, 1, 1)
        self.__layoutWidget2 = QtWidgets.QWidget(self.__graph_db)
        self.__layoutWidget2.setGeometry(QtCore.QRect(20, 292, 391, 171))
        self.__layoutWidget2.setObjectName("layoutWidget2")
        self.__gridLayout_4 = QtWidgets.QGridLayout(self.__layoutWidget2)
        self.__gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.__gridLayout_4.setObjectName("gridLayout_4")
        self.__add_filter = QtWidgets.QPushButton(self.__layoutWidget2)
        self.__add_filter.setObjectName("add_filter")
        self.__gridLayout_4.addWidget(self.__add_filter, 0, 1, 1, 1)
        self.__filter_nodes_label = QtWidgets.QLabel(self.__layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.__filter_nodes_label.setFont(font)
        self.__filter_nodes_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__filter_nodes_label.setObjectName("filter_nodes_label")
        self.__gridLayout_4.addWidget(self.__filter_nodes_label, 0, 0, 1, 1)
        self.__execute_property_filters_query = QtWidgets.QPushButton(self.__layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__execute_property_filters_query.setFont(font)
        self.__execute_property_filters_query.setObjectName("execute_property_filters_query")
        self.__gridLayout_4.addWidget(self.__execute_property_filters_query, 3, 0, 1, 2)
        self.__property_filters_table = QtWidgets.QTableWidget(self.__layoutWidget2)
        self.__property_filters_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.__property_filters_table.setObjectName("property_filters_table")
        self.__property_filters_table.setColumnCount(2)
        self.__property_filters_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.__property_filters_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.__property_filters_table.setHorizontalHeaderItem(1, item)
        self.__property_filters_table.horizontalHeader().setDefaultSectionSize(194)
        self.__gridLayout_4.addWidget(self.__property_filters_table, 1, 0, 1, 2)
        self.__line = QtWidgets.QFrame(self.__graph_db)
        self.__line.setGeometry(QtCore.QRect(-60, 90, 911, 20))
        self.__line.setFrameShape(QtWidgets.QFrame.HLine)
        self.__line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.__line.setObjectName("line")
        self.__line_2 = QtWidgets.QFrame(self.__graph_db)
        self.__line_2.setGeometry(QtCore.QRect(0, 190, 851, 16))
        self.__line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.__line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.__line_2.setObjectName("line_2")
        self.__line_3 = QtWidgets.QFrame(self.__graph_db)
        self.__line_3.setGeometry(QtCore.QRect(-10, 260, 851, 16))
        self.__line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.__line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.__line_3.setObjectName("line_3")
        self.__line_4 = QtWidgets.QFrame(self.__graph_db)
        self.__line_4.setGeometry(QtCore.QRect(425, 270, 20, 221))
        self.__line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.__line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.__line_4.setObjectName("line_4")
        self.__layoutWidget_4 = QtWidgets.QWidget(self.__graph_db)
        self.__layoutWidget_4.setGeometry(QtCore.QRect(20, 120, 801, 52))
        self.__layoutWidget_4.setObjectName("layoutWidget_4")
        self.__gridLayout_3 = QtWidgets.QGridLayout(self.__layoutWidget_4)
        self.__gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.__gridLayout_3.setObjectName("gridLayout_3")
        self.__closed_round_bracket_first_node = QtWidgets.QLabel(self.__layoutWidget_4)
        self.__closed_round_bracket_first_node.setObjectName("closed_round_bracket_first_node")
        self.__gridLayout_3.addWidget(self.__closed_round_bracket_first_node, 1, 3, 1, 1)
        self.__open_round_bracket_first_node = QtWidgets.QLabel(self.__layoutWidget_4)
        self.__open_round_bracket_first_node.setObjectName("open_round_bracket_first_node")
        self.__gridLayout_3.addWidget(self.__open_round_bracket_first_node, 1, 1, 1, 1)
        self.__open_round_bracket_second_node = QtWidgets.QLabel(self.__layoutWidget_4)
        self.__open_round_bracket_second_node.setObjectName("open_round_bracket_second_node")
        self.__gridLayout_3.addWidget(self.__open_round_bracket_second_node, 1, 7, 1, 1)
        self.__second_node_type = QtWidgets.QLineEdit(self.__layoutWidget_4)
        self.__second_node_type.setObjectName("second_node__type")
        self.__gridLayout_3.addWidget(self.__second_node_type, 1, 8, 1, 1)
        self.__relationships_between_with_properties = QtWidgets.QPushButton(self.__layoutWidget_4)
        self.__relationships_between_with_properties.setObjectName("relationships_between_with_properties")
        self.__gridLayout_3.addWidget(self.__relationships_between_with_properties, 1, 10, 1, 1)
        self.__relationship_type = QtWidgets.QLineEdit(self.__layoutWidget_4)
        self.__relationship_type.setObjectName("relationship_type")
        self.__gridLayout_3.addWidget(self.__relationship_type, 1, 5, 1, 1)
        self.__closed_square_bracket = QtWidgets.QLabel(self.__layoutWidget_4)
        self.__closed_square_bracket.setObjectName("closed_square_bracket")
        self.__gridLayout_3.addWidget(self.__closed_square_bracket, 1, 6, 1, 1)
        self.__first_node_type = QtWidgets.QLineEdit(self.__layoutWidget_4)
        self.__first_node_type.setObjectName("first_node_type")
        self.__gridLayout_3.addWidget(self.__first_node_type, 1, 2, 1, 1)
        self.__label_2 = QtWidgets.QLabel(self.__layoutWidget_4)
        self.__label_2.setText("")
        self.__label_2.setObjectName("label_2")
        self.__gridLayout_3.addWidget(self.__label_2, 1, 0, 1, 1)
        self.__relationships_between_without_properties = QtWidgets.QPushButton(self.__layoutWidget_4)
        self.__relationships_between_without_properties.setObjectName("relationships_between_without_properties")
        self.__gridLayout_3.addWidget(self.__relationships_between_without_properties, 1, 11, 1, 1)
        self.__open_square_bracket = QtWidgets.QLabel(self.__layoutWidget_4)
        self.__open_square_bracket.setObjectName("open_square_bracket")
        self.__gridLayout_3.addWidget(self.__open_square_bracket, 1, 4, 1, 1)
        self.__close_round_bracket_second_node = QtWidgets.QLabel(self.__layoutWidget_4)
        self.__close_round_bracket_second_node.setObjectName("close_round_bracket_second_node")
        self.__gridLayout_3.addWidget(self.__close_round_bracket_second_node, 1, 9, 1, 1)
        self.__first_node_type_label = QtWidgets.QLabel(self.__layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__first_node_type_label.setFont(font)
        self.__first_node_type_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__first_node_type_label.setObjectName("first_node_type_label")
        self.__gridLayout_3.addWidget(self.__first_node_type_label, 0, 2, 1, 1)
        self.__second_node_type_label = QtWidgets.QLabel(self.__layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__second_node_type_label.setFont(font)
        self.__second_node_type_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__second_node_type_label.setObjectName("second_node_type_label")
        self.__gridLayout_3.addWidget(self.__second_node_type_label, 0, 8, 1, 1)
        self.__execute_label = QtWidgets.QLabel(self.__layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.__execute_label.setFont(font)
        self.__execute_label.setStyleSheet("")
        self.__execute_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__execute_label.setObjectName("execute_label")
        self.__gridLayout_3.addWidget(self.__execute_label, 0, 10, 1, 2)
        self.__relationship_type_label = QtWidgets.QLabel(self.__layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__relationship_type_label.setFont(font)
        self.__relationship_type_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__relationship_type_label.setObjectName("reationship_type_label")
        self.__gridLayout_3.addWidget(self.__relationship_type_label, 0, 5, 1, 1)
        self.__layoutWidget3 = QtWidgets.QWidget(self.__graph_db)
        self.__layoutWidget3.setGeometry(QtCore.QRect(460, 290, 361, 171))
        self.__layoutWidget3.setObjectName("layoutWidget3")
        self.__gridLayout_7 = QtWidgets.QGridLayout(self.__layoutWidget3)
        self.__gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.__gridLayout_7.setObjectName("gridLayout_7")
        self.__query_results_label = QtWidgets.QLabel(self.__layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.__query_results_label.setFont(font)
        self.__query_results_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__query_results_label.setObjectName("query_results_label")
        self.__gridLayout_7.addWidget(self.__query_results_label, 0, 0, 1, 1)
        self.__triples_table = QtWidgets.QTableWidget(self.__layoutWidget3)
        self.__triples_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.__triples_table.setObjectName("triples_table")
        self.__triples_table.setColumnCount(3)
        self.__triples_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.__triples_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.__triples_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.__triples_table.setHorizontalHeaderItem(2, item)
        self.__triples_table.horizontalHeader().setDefaultSectionSize(119)
        self.__gridLayout_7.addWidget(self.__triples_table, 1, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/neo4j-database-meta-image-removebg-preview.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.__tabs.addTab(self.__graph_db, icon, "")
        self.__sparql = QtWidgets.QWidget()
        self.__sparql.setObjectName("sparql")
        self.__layoutWidget4 = QtWidgets.QWidget(self.__sparql)
        self.__layoutWidget4.setGeometry(QtCore.QRect(20, 60, 801, 27))
        self.__layoutWidget4.setObjectName("layoutWidget4")
        self.__gridLayout_5 = QtWidgets.QGridLayout(self.__layoutWidget4)
        self.__gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.__gridLayout_5.setObjectName("gridLayout_5")
        self.__sparql_user_query_label = QtWidgets.QLabel(self.__layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__sparql_user_query_label.setFont(font)
        self.__sparql_user_query_label.setObjectName("sparql_user_query_label")
        self.__gridLayout_5.addWidget(self.__sparql_user_query_label, 0, 0, 1, 1)
        self.__sparql_user_query = QtWidgets.QLineEdit(self.__layoutWidget4)
        self.__sparql_user_query.setObjectName("sparql_user_query")
        self.__gridLayout_5.addWidget(self.__sparql_user_query, 0, 1, 1, 1)
        self.__sparql_execute_user_query = QtWidgets.QPushButton(self.__layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__sparql_execute_user_query.setFont(font)
        self.__sparql_execute_user_query.setObjectName("sparql_execute_user_query")
        self.__gridLayout_5.addWidget(self.__sparql_execute_user_query, 0, 2, 1, 1)
        self.__layoutWidget_3 = QtWidgets.QWidget(self.__sparql)
        self.__layoutWidget_3.setGeometry(QtCore.QRect(20, 330, 801, 131))
        self.__layoutWidget_3.setObjectName("layoutWidget_3")
        self.__gridLayout_8 = QtWidgets.QGridLayout(self.__layoutWidget_3)
        self.__gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.__gridLayout_8.setObjectName("gridLayout_8")
        self.__sparql_query_results_label = QtWidgets.QLabel(self.__layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.__sparql_query_results_label.setFont(font)
        self.__sparql_query_results_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__sparql_query_results_label.setObjectName("sparql_query_results_label")
        self.__gridLayout_8.addWidget(self.__sparql_query_results_label, 0, 0, 1, 1)
        self.__sparql_triples_table = QtWidgets.QTableWidget(self.__layoutWidget_3)
        self.__sparql_triples_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.__sparql_triples_table.setObjectName("sparql_triples_table")
        self.__sparql_triples_table.setColumnCount(3)
        self.__sparql_triples_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.__sparql_triples_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.__sparql_triples_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.__sparql_triples_table.setHorizontalHeaderItem(2, item)
        self.__sparql_triples_table.horizontalHeader().setDefaultSectionSize(266)
        self.__gridLayout_8.addWidget(self.__sparql_triples_table, 1, 0, 1, 1)
        self.__layoutWidget_2 = QtWidgets.QWidget(self.__sparql)
        self.__layoutWidget_2.setGeometry(QtCore.QRect(20, 140, 801, 136))
        self.__layoutWidget_2.setObjectName("layoutWidget_2")
        self.__gridLayout_6 = QtWidgets.QGridLayout(self.__layoutWidget_2)
        self.__gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.__gridLayout_6.setObjectName("gridLayout_6")
        self.__sparql_add_filter = QtWidgets.QPushButton(self.__layoutWidget_2)
        self.__sparql_add_filter.setObjectName("sparql_add_filter")
        self.__gridLayout_6.addWidget(self.__sparql_add_filter, 0, 1, 1, 1)
        self.__sparql_filter_nodes_label = QtWidgets.QLabel(self.__layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.__sparql_filter_nodes_label.setFont(font)
        self.__sparql_filter_nodes_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__sparql_filter_nodes_label.setObjectName("sparql_filter_nodes_label")
        self.__gridLayout_6.addWidget(self.__sparql_filter_nodes_label, 0, 0, 1, 1)
        self.__sparql_property_filters_table = QtWidgets.QTableWidget(self.__layoutWidget_2)
        self.__sparql_property_filters_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.__sparql_property_filters_table.setObjectName("sparql_property_filters_table")
        self.__sparql_property_filters_table.setColumnCount(2)
        self.__sparql_property_filters_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.__sparql_property_filters_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.__sparql_property_filters_table.setHorizontalHeaderItem(1, item)
        self.__sparql_property_filters_table.horizontalHeader().setDefaultSectionSize(399)
        self.__gridLayout_6.addWidget(self.__sparql_property_filters_table, 1, 0, 1, 2)
        self.__sparql_execute_property_filters_query = QtWidgets.QPushButton(self.__layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__sparql_execute_property_filters_query.setFont(font)
        self.__sparql_execute_property_filters_query.setObjectName("__sparql_execute_property_filters_query")
        self.__gridLayout_6.addWidget(self.__sparql_execute_property_filters_query, 2, 0, 1, 2)
        self.__line_5 = QtWidgets.QFrame(self.__sparql)
        self.__line_5.setGeometry(QtCore.QRect(0, 100, 851, 20))
        self.__line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.__line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.__line_5.setObjectName("line_5")
        self.__line_6 = QtWidgets.QFrame(self.__sparql)
        self.__line_6.setGeometry(QtCore.QRect(-30, 290, 891, 20))
        self.__line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.__line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.__line_6.setObjectName("line_6")
        self.__widget = QtWidgets.QWidget(self.__sparql)
        self.__widget.setGeometry(QtCore.QRect(20, 20, 801, 27))
        self.__widget.setObjectName("widget")
        self.__gridLayout_9 = QtWidgets.QGridLayout(self.__widget)
        self.__gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.__gridLayout_9.setObjectName("gridLayout_9")
        self.__sparql_endpoint = QtWidgets.QLineEdit(self.__widget)
        self.__sparql_endpoint.setObjectName("sparql_endpoint")
        self.__gridLayout_9.addWidget(self.__sparql_endpoint, 0, 1, 1, 1)
        self.__sparql_endpoint_label = QtWidgets.QLabel(self.__widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.__sparql_endpoint_label.setFont(font)
        self.__sparql_endpoint_label.setObjectName("sparql_endpoint_label")
        self.__gridLayout_9.addWidget(self.__sparql_endpoint_label, 0, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../resources/sparql-blog-1-removebg-preview.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.__tabs.addTab(self.__sparql, icon1, "")
        main_window.setCentralWidget(self.__centralwidget)
        self.__statusbar = QtWidgets.QStatusBar(main_window)
        self.__statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.__statusbar)

        self.__retranslate_ui(main_window)
        self.__tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    ## define label text, table headers and other GUI parameters
    # @param: main_window: main_window of the application
    def __retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "main_window"))
        self.__parse_method_label.setText(_translate("main_window", "Select parse method"))
        self.__execute_user_query.setText(_translate("main_window", "Execute"))
        self.__user_query_label.setText(_translate("main_window", "Query"))
        self.__parse_method_combo.setItemText(0, _translate("main_window", "parse_props_array"))
        self.__parse_method_combo.setItemText(1, _translate("main_window", "parse_node"))
        self.__parse_method_combo.setItemText(2, _translate("main_window", "parse_property_map"))
        self.__parse_method_combo.setItemText(3, _translate("main_window", "parse_node_rels_with_props"))
        self.__parse_method_combo.setItemText(4, _translate("main_window", "parse_node_rels_with_props_map"))
        self.__parse_method_combo.setItemText(5, _translate("main_window", "parse_node_rels"))
        self.__parse_method_combo.setItemText(6, _translate("main_window", "parse_node_rels_with_props_array"))
        self.__nodes_and_relationships.setText(_translate("main_window", "Get all nodes and relationship"))
        self.__relationships_without_properties.setText(
            _translate("main_window", "Get all nodes\' relationship without node properties"))
        self.__add_filter.setText(_translate("main_window", "Add filter"))
        self.__filter_nodes_label.setText(_translate("main_window", "Filter nodes by properties"))
        self.__execute_property_filters_query.setText(_translate("main_window", "Execute"))
        item = self.__property_filters_table.horizontalHeaderItem(0)
        item.setText(_translate("main_window", "Property name"))
        item = self.__property_filters_table.horizontalHeaderItem(1)
        item.setText(_translate("main_window", "Property value"))
        self.__closed_round_bracket_first_node.setText(_translate("main_window", ")"))
        self.__open_round_bracket_first_node.setText(_translate("main_window", "("))
        self.__open_round_bracket_second_node.setText(_translate("main_window", "("))
        self.__relationships_between_with_properties.setText(_translate("main_window", "With properties"))
        self.__closed_square_bracket.setText(_translate("main_window", "]->"))
        self.__relationships_between_without_properties.setText(_translate("main_window", "Without properties"))
        self.__open_square_bracket.setText(_translate("main_window", "-["))
        self.__close_round_bracket_second_node.setText(_translate("main_window", ")"))
        self.__first_node_type_label.setText(_translate("main_window", "First node label"))
        self.__second_node_type_label.setText(_translate("main_window", "Second node label"))
        self.__execute_label.setText(_translate("main_window", "<html><head/><body><p>Execute</p></body></html>"))
        self.__relationship_type_label.setText(_translate("main_window", "Relationship"))
        self.__query_results_label.setText(_translate("main_window", "QUERY RESULTS"))
        item = self.__triples_table.horizontalHeaderItem(0)
        item.setText(_translate("main_window", "Individual"))
        item = self.__triples_table.horizontalHeaderItem(1)
        item.setText(_translate("main_window", "Property"))
        item = self.__triples_table.horizontalHeaderItem(2)
        item.setText(_translate("main_window", "Value"))
        self.__tabs.setTabText(self.__tabs.indexOf(self.__graph_db), _translate("main_window", "Graph DB"))
        self.__sparql_user_query_label.setText(_translate("main_window", "Query"))
        self.__sparql_execute_user_query.setText(_translate("main_window", "Execute"))
        self.__sparql_query_results_label.setText(_translate("main_window", "QUERY RESULTS"))
        item = self.__sparql_triples_table.horizontalHeaderItem(0)
        item.setText(_translate("main_window", "Individual"))
        item = self.__sparql_triples_table.horizontalHeaderItem(1)
        item.setText(_translate("main_window", "Property"))
        item = self.__sparql_triples_table.horizontalHeaderItem(2)
        item.setText(_translate("main_window", "Value"))
        self.__sparql_add_filter.setText(_translate("main_window", "Add filter"))
        self.__sparql_filter_nodes_label.setText(_translate("main_window", "Filter nodes by properties"))
        item = self.__sparql_property_filters_table.horizontalHeaderItem(0)
        item.setText(_translate("main_window", "Property name"))
        item = self.__sparql_property_filters_table.horizontalHeaderItem(1)
        item.setText(_translate("main_window", "Property value"))
        self.__sparql_execute_property_filters_query.setText(_translate("main_window", "Execute"))
        self.__sparql_endpoint_label.setText(_translate("main_window", "SPARQL endpoint"))
        self.__tabs.setTabText(self.__tabs.indexOf(self.__sparql), _translate("main_window", "SPARQL endpoint"))

    ## initialize (add first row) to filters table, both SPARQL and graph DB
    def initialize_filters_tables(self):
        property_name = QtWidgets.QLineEdit(self.__layoutWidget)
        property_value = QtWidgets.QLineEdit(self.__layoutWidget)

        self.__property_filters_table.setCellWidget(0, 0, property_name)
        self.__property_filters_table.setCellWidget(0, 1, property_value)

        property_name = QtWidgets.QLineEdit(self.__layoutWidget)
        property_value = QtWidgets.QLineEdit(self.__layoutWidget)

        self.__sparql_property_filters_table.setCellWidget(0, 0, property_name)
        self.__sparql_property_filters_table.setCellWidget(0, 1, property_value)

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

    ## method related to __execute_user_query button
    def execute_user_query(self):
        dbms_query = DbmsQuery(self.__user_query.text(), self.__parse_method_combo.currentText())
        write_results(self.__triples_table, dbms_query.run_query().get_triples())

    ## method related to __add_filter or sparql_add_filer, add a row in a filter table
    # @param: table: in which table the filter should be added
    def add_filter(self, table):
        row_count = table.rowCount()
        table.insertRow(row_count)

        property_name = QtWidgets.QLineEdit(self.__layoutWidget)
        property_value = QtWidgets.QLineEdit(self.__layoutWidget)

        table.setCellWidget(row_count, 0, property_name)
        table.setCellWidget(row_count, 1, property_value)

    ## method related to __nodes_and_relationships, execute cypher query that retrieves all nodes (with properties) and relationships between them
    def nodes_and_relationships(self):
        dbms_query = DbmsQuery(
            "MATCH (n) OPTIONAL MATCH (n)-[r]-(m) RETURN ID(n), properties(n), TYPE(r), ID(m), properties(m)",
            "parse_node_rels_with_props_map")
        write_results(self.__triples_table, dbms_query.run_query().get_triples())

    ## method related to __relationships_without_properties, execute cypher query that retrieves all relationships between nodes
    def relationships_without_properties(self):
        dbms_query = DbmsQuery("MATCH (n)-[r]-(m) RETURN ID(n), TYPE(r), ID(m)", "parse_node_rels")
        write_results(self.__triples_table, dbms_query.run_query().get_triples())

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

        write_results(self.__triples_table, dbms_query.run_query().get_triples())

    ## method related to __relationships_between_without_properties
    ## relationships, eventually of a specified type, between nodes, eventually of a specified type (both for first and second node); ndoe properties are not retrieved
    def relationships_between_without_properties(self):
        first_node_label_text, second_node_label_text, relationship_text = self.__add_dots_to_filter()

        dbms_query = DbmsQuery(
            "MATCH (n" + first_node_label_text + ")-[r" + relationship_text + "]-(m" + second_node_label_text + ") RETURN ID(n), TYPE(r), ID(m)",
            "parse_node_rels")
        write_results(self.__triples_table, dbms_query.run_query().get_triples())

    ## method related to __execute_property_filters_query
    ## all nodes that have the specified values for the specified properties, retrieves all nodes if nothing is specified
    def execute_property_filters_query(self):
        query = "MATCH(n) "
        query_where = " AND ".join(
            [(("n." + self.__property_filters_table.cellWidget(i, 0).text() + "=" +
               (str(self.__property_filters_table.cellWidget(i, 1).text())
                if self.__property_filters_table.cellWidget(i, 1).text().isdecimal() else ("'" + self.__property_filters_table.cellWidget(i, 1).text()) + "'"))
              if self.__property_filters_table.cellWidget(i,0).text() != "" and self.__property_filters_table.cellWidget(i, 1).text() != "" else '')
             for i in range(0, self.__property_filters_table.rowCount())])

        if query_where != "":
            query += "WHERE " + query_where
        query += " RETURN ID(n), properties(n)"

        dbms_query = DbmsQuery(query, "parse_property_map")
        write_results(self.__triples_table, dbms_query.run_query().get_triples())

    ## method related to __sparql_execute_user_query
    def sparql_execute_user_query(self):
        cloud_query = CloudQuery(self.__sparql_user_query, self.__sparql_endpoint.text())

        write_results(self.__sparql_triples_table, cloud_query.run_query().get_triples())

    def sparql_execute_property_filters_query(self):
        pass

## function to write triples in a specified three column table
# @param: table: in which table the tripels should be added
# @param: triples: triples to add
def write_results(table, triples):
    table.setRowCount(0)
    for triple in triples:
        row_count = table.rowCount()
        table.insertRow(row_count)
        table.setItem(row_count, 0, QTableWidgetItem(str(triple[0])))
        table.setItem(row_count, 1, QTableWidgetItem(str(triple[1])))
        table.setItem(row_count, 2, QTableWidgetItem(str(triple[2])))

    return table


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    main_window = QtWidgets.QMainWindow()
    ui = UiMainWindow(main_window)
    ui.initialize_filters_tables()
    ui.setup_signals()
    main_window.show()
    sys.exit(app.exec_())
