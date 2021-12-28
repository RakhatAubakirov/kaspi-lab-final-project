from dataclasses import dataclass
from typing import List, Optional
from uuid import uuid4, UUID
import pandas as pd
from pandas import DataFrame, Series
from decimal import Decimal

import psycopg2

from account.account import Account


class TableAccounts:
    conn = psycopg2.connect(
        "dbname=project_banking port=5433 user=postgres password=20002000alim17alim11 host=127.0.0.1")

    def update_row(self, phone_number: str, balance: int) -> None:
        cur = self.conn.cursor()
        cur.execute(""" 
                UPDATE accounts SET balance = %s WHERE phone_number = %s; 
        """, (balance, phone_number))
        self.conn.commit()

    def insert_row(self, id_: UUID, phone_number: str, balance: Decimal, currency: str) -> None:
        cur = self.conn.cursor()
        cur.execute(""" 
                INSERT INTO accounts (id, phone_number, balance, currency) VALUES (%s, %s, %s, %s); 
                """, (str(id_), phone_number, balance, currency))
        self.conn.commit()

    def delete_row(self, account: Account) -> None:
        if account.id_ is None:
            print('No such account')
        cur = self.conn.cursor()
        cur.execute("DELETE FROM accounts WHERE id = %s;", (str(account.id_),))
        self.conn.commit()


    def get_row(self, account: Account) -> Optional[Account]:
        if account.id_ is None:
            print('No such account')
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM accounts WHERE id = %s;", (str(account.id_),))
        data = cur.fetchall()
        cols = [x[0] for x in cur.description]
        df = pd.DataFrame(data, columns=cols)
        return self.pandas_row_to_account(row=df.iloc[0])

    def get_rows(self) -> List[Account]:
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM accounts;")
        data = cur.fetchall()
        cols = [x[0] for x in cur.description]
        df = pd.DataFrame(data, columns=cols)
        return [self.pandas_row_to_account(row) for index, row in df.iterrows()]

    def get_rows2(self) -> List[Account]:
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM accounts;")
        # data = cur.fetchall()
        f = "%10s %40s %20s %20s"

        print(f % ('id', 'phone_number', 'balance', 'currency'))
        print("=" * 125)
        for i in cur:
            for j in i:
                print('%14s' % j, end=' ')
            print()
        print("=" * 125)

    def get_balance(self, phone_number: str) -> int:
        cur = self.conn.cursor()
        cur.execute(""" 
            SELECT balance from accounts WHERE phone_number = %s;""", (str(phone_number),))
        balance = cur.fetchone()
        return balance[0]