exception ExampleException {
  1:i32 code,
  2:string message
}


service ThriftService {
  string ping()
  i32 inc(1:i32 value)
}

