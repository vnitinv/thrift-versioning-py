exception InvalidInterfaceException {
  1: string message
}

struct RetStatus {
  1: i32 err_code,
  2: string err_str,
}

service InterfacesService {

  RetStatus V4InterfaceAdd(
    1: string if_name,
    2: i32 unit,
    3: string prefix,
    4: i32 prefix_len,
  ) throws (1:InvalidInterfaceException ae);

  bool V4InterfaceDelete(
    1: string if_name,
    2: i32 unit,
    3: string prefix,
    4: i32 prefix_len,
  );
  void InterfaceExists(1: string if_name);
}