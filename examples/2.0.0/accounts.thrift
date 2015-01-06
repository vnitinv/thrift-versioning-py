struct AccountID {
  1: required double id,
  2: string name,
  4: double age
}

enum Mode {
  ADMIN = 0,
  PARTNER = 1
}

exception InvalidAccountException {
  1: string message
}

service Accounts {
  AccountID lookup(2:Mode mode, 1:double id, 4:string name="*"),
  // Rename update method
  AccountID update_account(1:AccountID account)
  // Change the return type of function
  void credit(1:double id, 2: double amount)
  // Removed function credit_balance
  // double credit_balance(1:double id)
  // changing parameter type
  bool debit(1:double id, 2: i32 amount)
}

