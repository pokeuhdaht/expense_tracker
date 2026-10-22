import json
import argparse






if __name__ == "__main__":

parser = argparse.ArgumentParser(description='Spendy - Simple CLI Expense Tracking App')

sub_parser = parser.add_subparsers(dest='command')

add_expense_parser = sub_parser.add_parser('add', help='Add an expense to the report.')
add_expense_parser.add_argument('--description','-d', type=str, help='Name of expense.')
add_expense_parser.add_argument('--amount','-d', tpye=float, help='Cost of expense.')

args = parser.parse_args()

if args.description:
    print(f"description is: {args.description}")
if args.amount:
    print(f"amount is: {args.amount}")