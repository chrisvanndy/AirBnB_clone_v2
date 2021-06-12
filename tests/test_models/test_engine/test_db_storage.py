#!/usr/bin/python3
""" test for console"""
import os
import sys
import unittest
import MySQLdb
from io import StringIO
from datetime import datetime
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

args = {
    'user': os.getenv('HBNB_MYSQL_USER'),
    'passwd': os.getenv('HBNB_MYSQL_PWD'),
    'db': os.getenv('HBNB_MYSQL_DB'),
    'host': os.getenv('HBNB_MYSQL_HOST')
}


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'file')
class TestDBStorage(unittest.TestCase):
    """class for test dbstorage"""

    def test_DB_create(self):
        """test state for DB"""
        self.db_connection = MySQLdb.connect(**args)
        self.cursor = self.db_connection.cursor()
        self.cursor.execute('SELECT count(*) FROM states')
        length1 = self.cursor.fetchone()[0]
        self.cursor.close()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State name='Montana'")
        self.db_connection = MySQLdb.connect(**args)
        self.cursor = self.db_connection.cursor()
        self.cursor.execute('SELECT count(*) FROM states')
        length2 = self.cursor.fetchone()[0]
        self.assertEqual(length2, length1 + 1)

    def test_DB_create2(self):
        """test state for DB"""
        self.db_connection = MySQLdb.connect(**args)
        self.cursor = self.db_connection.cursor()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State name='California'")
            s_id = f.getvalue()[:-1]
        self.cursor.execute('SELECT count(*) FROM cities')
        length1 = self.cursor.fetchone()[0]
        self.cursor.close()
        with patch('sys.stdout', new=StringIO()) as f:
            name = 'name = "San Francisco"'
            command = 'create City {} "{}"'
            command = command.format(s_id, name)
            HBNBCommand().onecmd(command)
            c_id = f.getvalue()[:-1]
        self.db_connection = MySQLdb.connect(**args)
        self.cursor = self.db_connection.cursor()
        self.cursor.execute('SELECT count(*) FROM cities')
        length2 = self.cursor.fetchone()[0]
        self.assertEqual(length2, length1 + 1)
