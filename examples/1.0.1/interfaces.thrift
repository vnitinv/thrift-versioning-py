exception InvalidInterfaceException {
  1: string message
}

struct RetStatus {
  1: i32 err_code,
  2: string err_str,
  // (1) Adding another optional field
  3: string traceback,
}

service InterfacesService {
  // (2) Remove the declared exception from the method signature
  RetStatus V4InterfaceAdd(
    1: string if_name,
    2: i32 unit,
    3: string prefix,
    4: i32 prefix_len,
  );

  // (3) Change method signature to return RetStatus instead of bool
  // (4) Add exception to method signature
  // bool V4InterfaceDelete(
  RetStatus V4InterfaceDelete(
    1: string if_name,
    2: i32 unit,
    3: string prefix,
    4: i32 prefix_len,
  ) throws (1:InvalidInterfaceException ae);

  // (5) Adding exception to a function with void return type
  void InterfaceExists(1: string if_name,
  ) throws (1:InvalidInterfaceException ae);
}