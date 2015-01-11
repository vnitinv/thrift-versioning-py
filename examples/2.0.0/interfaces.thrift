exception InvalidInterfaceException {
  1: string message
}

struct IF {
    1: string if_name,
    2: i32 unit,
    3: string prefix,
    4: i32 size,
}

enum IfStatus {DOWN = 0, UP = 1}

struct ReturnStatus {
  1: i32 err_code,
  3: string traceback,
}

service InterfacesService {
  ReturnStatus V4InterfaceAdd(
    1: string if_name,
    3: string prefix,
    2: i32 unit,
    5: i32 size = 48,
  );

  // (1) renamed V4InterfaceDelete to V4InterfaceRemove
  ReturnStatus V4InterfaceRemove(
    1: string if_name,
    2: i32 unit,
    3: string prefix,
    4: i32 prefix_len,
  ) throws (1:InvalidInterfaceException ae);

  // (2) changing parameter type
  list<IF> InterfaceGet(1: i32 unit);

  // (3) removed function InterfaceStatsGet
  /*
  IfStatus InterfaceStatsGet(1: string if_name);*/
}