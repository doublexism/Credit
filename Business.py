
import pandas as pd
import os


user_info = pd.read_csv('./train/user_info_train.txt', names=['ID', 'gender', 'career', 'education', 'marriage', 'hukou'])
bank_detail = pd.read_csv('./train/bank_detail_train.txt', names=['ID', 'timestamp_bank', 'type', 'money', 'salary'])
browse_history = pd.read_csv('./train/browse_history_train.txt', names=['ID', 'timestamp_browse', 'browse_data', 'browser_code'])
bill_detail = pd.read_csv('./train/bill_detail_train.txt', names=['ID', 'timestamp_bill', 'bank_id', 'last_bill', 'last_repayment', 'credit_line', 'current_balance', 'minimum_payments', 'amount_transactions','current_money','adjust_money','cycle_interest','available_money','cash_advance','repayment_status'])
loan_time = pd.read_csv('./train/loan_time_train.txt', names=['ID', 'timestamp_money'])
overdue = pd.read_csv('./train/overdue_train.txt', names=['ID', 'Label'])

# 数据维度

print(user_info.shape)
print(overdue.shape)
print(loan_time.shape)

print(bill_detail.shape)
print(browse_history.shape)
print(bank_detail.shape)
