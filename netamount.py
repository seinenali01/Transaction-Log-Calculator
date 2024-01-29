def compute_net_amount(transaction_log):
    net_amount = 0

    for transaction in transaction_log:
       action, amount = transaction.split()
       amount = int(amount)

       if action == 'D':
           net_amount += amount
       elif action == 'W':
           net_amount -= amount
    return net_amount

def main():
    transaction_log = []
    print("Enter the Transaction Log. Type 'done' when finished.")

    while True:
        transaction = input("Transaction: ")
        if transaction.lower() == 'done':
           break
        transaction_log.append(transaction)
    net_amount = compute_net_amount(transaction_log)
    print(f"Net Amount: {net_amount}")

if __name__ == "__main__":
    main()                           
