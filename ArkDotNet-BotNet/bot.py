import socket, random, string
from threading import Thread

global bot
global botid

banner = ''' 
       d8888         888      8888888b.           888    888b    888          888    
      d88888         888      888  "Y88b          888    8888b   888          888    
     d88P888         888      888    888          888    88888b  888          888    
    d88P 888 888d888 888  888 888    888  .d88b.  888888 888Y88b 888  .d88b.  888888 
   d88P  888 888P"   888 .88P 888    888 d88""88b 888    888 Y88b888 d8P  Y8b 888    
  d88P   888 888     888888K  888    888 888  888 888    888  Y88888 88888888 888    
 d8888888888 888     888 "88b 888  .d88P Y88..88P Y88b.  888   Y8888 Y8b.     Y88b.  
d88P     888 888     888  888 8888888P"   "Y88P"   "Y888 888    Y888  "Y8888   "Y888 
                                                                                     
### Criadores: Cyber, Kristian, Command, Gates, invi e R3brake:
\n'''

class connection:

    def __init__(self, sock=None):
        pass

        ##Sockets - Kristian
    def connect(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.sock.connect((self.host, int(self.port)))
        message = "0~"+toolbox().getid()+"~"+toolbox().getLocalIP()
        self.sock.sendall(message)
        while 1:
            message = self.sock.recv(4096)
            if message != " ":
                print("Mensagem: " + message)
                self.sock.close()
                break
                                  
    def sendall(self, msg):
        self.sock.sendall(msg[totalsent:])
            
    def receive(self):
        msg = ''
        while len(msg) < MSGLEN:
            chunk = self.sock.recv(MSGLEN-len(msg))
            if chunk == '':
                raise RuntimeError("socket esta broked!")
            msg = msg + chunk
        return msg
    ##Fim

class bot:
    
    def __init__(self):
        self.connections = []
        self.ip = toolbox().getLocalIP()
        self.id = toolbox().idGenerator(toolbox().strGenerator(20), self.ip)
        global botid
        botid = self.id
        print("Iniciando com id: " + self.id)
        Thread(target = self.listenForUser).start()
        Thread(target = self.listener).start()
        
    def addConnection(self, host,port=8889):
        conn = connection()
        try:
            conn.connect(host, port)
            self.connections.append(conn)
            return "Bot adicionado " + host + ":" + port
        except:
            return "Nao consegui conectar no bot " + host + ":" + port
    def listener(self):
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 8889
        self.listener.bind(("", port))
        self.listener.listen(10)
        print("entrada do bot na porta " + str(port))
        while 1:
            conn, addr = self.listener.accept()           
            message = conn.recv(1024).strip("\n").split("~")
            
            
        
    def listenForUser(self):
        self.uListener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 8888
        self.uListener.bind(("", port))
        self.uListener.listen(10)
        print("Entrada do usuario na porta " + str(port))
        while 1:
            conn, addr = self.listener.accept()
            print('Conectado em ' + addr[0] + ':' + str(addr[1]))
            message = conn.recv(1024).strip("\n").split(" ")
            if not message: 
                break
            if message[0] == "addcon":
                if len(message) == 2:
                    output = self.addConnection(message[1])
                else:
                    output = self.addConnection(message[1], message[2])
                conn.sendall(output)
                print(output + "\n")
    

class toolbox:
    def __init__(self):
        pass
    def strGenerator(self,size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    def getLocalIP(self):
        return socket.gethostbyname(socket.gethostname())
    def idGenerator(self,hashcode , ip):
        hashls = list(hashcode)
        ipls = list("".join(ip.split(".")))
        result = [item for sublist in zip(hashls,ipls) for item in sublist]
        return "".join(result)
    def getid(self):
        global bot
        return botid
   
def main():
    global bot
    bot = bot()


main()
