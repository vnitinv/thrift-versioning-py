/*
 * This interface has changes to version 1 which are backward binary compatible
 * but not source compatible (the client code needs to be changed).
 */

// (1) Rename the struct from Account to AccountID
struct AccountID {
  1: required double id,
  2: string name,
  // (2) Remove a field from a struct
  // 3: string city,
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
  // (3) Remove an argument 'active' which will just be ignored in old clients.
  // (4) Add an argument 'name' to the account lookup method with a default value for old clients.  Note that
  //     it uses index 4, skipping 3 which was allocated to "active"
  // (5) Change position of first and second arguments
  // check http://stackoverflow.com/questions/14878004/default-arguments-with-default-values-in-thrift-python-client
  AccountID lookup(2:Mode mode, 1:double id, 4:string name="*"),
  AccountID update(1:AccountID account) throws (1:InvalidAccountException ae)
  // Adding 2 new function
  bool credit(1:double id, 2: double amount)
  double credit_balance(1:double id)
  bool debit(1:double id, 2: double amount)
}