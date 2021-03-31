import socket, time

HOST = "irc.twitch.tv"
PORT = 6667
token = "oauth:zc9vb8b2h39x7m6lwadbkym5z3zjwr"
nickname = 'g0thangelbot'
channel = 'bt0tv'

s = socket.socket()
s.connect((HOST, PORT))

s.send(f"PASS {token}\r\n".encode('utf-8'))
s.send(f"NICK {nickname}\r\n".encode('utf-8'))
s.send(f"JOIN #{channel}\r\n".encode('utf-8'))

while True:
    try:
        r = s.recv(2048).decode('utf-8')

        # format strings
        c = r.split(":", -1)
        v = r.split("!")
        v += v[0].split(":")
        ###################

        f = open("tweet", "a")
        f.write(c[-1])
        f.close()
        print("{}: {}".format(v[-1], c[len(c) - 1]))

        f = open('log', "a")
        f.write("{}: {}".format(v[-1], c[len(c) - 1]))
        f.close()

        time.sleep(0.1)

    except Exception:
        time.sleep(0.1)