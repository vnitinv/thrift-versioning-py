struct Account {
  1: required double id,
  2: string name,
  3: string city
}

enum Mode {
  ADMIN = 0,
  PARTNER = 1
}

exception InvalidAccountException {
  1: string message
}

service Accounts {
  Account lookup(1:double id, 2:Mode mode, 3:bool active) throws (1:InvalidAccountException ae),
  void update(1:Account account)
}

