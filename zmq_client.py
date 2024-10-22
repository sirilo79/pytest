import zmq

# ZeroMQ 컨텍스트 생성
context = zmq.Context()

# REQ(요청) 소켓 생성
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")  # 서버에 연결

# 서버에 메시지 전송
message = "World"
print(f"Sending request: {message}")
socket.send_string(message)

# 서버로부터 응답 수신
response = socket.recv_string()
print(f"Received reply: {response}")
