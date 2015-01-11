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

// (1) Rename the struct from RetStatus to ReturnStatus
struct ReturnStatus {
  1: i32 err_code,
  // (2) Remove err_str field from a struct
  // 2: string err_str,
  3: string traceback,
}

// (3) Remove an argument 'prefix_len' which will just be ignored in old clients.
// (4) Add an argument 'size' to the V4InterfaceAdd method with a default value
//     for old clients. Note that it uses index 5, skipping 4 which was allocated to "prefix_len"
// (5) Changed position of second and third arguments
service InterfacesService {
  ReturnStatus V4InterfaceAdd(
    1: string if_name,
    3: string prefix,
    2: i32 unit,
    5: i32 size = 48,
  );

  ReturnStatus V4InterfaceDelete(
    1: string if_name,
    2: i32 unit,
    3: string prefix,
    4: i32 prefix_len,
  ) throws (1:InvalidInterfaceException ae);

// Adding 2 new function
  list<IF> InterfaceGet(1: string if_name);
  IfStatus InterfaceStatsGet(1: string if_name);
}