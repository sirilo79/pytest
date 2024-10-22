import zmq

# ZeroMQ 컨텍스트 생성
context = zmq.Context()

# REP(응답) 소켓 생성
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")  # 모든 IP에서 5555 포트를 통해 수신

print("Server started, waiting for messages...")

while True:
    # 클라이언트로부터 메시지 수신
    message = socket.recv_string()
    print(f"Received request: {message}")
    
    # 처리할 내용을 추가할 수 있음 (예: 데이터베이스 조회, 연산 등)
    response = f"Hello, {message}!"

    # 응답 전송
    socket.send_string(response)
