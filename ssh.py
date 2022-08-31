import paramiko
from sys import stderr, stdin, stdout
from flask import Flask, render_template, redirect, request,url_for
 
app = Flask(__name__)
 
@app.route('/dashboard/<nome>')
def dashboard(nome):
       comando = 'useradd '+ nome
       address =  '20.226.70.95'
       username = 'root'
       password = '171716'
 
       ssh = paramiko.SSHClient()
       ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       ssh.connect(hostname=address, username=username, password=password)
       stdin, stdout, stderr = ssh.exec_command(comando)
 
       stdin.close()
 
       return render_template('senha.html', nome = nome)
 
 
 

 
@app.route('/index',methods = ['POST', 'GET'])
def index():
   if (request.method == 'POST'):
      user = request.form['nome']
 
 
      return redirect(url_for('dashboard',nome = user))
   else:
 
      return render_template('index.html')
 
 
@app.route('/senha',methods = ['POST', 'GET'])
def wd():
   if (request.method == 'POST'):
      senha = request.form['senha']
      nome = request.form['nome']
 
 
      return redirect(url_for('senha',nome = nome ,senha = senha))
   else:
 
      return render_template('senha.html')
 
 
 
@app.route('/senha/<nome>/<senha>')
def senha(nome, senha):
       comandosenha = 'echo "' + nome + ':' + senha + '" | chpasswd'
       address =  '20.226.70.95'
       username = 'root'
       password = '171716'
 
       ssh = paramiko.SSHClient()
       ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       ssh.connect(hostname=address, username=username, password=password)
       stdin, stdout, stderr = ssh.exec_command(comandosenha)
 
       stdin.close()
 
       return nome, senha
 
 
 
 
 
if __name__ == "__main__":
	app.run(debug = True)




