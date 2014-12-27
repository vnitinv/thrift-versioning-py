struct Account {
  1: required double id,
  2: string name,
  3: string city,
  // (1) Adding another optional field
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
  // (2) Remove the declared exception from the method signature
  Account lookup(1:double id, 2:Mode mode, 3:bool active),
  // (3) Change method signature to return Account instead of void
  // (4) Add exception to method signature
  Account update(1:Account account) throws (1:InvalidAccountException ae)
}